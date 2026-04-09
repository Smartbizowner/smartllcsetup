import os
import re

targets = [
    "start-a-us-company.html",
    "get-an-ein.html",
    "us-bank-account.html",
    "stripe-shopify.html",
    "itin.html",
    "us-paypal.html",
    "annual-renewal.html",
    "irs-return-filing.html",
    "maintain-llc.html",
    "llc-reinstatement.html",
    "llc-closing.html",
    "contact.html",
    "bank-approval-website.html",
    "llc-taxes-non-resident.html",
    "llc-tax-estimator.html"
]

def process_html(filename):
    if not os.path.exists(filename):
        return
        
    with open(filename, 'r') as f:
        html = f.read()
        
    match = re.search(r'<section class="article-wrap">(.*?)</section>\s*<!-- FOOTER -->', html, re.DOTALL)
    if not match:
        print(f"[{filename}] article-wrap section not found in expected location.")
        return
        
    inner_html = match.group(1).strip()
    
    parts = re.split(r'(<h2[^>]*>.*?</h2\s*>)', inner_html, flags=re.DOTALL)
    
    blocks = []
    
    if parts[0].strip():
        blocks.append({
            'heading': '',
            'content': parts[0].strip()
        })
        
    for i in range(1, len(parts), 2):
        heading = parts[i]
        content = parts[i+1].strip() if (i+1) < len(parts) else ""
        blocks.append({
            'heading': heading,
            'content': content
        })
        
    if not blocks:
        return
        
    new_html = ""
    for idx, block in enumerate(blocks):
        # Alternate backgrounds
        bg_style = 'background:var(--gray-50)' if idx % 2 == 1 else 'background:#fff'
        
        content = block['content']
        # Upgrade alerts to tax-highlights
        content = re.sub(r'<div class="alert">', r'<div class="tax-highlight">', content)
        
        # Inject glass-box wrapping for the first major paragraph if it exists on gray sections
        # to replicate the industry block layout exactly
        if idx % 2 == 1:
             content = re.sub(r'^\s*(<p>.*?</p>)', r'<div class="glass-box">\n\1\n</div>', content, count=1, flags=re.DOTALL)
             
        new_section = f'<section style="{bg_style}; padding:64px 0; border-bottom:1px solid var(--border);">\n'
        new_section += f'  <div class="wrap" style="max-width:800px; margin:0 auto;">\n'
        # Keep .article-wrap on the inner div so nested CSS works (like lists and strong tags)
        new_section += f'    <div class="article-wrap" style="padding:0; margin:0;">\n'
        
        if block['heading']:
            heading = re.sub(r'(<h2)', r'\1 style="margin-top:0;"', block['heading'])
            new_section += f'      {heading}\n'
            
        new_section += f'      {content}\n'
        new_section += f'    </div>\n'
        new_section += f'  </div>\n'
        new_section += f'</section>\n'
        
        new_html += new_section
        
    full_new_html = html.replace(match.group(0), new_html + "\n<!-- FOOTER -->")
    
    if html != full_new_html:
        with open(filename, 'w') as f:
            f.write(full_new_html)
        print(f"Restructured: {filename}")

for t in targets:
    process_html(t)
