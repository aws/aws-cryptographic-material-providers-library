#!/bin/bash

# Change to the directory where this script is located
cd "$(dirname "$0")"

# Get the list of files from get_release_unignored_files.sh
release_unignored_files=$(./get_release_unignored_files.sh)

# Run `git rm --cached` from the root directory
cd ../..

while IFS= read -r line; do
    # Only proceed if the line is not empty
    if [[ -n "$line" ]]; then
        git rm --cached "$line"
    fi
done <<< "$release_unignored_files"