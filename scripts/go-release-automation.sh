#!/bin/bash

# Automated Go Release Process Script
# This script automates steps 1-8 of the Go release process

set -e  # Exit on error

# Check if project name and version is provided
if [ $# -lt 2 ]; then
  echo "Usage: $0 <project-name> [version]"
  echo "Example: $0 ComAmazonawsKms v0.1.0"
  exit 1
fi

PROJECT_NAME=$1
VERSION=$2

# Function to map project name to release directory name
get_release_dir_name() {
  local project=$1
  case "$project" in
    "AwsCryptographicMaterialProviders") echo "mpl" ;;
    "AwsCryptographyPrimitives") echo "primitives" ;;
    "ComAmazonawsKms") echo "kms" ;;
    "ComAmazonawsDynamodb") echo "dynamodb" ;;
    "StandardLibrary") echo "smithy-dafny-standard-library" ;;
    *) echo "$project" ;;  # Default to the original name if no mapping exists
  esac
}

cd ..

echo "Starting Go release process for $PROJECT_NAME $VERSION"

# Check if this is an AWS SDK project
IS_AWS_SDK=false
if [[ "$PROJECT_NAME" == "ComAmazonawsKms" || "$PROJECT_NAME" == "ComAmazonawsDynamodb" ]]; then
  IS_AWS_SDK=true
  echo "Detected AWS SDK project: $PROJECT_NAME"
fi

# Step 1: Pull the latest smithy-dafny and libraries git submodules
echo "Step 1: Pulling latest git submodules..."
git submodule update --init --recursive

# Step 2: Go to the project directory
echo "Step 2: Navigating to $PROJECT_NAME..."
cd "$PROJECT_NAME" || { echo "Error: Project directory $PROJECT_NAME not found"; exit 1; }

# Step 3: Build using make commands
echo "Step 3: Building project..."
make polymorph_dafny
make polymorph_go
make transpile_go
make test_go

# Step 4: Show git diff
echo "Step 4: Showing git diff for review..."

# Step 5: Run Go tools in ImplementationFromDafny-go
echo "Step 5: Running Go tools in ImplementationFromDafny-go..."
cd runtimes/go/ImplementationFromDafny-go || { echo "Error: ImplementationFromDafny-go directory not found"; exit 1; }

if [ "$IS_AWS_SDK" = false ]; then
  # Remove all shim.go files for non-AWS SDK projects
  find . -name "*shim.go" -type f -delete
  echo "Removed all shim.go files"
fi

echo "Running goimports..."
goimports -w .

echo "Running go get -u..."
go get -u

echo "Running go mod tidy..."
go mod tidy

echo "Running go build to check for errors..."
go build --gcflags="-e" ./...

# Get the mapped release directory name
RELEASE_DIR_NAME=$(get_release_dir_name "$PROJECT_NAME")

# Step 6: Copy files to releases directory
echo "Step 6: Copying files to releases/go/$RELEASE_DIR_NAME..."

# Use rsync to copy files while excluding specific ones
rsync -av --exclude="ImplementationFromDafny.go" --exclude="ImplementationFromDafny-go.dtr" ./ "../../../releases/go/$RELEASE_DIR_NAME/"

# Step 7: Run Go tools in releases directory
echo "Step 7: Running Go tools in releases/go/$RELEASE_DIR_NAME..."

cd "../../../../releases/go/$RELEASE_DIR_NAME" || { echo "Error: releases directory not found"; exit 1; }

echo "Running goimports..."
goimports -w .
echo "Running go get -u..."
go get -u ./...

echo "Running go mod tidy..."
go mod tidy

echo "Running go build to check for errors..."
go build --gcflags="-e" ./...

# Step 8: Prepare for commit
echo "Step 8: Preparing for commit..."
cd ../../../ || { echo "Error: Cannot navigate back to project root"; exit 1; }

git add "releases/go/$RELEASE_DIR_NAME"
git status

echo ""
echo "Go release process completed successfully!"
echo ""
echo "Next steps:"
echo "1. Review the changes and commit them:"
echo "   git commit -m \"Release $RELEASE_DIR_NAME Go module ${VERSION}\""
echo "2. Create a PR with your changes"
echo "3. After PR is merged, create a tag:"
echo "   git tag releases/go/${RELEASE_DIR_NAME}/${VERSION}"
echo "4. Push the tag:"
echo "   git push --tags"
echo ""