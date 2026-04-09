import os
import glob
import re

files = glob.glob("*.html")

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    original = content
    
    # 1. Fix the Tax Estimator padding (and all other sections that lost lateral padding)
    # Change: section { padding: 32px 0 !important; }
    # To: section { padding-top: 32px !important; padding-bottom: 32px !important; }
    content = re.sub(r'section\s*\{\s*padding:\s*32px\s+0\s*!important;\s*\}', 
                     r'section { padding-top: 32px !important; padding-bottom: 32px !important; }', content)
                     
    # Also fix the fallback: section[style*="padding:64px"] { padding: 32px 20px !important; }
    # This was a patch, we can just leave it or improve it, but it shouldn't hurt.
    
    # 2. Make the logo bigger
    # Change: .nav-logo img{height:30px;object-fit:contain}
    # To: .nav-logo img{height:44px;object-fit:contain}
    content = re.sub(r'\.nav-logo img\{height:30px', r'.nav-logo img{height:44px', content)
    
    # Also some files might have it separated with spaces.
    content = re.sub(r'\.nav-logo\s+img\s*\{\s*height:\s*30px', r'.nav-logo img{height:44px', content)

    # 3. Fix the ITIN/PayPal service box icon squishing on mobile
    # We find the inline style for that box in itin.html and us-paypal.html
    # "display:flex;align-items:flex-start;gap:20px;" -> add flex-wrap:wrap;
    # Actually wait. If we just add flex-wrap:wrap it will stack the text under the icon if it gets too tight.
    # Let's target the exact string:
    target_style = r'margin-top:48px;display:flex;align-items:flex-start;gap:20px;padding:32px;'
    new_style = r'margin-top:48px;display:flex;flex-wrap:wrap;align-items:center;gap:20px;padding:32px;'
    
    content = content.replace(target_style, new_style)
    
    # Also find: flex-shrink:0;width:48px;height:48px;
    # Let's ensure the icon has margin-bottom if it wraps. It naturally will if there's gap:20px.
    
    if original != content:
        with open(f, 'w') as file:
            file.write(content)
        print(f"Updated {f}")
