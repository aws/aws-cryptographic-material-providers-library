#!/bin/bash

cd "$(dirname "$0")"

# Define the markers
START_MARKER="# START_RELEASE_IGNORED_FILES"
END_MARKER="# END_RELEASE_IGNORED_FILES"

# Initialize variables
in_block=false

# Read each line in the .gitignore file
while IFS= read -r line; do
    # Trim whitespace from the line
    trimmed_line=$(echo "$line" | xargs)

    # Check for the start marker
    if [[ "$trimmed_line" == "$START_MARKER" ]]; then
        in_block=true
        continue
    fi

    # Check for the end marker
    if [[ "$trimmed_line" == "$END_MARKER" ]]; then
        in_block=false
        continue
    fi

    # If within the block, and the line is not a comment or empty, print it
    if $in_block && [[ -n "$trimmed_line" && "$trimmed_line" != \#* ]]; then
        echo "$trimmed_line"
    fi
done < ../../.gitignore