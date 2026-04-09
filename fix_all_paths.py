#!/usr/bin/env python3
"""
Fix all internal links and asset paths site-wide for Vercel compatibility.
- Change relative logo.png, favicon.png → /logo.png, /favicon.png (root-relative)
- Change relative footer page links → root-relative /page.html
- Ensure logo href="/index.html" stays as-is (already correct)
- Leave external http/https links untouched
"""

import os
import re

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

# These are the internal page files that exist (relative → root-relative)
INTERNAL_PAGES = [
    "start-a-us-company.html",
    "get-an-ein.html",
    "us-bank-account.html",
    "stripe-shopify.html",
    "annual-renewal.html",
    "irs-return-filing.html",
    "maintain-llc.html",
    "llc-reinstatement.html",
    "llc-closing.html",
    "wyoming-vs-delaware.html",
    "wyoming-vs-new-mexico.html",
    "delaware-vs-florida.html",
    "texas-vs-colorado.html",
    "llc-tax-estimator.html",
    "privacy-policy.html",
    "terms-of-service.html",
    "contact.html",
]

# Asset files that should use root-relative paths
ASSET_FILES = [
    "logo.png",
    "favicon.png",
    "business_document.png",
    "articles_of_org.png",
]

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    # 1. Fix asset src/href paths: relative → root-relative
    # src="logo.png" → src="/logo.png"
    # href="favicon.png" → href="/favicon.png"
    for asset in ASSET_FILES:
        # Fix src= references  (must not already be /asset)
        content = re.sub(
            r'(src=")(?!/)' + re.escape(asset) + r'"',
            r'\1/' + asset + '"',
            content
        )
        # Fix href= references for favicon
        content = re.sub(
            r'(href=")(?!/)' + re.escape(asset) + r'"',
            r'\1/' + asset + '"',
            content
        )

    # 2. Fix internal page links: relative → root-relative
    # href="start-a-us-company.html" → href="/start-a-us-company.html"
    # But DON'T change /index.html or already root-relative ones
    for page in INTERNAL_PAGES:
        # Match href="page.html" (not already starting with /)
        content = re.sub(
            r'(href=")(?!/)' + re.escape(page) + r'"',
            r'\1/' + page + '"',
            content
        )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED: {os.path.basename(filepath)}")
    else:
        print(f"OK (no changes): {os.path.basename(filepath)}")
    
    return content != original

def main():
    html_files = [f for f in os.listdir(SITE_DIR) if f.endswith('.html')]
    html_files.sort()
    
    fixed = 0
    for filename in html_files:
        filepath = os.path.join(SITE_DIR, filename)
        if fix_file(filepath):
            fixed += 1
    
    print(f"\n✅ Done: {fixed}/{len(html_files)} files updated")

    # Verify no old relative paths remain
    print("\n--- Verification: Checking for any remaining bare relative internal links ---")
    for filename in html_files:
        filepath = os.path.join(SITE_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = []
        for page in INTERNAL_PAGES:
            # Check for href="page.html" without leading slash
            pattern = r'href="(?!/)' + re.escape(page) + r'"'
            matches = re.findall(pattern, content)
            if matches:
                issues.append(f"  ⚠️  Still has relative: {matches}")
        
        for asset in ASSET_FILES:
            pattern = r'src="(?!/)' + re.escape(asset) + r'"'
            matches = re.findall(pattern, content)
            if matches:
                issues.append(f"  ⚠️  Still has relative asset: {matches}")
            # Also check href= for favicon
            pattern = r'href="(?!/)' + re.escape(asset) + r'"'
            matches = re.findall(pattern, content)
            if matches:
                issues.append(f"  ⚠️  Still has relative asset href: {matches}")

        if issues:
            print(f"\n{filename}:")
            for issue in issues:
                print(issue)
        else:
            print(f"  ✅ {filename} — clean")

if __name__ == '__main__':
    main()
