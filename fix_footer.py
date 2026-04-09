import re

file_path = "/Users/mayankmalik/Documents/SBO WEBSITE /sbo-llc-final.html"

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Find the start of the footer
footer_start = text.find("<!-- FOOTER -->")
if footer_start != -1:
    # We want to replace everything from <!-- FOOTER --> to the end of the file.
    header_content = text[:footer_start]
    
    new_footer = """<!-- FOOTER -->
<footer style="background:#111;color:#fff;padding:64px 20px 24px;border:none;">
  <div class="wrap" style="max-width:1000px;display:grid;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));gap:32px;margin-bottom:48px;">
    <div>
      <h4 style="font-size:15px;font-weight:700;margin-bottom:16px;">Solutions</h4>
      <div style="display:flex;flex-direction:column;gap:10px;">
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Start a US Company</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Get an EIN</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">US Bank Account</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Stripe &amp; Shopify</a>
      </div>
    </div>
    <div>
      <h4 style="font-size:15px;font-weight:700;margin-bottom:16px;">LLC Management</h4>
      <div style="display:flex;flex-direction:column;gap:10px;">
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Annual Renewal</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">LLC Reinstatement</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">IRS Return Filing</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">LLC Closing</a>
      </div>
    </div>
    <div>
      <h4 style="font-size:15px;font-weight:700;margin-bottom:16px;">Compare States</h4>
      <div style="display:flex;flex-direction:column;gap:10px;">
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Wyoming vs Delaware</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Wyoming vs New Mexico</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Delaware vs Florida</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Texas vs Colorado</a>
      </div>
    </div>
    <div>
      <h4 style="font-size:15px;font-weight:700;margin-bottom:16px;">Resources</h4>
      <div style="display:flex;flex-direction:column;gap:10px;">
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Blog</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Guides</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Help Center</a>
        <a href="#" style="font-size:13px;color:var(--gray-400);transition:color .2s;text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--gray-400)'">Contact Us</a>
      </div>
    </div>
  </div>

  <div style="border-top:1px solid #333;padding-top:24px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;max-width:1000px;margin:0 auto;font-size:12px;color:var(--gray-500);">
    <div>&copy; 2024 Smart LLC Setup &amp; Smart Biz Owner. All rights reserved.</div>
    <div style="display:flex;gap:12px;">
      <a href="#" style="color:var(--gray-500);text-decoration:none;">Privacy Policy</a>
      <a href="#" style="color:var(--gray-500);text-decoration:none;">Terms of Service</a>
    </div>
  </div>
</footer>
</body>
</html>
"""
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(header_content + new_footer)
    print("Footer updated successfully.")
else:
    print("Failed to find footer section.")
