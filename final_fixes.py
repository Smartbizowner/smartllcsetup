import glob
import os

html_files = glob.glob("*.html")

mobile_pad_css = """
<style>
/* ── MOBILE SPACING FIX ── */
@media(max-width:768px){
  section { padding: 32px 0 !important; }
  section[style*="padding:64px"] { padding: 32px 20px !important; }
  .article-wrap { padding: 24px 16px !important; }
  .article-wrap h2 { margin-top: 24px !important; margin-bottom: 12px !important; font-size: 24px !important; }
  .glass-box { padding: 20px !important; margin: 24px 0 !important; }
  .tax-highlight { padding: 16px !important; margin: 24px 0 !important; }
}
</style>
"""

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    
    # Enable hero-docs on mobile for index.html ONLY
    if filepath == "index.html":
        content = content.replace('.hero-docs{display:none}', '.hero-docs{display:flex; transform:scale(0.85); transform-origin:top center; margin-top:16px; margin-bottom:-40px;}')
        content = content.replace('section style="background:#fff;border-bottom:1px solid var(--border);padding:40px 20px;"', 'section class="mobile-pad" style="background:#fff;border-bottom:1px solid var(--border);padding:40px 20px;"')
        
    # Inject mobile spacing fixes globally
    if "/* ── MOBILE SPACING FIX ── */" not in content:
        content = content.replace("</head>", mobile_pad_css + "\n</head>")

    # Replace logo with optimized format, adding intrinsic dimensions to kill layout shift
    content = content.replace(
        '<img src="./logo.png" alt="Smart LLC Setup" style="height: 48px; object-fit: contain;">',
        '<img src="./logo_optim.png" alt="Smart LLC Setup" width="108" height="48" style="height: 48px; width: auto; object-fit: contain;" fetchpriority="high">'
    )
    content = content.replace(
        '<img src="../logo.png" alt="Smart LLC Setup" style="height: 48px; object-fit: contain;">',
        '<img src="../logo_optim.png" alt="Smart LLC Setup" width="108" height="48" style="height: 48px; width: auto; object-fit: contain;" fetchpriority="high">'
    )
    
    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filepath}")
