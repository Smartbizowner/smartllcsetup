import os
import glob
import re

target_files = [
    "bank-approval-website.html",
    "start-a-us-company.html",
    "get-an-ein.html",
    "us-bank-account.html",
    "itin.html",
    "us-paypal.html",
    "annual-renewal.html",
    "irs-return-filing.html",
    "maintain-llc.html",
    "llc-reinstatement.html",
    "llc-closing.html",
    "contact.html"
]

EXTRA_CSS = """
<style>
/* ── INJECTED PREMIUM UI ── */
.glass-box {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.4);
  border-radius: var(--r);
  padding: 32px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.02);
}
.tax-highlight {
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  border-left: 4px solid var(--blue);
  padding: 24px;
  border-radius: 0 var(--r) var(--r) 0;
  margin: 32px 0;
}
.tax-highlight strong, .tax-highlight h3 { color: #111; }
</style>
</head>
"""

def replace_ol_with_proc(match):
    content = match.group(1)
    lis = re.findall(r'<li[^>]*>(.*?)</li>', content, re.DOTALL)
    new_html = '<div class="proc-list" style="margin-top:24px;margin-bottom:32px;">\n'
    for i, li in enumerate(lis):
        num = i + 1
        strong_match = re.search(r'<strong>(.*?)</strong>(.*)', li, re.DOTALL)
        if strong_match:
            title = strong_match.group(1).strip()
            desc = strong_match.group(2).strip()
            # Some lists have <br> or other elements, remove trailing hyphens
            if desc.startswith('- '): desc = desc[2:]
            if desc.startswith('— '): desc = desc[2:]
            new_html += f'''
    <div class="proc-row">
      <div class="proc-n">{num}</div>
      <div>
        <strong>{title}</strong>
        <span>{desc}</span>
      </div>
    </div>
'''
        else:
            new_html += f'''
    <div class="proc-row">
      <div class="proc-n">{num}</div>
      <div>
        <span style="font-size:14px;font-weight:600;color:var(--gray-700);">{li.strip()}</span>
      </div>
    </div>
'''
    new_html += '</div>'
    return new_html

def replace_ul_with_get(match):
    content = match.group(1)
    lis = re.findall(r'<li[^>]*>(.*?)</li>', content, re.DOTALL)
    new_html = '<div class="get-list" style="margin-top:16px;margin-bottom:32px;">\n'
    for li in lis:
        strong_match = re.search(r'<strong>(.*?)</strong>(.*)', li, re.DOTALL)
        if strong_match:
            title = strong_match.group(1).strip()
            desc = strong_match.group(2).strip()
            if desc.startswith('- '): desc = desc[2:]
            if desc.startswith('— '): desc = desc[2:]
            new_html += f'''
    <div class="get-row">
      <div class="get-icon"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"></path></svg></div>
      <div>
        <strong>{title}</strong>
        <span>{desc}</span>
      </div>
    </div>
'''
        else:
            new_html += f'''
    <div class="get-row">
      <div class="get-icon"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"></path></svg></div>
      <div>
        <span style="font-size:14px;font-weight:500;color:var(--gray-700);">{li.strip()}</span>
      </div>
    </div>
'''
    new_html += '</div>'
    return new_html


def process_file(file):
    if not os.path.exists(file):
        print(f"Skipping {file}, does not exist")
        return
        
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    article_match = re.search(r'(<section class="article-wrap">)(.*?)(</section>)', html, re.DOTALL)
    if not article_match:
        print(f"NO article-wrap in {file}")
        return
        
    prefix = article_match.group(1)
    inner = article_match.group(2)
    suffix = article_match.group(3)
    
    # 1. Replace <ol> ... </ol>
    inner = re.sub(r'<ol[^>]*>(.*?)</ol>', replace_ol_with_proc, inner, flags=re.DOTALL | re.IGNORECASE)
    
    # 2. Replace <ul> ... </ul>
    inner = re.sub(r'<ul[^>]*>(.*?)</ul>', replace_ul_with_get, inner, flags=re.DOTALL | re.IGNORECASE)
    
    # 3. Enhance <div class="alert">
    inner = re.sub(r'<div class="alert"[^>]*>', '<div class="glass-box" style="margin:32px 0;">', inner)
    
    # 4. Enhance <div class="warn"> 
    inner = re.sub(r'<div class="warn"[^>]*>', '<div class="tax-highlight" style="margin:32px 0;">', inner)
    
    new_html = html[:article_match.start()] + prefix + inner + suffix + html[article_match.end():]
    
    # Inject extra CSS
    if 'INJECTED PREMIUM UI' not in new_html:
        new_html = new_html.replace('</head>', EXTRA_CSS)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print(f"Upgraded {file}")

import sys
folder = "/Users/mayankmalik/Documents/SBO WEBSITE "
for f in target_files:
    process_file(os.path.join(folder, f))
