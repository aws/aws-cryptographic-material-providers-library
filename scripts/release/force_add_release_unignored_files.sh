cd "$(dirname "$0")"

release_unignored_files=$(./get_release_unignored_files.sh)

# Run `git add` from root directory
cd ../..

while IFS= read -r line; do
    # Only proceed if the line is not empty
    if [[ -n "$line" ]]; then
        git add -f --all "$line"
    fi
done <<< "$release_unignored_files"