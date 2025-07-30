#!/bin/bash

# Go Release Process Script
# Used for copying go files to release directory and make a commit

set -e  # Exit on error

# Check if project name and version is provided
if [ $# -ne 3 ]; then
  echo "Usage: $0 <function> <project-name> [version]"
  echo "Example: $0 get_release_dir_name ComAmazonawsKms v0.1.0"
  echo "Example: $0 run_release_script ComAmazonawsKms v0.1.0"
  exit 1
fi

# Function to map project name to release directory name
get_release_dir_name() {
  local project=$1
  case "$project" in
    "AwsCryptographicMaterialProviders") echo "mpl" ;;
    "AwsCryptographyPrimitives") echo "primitives" ;;
    "ComAmazonawsKms") echo "kms" ;;
    "ComAmazonawsDynamodb") echo "dynamodb" ;;
    "StandardLibrary") echo "smithy-dafny-standard-library" ;;
    "DynamoDbEncryption") echo "dynamodb-esdk" ;;
    *) echo "Error: Unknown project name: $project" >&2; return 1 ;;
  esac
}

run_release_script() {
  PROJECT_NAME=$1
  VERSION=$2

  echo "Starting Go release script for $PROJECT_NAME $VERSION"

  # Check if this is an AWS SDK project
  IS_AWS_SDK=false
  if [[ "$PROJECT_NAME" == "ComAmazonawsKms" || "$PROJECT_NAME" == "ComAmazonawsDynamodb" ]]; then
    IS_AWS_SDK=true
    echo "Detected AWS SDK project: $PROJECT_NAME"
  fi

  # Pull the latest smithy-dafny and libraries git submodules
  echo " Pulling latest git submodules..."
  git submodule update --init --recursive

  # Go to the project directory
  echo " Navigating to $PROJECT_NAME..."
  cd "$PROJECT_NAME" || { echo "Error: Project directory $PROJECT_NAME not found"; exit 1; }

  # Build using make commands
  echo " Building project..."
  # make polymorph_dafny
  # make polymorph_go
  # make transpile_go
  # make test_go

  # Run Go tools in ImplementationFromDafny-go
  echo " Running Go tools in ImplementationFromDafny-go..."
  cd runtimes/go/ImplementationFromDafny-go || { echo "Error: ImplementationFromDafny-go directory not found"; exit 1; }

  if [ "$IS_AWS_SDK" = false ]; then
    # Remove all shim.go files for non-AWS SDK projects
    find . -name "*shim.go" -type f -delete
    echo "Removed all shim.go files"
  fi

  # run_go_tools()

  # Replacement directives are removed to get package from go pkg instead of local copy
  echo "Removing all replace directives from go.mod..."
  go mod edit -json | jq -r '.Replace[].Old.Path' | xargs -n1 go mod edit -dropreplace

  # Get the mapped release directory name
  RELEASE_DIR_NAME=$(get_release_dir_name "$PROJECT_NAME")

  # Copy files to releases directory
  echo " Copying files to releases/go/$RELEASE_DIR_NAME..."

  # Use rsync to copy files while excluding following ones:
    # ImplementationFromDafny.go: This file is for devlopment. Users is expected use API(s) from `*/api_client.go`
    # ImplementationFromDafny-go.dtr: This is the dafny translation record only needed for code generation
    # go.sum: This files will be updated by go mod tidy
  rsync -av --exclude="ImplementationFromDafny.go" --exclude="ImplementationFromDafny-go.dtr" --exclude="go.sum" ./ "$(git rev-parse --show-toplevel)/releases/go/$RELEASE_DIR_NAME/"

  case "$PROJECT_NAME" in
    "AwsEncryptionSDK"|"DynamoDbEncryption") copy_examples ;;
  esac

  # Run Go tools in releases directory
  echo "Running Go tools in releases/go/$RELEASE_DIR_NAME..."

  cd "$(git rev-parse --show-toplevel)/releases/go/$RELEASE_DIR_NAME/" || { echo "Error: releases directory not found"; exit 1; }

  # run_go_tools()

  case "$PROJECT_NAME" in
    "AwsEncryptionSDK"|"DynamoDbEncryption") test_examples ;;
  esac

  # Prepare for commit
  echo "creating a branch..."

  # git checkout -b "golang-release-staging-branch/$RELEASE_DIR_NAME/${VERSION}"
  # git add *

  # git commit -m "Release $RELEASE_DIR_NAME Go module ${VERSION}"
  # git push origin "golang-release-staging-branch/$RELEASE_DIR_NAME/${VERSION}"
}

run_go_tools() {
    echo "Running goimports..."
    goimports -w .
    echo "Running go get -u..."
    go get -u ./...

    echo "Running go mod tidy..."
    go mod tidy

    echo "Running go build to check for errors..."
    go build --gcflags="-e" ./...
}

copy_examples() {
  local source_dir
  case "$PROJECT_NAME" in
    "AwsEncryptionSDK") source_dir="$PROJECT_NAME/runtimes/go/ImplementationFromDafny-go/examples" ;;
    "DynamoDbEncryption") source_dir="Examples/runtimes/go" ;;
    *) return ;;
  esac
  
  cd "$(git rev-parse --show-toplevel)/$source_dir"
  echo "Removing all replace directives from go.mod and only adding replacement for ESDK"
  go mod edit -json | jq -r '.Replace[].Old.Path' | xargs -n1 go mod edit -dropreplace
  go mod edit -replace=github.com/aws/aws-encryption-sdk/releases/go/encryption-sdk=../
  rsync -av --exclude="go.sum" ./ "$(git rev-parse --show-toplevel)/releases/go/$RELEASE_DIR_NAME/examples"
}

test_examples() {
  cd "$(git rev-parse --show-toplevel)/releases/go/$RELEASE_DIR_NAME/examples" || { echo "Error: examples directory not found"; exit 1; }
  # run_go_tools
  go run main.go
}

"$@"