import os

def get_files(directory):
    """Retrieve and sort Quarto files by filename, excluding 'all.qmd'."""
    files = [f for f in os.listdir(directory) if f.endswith('.qmd') and f != 'all.qmd']
    files.sort()  # Sort by filename
    return files

def update_navigation(directory, files):
    """Update each file with previous and next navigation links."""
    for i, file in enumerate(files):
        file_path = os.path.join(directory, file)
        with open(file_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0)
            f.truncate()  # Clear the file to rewrite it
            
            # Remove existing navigation if present
            content = content.rsplit('---', 1)[0]

            # Define new navigation links
            prev_link = f'[Previous Post]({files[i-1]})' if i > 0 else ""
            next_link = f'[Next Post]({files[i+1]})' if i < len(files) - 1 else ""
            navigation_md = f"\n---\n{prev_link} {next_link}\n"

            # Rewrite the file with updated content and new navigation
            f.write(content.strip() + navigation_md)

def main():
    directory = 'projects/data-viz'  # Path to your Quarto files
    files = get_files(directory)
    update_navigation(directory, files)

if __name__ == "__main__":
    main()
