#!/bin/bash
# Build the Tailwind CSS for nf-docs
# Run this script after modifying the HTML template

set -e

cd "$(dirname "$0")"

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm install
fi

echo "Building Tailwind CSS..."
npm run build

echo "Done! CSS size: $(wc -c < ../src/nf_docs/templates/tailwind.css | tr -d ' ') bytes"
