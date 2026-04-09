import os
import glob
import re

def fix_links():
    html_files = glob.glob('*.html')
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        
        # Replace href="/..." with href="./..." 
        # (Exclude external links with //)
        content = re.sub(r'href="/(?!/)', r'href="./', content)
        
        # Replace src="/..." with src="./..."
        content = re.sub(r'src="/(?!/)', r'src="./', content)

        if content != original:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed paths in {file}")

if __name__ == '__main__':
    fix_links()
