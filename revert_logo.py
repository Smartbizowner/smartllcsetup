import glob
import re

for f in glob.glob('*.html'):
    with open(f, 'r') as file:
        content = file.read()

    new_content = re.sub(
        r'<a href="\./index\.html" class="nav-logo">\s*<img[^>]*src="\./logo[^>]*>\s*</a>',
        '<a href="./index.html" class="nav-logo"><img src="./logo.png" alt="Smart LLC Setup"></a>',
        content
    )
    new_content = re.sub(
        r'<a href="\.\./index\.html" class="nav-logo">\s*<img[^>]*src="\.\./logo[^>]*>\s*</a>',
        '<a href="../index.html" class="nav-logo"><img src="../logo.png" alt="Smart LLC Setup"></a>',
        new_content
    )

    if content != new_content:
        with open(f, 'w') as file:
            file.write(new_content)
        print(f"Reverted logo in {f}")
