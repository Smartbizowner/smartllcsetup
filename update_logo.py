import glob

for f in glob.glob('*.html'):
    with open(f, 'r') as file:
        content = file.read()
    
    new_content = content.replace(
        '<img src="./logo.png" alt="Smart LLC Setup">',
        '<img src="./logo.png" alt="Smart LLC Setup" style="height: 48px; object-fit: contain;">'
    )
    new_content = new_content.replace(
        '<img src="../logo.png" alt="Smart LLC Setup">',
        '<img src="../logo.png" alt="Smart LLC Setup" style="height: 48px; object-fit: contain;">'
    )

    if content != new_content:
        with open(f, 'w') as file:
            file.write(new_content)
        print(f'Updated {f}')
