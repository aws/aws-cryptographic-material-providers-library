#!/bin/bash

# Runs `git add -f --all X` for every entry X from list_gitignore_bypass_release_files.sh.
# This is used to bypass the .gitignore to commit files that should ONLY be committed for releases.

# Change to the directory where this script is located
cd "$(dirname "$0")"

# Get the list of files from list_gitignore_bypass_release_files.sh
gitignore_bypass_release_files=$(./list_gitignore_bypass_release_files.sh)

# Run `git add` from root directory
cd ../..

while IFS= read -r line; do
    # Only proceed if the line is not empty
    if [[ -n "$line" ]]; then
        git add -f --all "$line"
    fi
done <<< "$gitignore_bypass_release_files"