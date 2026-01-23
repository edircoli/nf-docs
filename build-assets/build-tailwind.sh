#!/bin/bash
# Build the Tailwind CSS for nf-docs
# Run this script after modifying the HTML template

set -e

cd "$(dirname "$0")"

# Check dependencies are installed
if [ ! -d "node_modules" ]; then
    echo "Error: build-assets/node_modules not found."
    echo "Run 'cd build-assets && npm install' first."
    exit 1
fi

echo "Building Tailwind CSS..."
npm run build

echo "Done! CSS size: $(wc -c < ../src/nf_docs/templates/tailwind.css | tr -d ' ') bytes"
