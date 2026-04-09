import os
import glob
import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()

    # Extract blocks from index.html
    style_match = re.search(r'(<style>.*?</style>)', index_content, re.DOTALL)
    nav_match = re.search(r'(<nav>.*?</nav>)', index_content, re.DOTALL)
    footer_match = re.search(r'(<footer.*?>.*?</footer>)', index_content, re.DOTALL)

    if not (style_match and nav_match and footer_match):
        print("Could not find all required blocks in index.html")
        return

    style_block = style_match.group(1)
    nav_block = nav_match.group(1)
    footer_block = footer_match.group(1)

    html_files = [f for f in glob.glob('*.html') if f != 'index.html']
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace first <style> block
        content = re.sub(r'<style>.*?</style>', style_block, content, count=1, flags=re.DOTALL)
        
        # Replace <nav> block
        content = re.sub(r'<nav>.*?</nav>', nav_block, content, count=1, flags=re.DOTALL)
        
        # Replace <footer> block
        content = re.sub(r'<footer.*?>.*?</footer>', footer_block, content, count=1, flags=re.DOTALL)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {file}")

if __name__ == '__main__':
    main()
