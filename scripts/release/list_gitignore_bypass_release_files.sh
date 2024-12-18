#!/bin/bash
set -euxo pipefail

# Echoes every uncommented line between $START_MARKER and $END_MARKER in .gitignore.

# Run from this directory
cd "$(dirname "$0")"

# Define markers; only uncommented lines between these markers will be echoed
# Multiple pairs of markers are OK
START_MARKER="# START_RELEASE_IGNORED_FILES"
END_MARKER="# END_RELEASE_IGNORED_FILES"

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