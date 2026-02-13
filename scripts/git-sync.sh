#!/bin/bash

# Utility script to sync Domain Controller hub and its submodules

set -e

BRANCH=$(git rev-parse --abbrev-ref HEAD)

echo "Syncing Domain Controller Hub on branch: $BRANCH"

# Fetch latest for the hub
git fetch origin

# Sync submodules
echo "Updating submodules..."
git submodule update --init --recursive

# For each submodule, try to sync with the corresponding branch
git submodule foreach "
    echo \"Processing submodule: \$name\"
    # Try to checkout the same branch as the hub, fallback to develop
    if git rev-parse --verify origin/$BRANCH >/dev/null 2>&1; then
        TARGET_BRANCH=$BRANCH
    else
        TARGET_BRANCH=develop
    fi

    echo \"Targeting branch: \$TARGET_BRANCH\"
    git checkout \$TARGET_BRANCH || git checkout -b \$TARGET_BRANCH
    git fetch origin
    git merge origin/\$TARGET_BRANCH || echo \"Warning: Could not merge origin/\$TARGET_BRANCH in \$name\"
"

echo "Sync complete!"
