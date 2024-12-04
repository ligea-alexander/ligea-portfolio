#!/bin/bash
echo "Removing old 'docs' directory..."
rm -rf docs

echo "Rendering site..."
quarto render

echo "Renaming '_site' to 'docs'..."
mv _site docs

echo "Adding changes to git..."
git add .

echo "Committing changes..."
git commit -m "Update site contents"

echo "Pushing to GitHub..."
git push

echo "Done!"
