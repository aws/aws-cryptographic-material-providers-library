#!/bin/bash
set -euxo pipefail

# Runs `git rm --cached X` for every entry X from list_gitignore_bypass_release_files.sh.
# This is used to remove .gitignore'd files that were force-committed for a release.

# Change to the directory where this script is located
cd "$(dirname "$0")"

# Get the list of files from list_gitignore_bypass_release_files.sh
gitignore_bypass_release_files=$(./list_gitignore_bypass_release_files.sh)

# Run `git rm --cached` from the root directory
cd ../..

while IFS= read -r line; do
    # Only proceed if the line is not empty
    if [[ -n "$line" ]]; then
        git rm --cached "$line"
    fi
done <<< "$gitignore_bypass_release_files"