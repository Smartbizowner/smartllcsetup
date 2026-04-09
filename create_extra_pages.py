import re

def create_page(filename, title, label, h1, sub, article_content):
    with open('stripe-shopify.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the title
    content = re.sub(r'<title>.*?</title>', f'<title>{title} | Smart Biz Owner</title>', content)
    
    # Replace the label in the hero section
    content = re.sub(r'<div class="label">.*?</div>', f'<div class="label">{label}</div>', content, count=1)
    
    # Replace the h1 in the hero section
    content = re.sub(r'<h1 style="font-size:clamp\(26px,5vw,42px\);font-weight:800;margin-bottom:12px;">.*?</h1>',
                     f'<h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">{h1}</h1>', content)
                     
    # Replace the sub text in the hero section
    content = re.sub(r'<p class="sub" style="max-width:680px;margin:0 auto;">.*?</p>',
                     f'<p class="sub" style="max-width:680px;margin:0 auto;">{sub}</p>', content, count=1)
                     
    # Replace the article content
    content = re.sub(r'<section class="article-wrap">.*?</section>',
                     f'<section class="article-wrap">\n{article_content}\n</section>', content, flags=re.DOTALL)
                     
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Created {filename}")

taxes_article = """  <h2>US LLC \u2013 A Potential Tax Haven For Foreigners. Why?</h2>
  <p>A US-based LLC can have great tax advantages, especially for foreign entrepreneurs abroad.</p>
  <p>An LLC is a pass-through tax entity. What this means is that the LLC is not taxed directly. Instead, the profits and losses of the business pass through to its owners, who report them on their personal tax returns.</p>

  <h3>Tax-free LLC income for foreign owners of a US LLC</h3>
  <p>A little-known fact is that the US can be one of the biggest tax havens in the world. A US LLC opened by a non-US citizen or nonresident can arguably allow for earnings that are not taxed in the US.</p>
  <p>Of course, specific rules apply to avoid LLC taxes.</p>
  <p>Effectively, foreigners are only subject to US tax if they are \u201cengaged in a trade or business in the United States\u201d (ETOB). If your business is <strong>not</strong> ETOB, even if it generates income in the US, the income is not taxed in the US.</p>
  
  <div class="alert">
    <strong>However, you are engaged in a trade or business (ETOB) in the US if:</strong>
    <ol style="margin-bottom:0;margin-top:12px;">
      <li>You have at least one \u201cdependent agent\u201d in the US, which are employees or companies that work for you almost exclusively, and</li>
      <li>This dependent agent does something substantial to further your business in the US, as opposed to something purely administrative, or</li>
      <li>You are engaged in \u201cconsiderable, continuous, and regular\u201d business in the US.</li>
    </ol>
  </div>
  
  <p>If you meet these conditions, you have to pay on those earnings. We analyze the bank statements and nature of the business to confirm whether it is ETOB or NON-ETOB.</p>

  <h2>What to file, and how much it costs (SBO US Certified CPA)</h2>
  <p>You will transfer all profits and losses of the business to your personal tax return in whichever country you are in. For example, you will file an ITR in India for your earnings.</p>
  <p><strong>But still, you have to pay specific fees in the US to keep your LLC in good standing and active.</strong></p>

  <h3>Annual Fees Breakdown</h3>
  <div style="overflow-x:auto;margin-bottom:32px;">
    <table style="width:100%;border-collapse:collapse;font-size:14px;text-align:left;">
      <thead>
        <tr style="background:var(--gray-50);border-bottom:2px solid var(--border);">
          <th style="padding:12px;border:1px solid var(--border);">State</th>
          <th style="padding:12px;border:1px solid var(--border);">State Annual Fee</th>
          <th style="padding:12px;border:1px solid var(--border);">Agent Address (Outside Agent)</th>
          <th style="padding:12px;border:1px solid var(--border);">Federal IRS Fee</th>
          <th style="padding:12px;border:1px solid var(--border);">CPA + IRS Filing (&lt;$100k)</th>
          <th style="padding:12px;border:1px solid var(--border);">Total</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:12px;border:1px solid var(--border);font-weight:600;">Wyoming</td>
          <td style="padding:12px;border:1px solid var(--border);">$60</td>
          <td style="padding:12px;border:1px solid var(--border);">$25</td>
          <td style="padding:12px;border:1px solid var(--border);">$150</td>
          <td style="padding:12px;border:1px solid var(--border);">$75</td>
          <td style="padding:12px;border:1px solid var(--border);font-weight:700;color:var(--green-d);">$310</td>
        </tr>
        <tr>
          <td style="padding:12px;border:1px solid var(--border);font-weight:600;">Delaware</td>
          <td style="padding:12px;border:1px solid var(--border);">$300</td>
          <td style="padding:12px;border:1px solid var(--border);">$50</td>
          <td style="padding:12px;border:1px solid var(--border);">$150</td>
          <td style="padding:12px;border:1px solid var(--border);">$75</td>
          <td style="padding:12px;border:1px solid var(--border);font-weight:700;color:var(--green-d);">$575</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3>Accounting + IRS Filing Fee For Different Revenues</h3>
  <ul>
    <li>Under $300,000 = <strong>$120</strong></li>
    <li>Under $500,000 = <strong>$150</strong></li>
    <li>Under $1,000,000 = <strong>$250</strong></li>
  </ul>

  <h3>Documents we need to handle your US taxation:</h3>
  <ul>
    <li><strong>Company Bank Statements</strong></li>
    <li><strong>Owner Drawings:</strong> These are assets you withdraw from your business for your personal use.</li>
    <li><strong>Owner Investments:</strong> Any capital you personally invested into the business.</li>
    <li><strong>1099 Form:</strong> If any is received or issued (can be found on the company portal). A 1099 Form is a federal income tax form; businesses must file a 1099 form with the IRS.</li>
  </ul>
  
  <p>That's it; if we need anything more, we will contact you.</p>

  <div style="margin-top:48px;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:var(--gray-50);text-align:center;">
    <h3 style="margin-top:0;margin-bottom:16px;">Ready to start your US taxation with SBO?</h3>
    <p style="margin-bottom:24px;color:var(--gray-700);">Contact us on Skype or WhatsApp with the above documents, and we will get it sorted.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
      <a href="https://wa.me/917566631566?text=Hello%2C%20I%20need%20help%20with%20the%20facebook%20solution%20setup.%20" target="_blank" rel="noopener" class="btn-green" style="padding:12px 24px;">Message on WhatsApp</a>
      <a href="https://join.skype.com/invite/oGxE9jjpZFyQ" target="_blank" rel="noopener" class="btn-outline" style="padding:12px 24px;">Join Mayank on Skype</a>
    </div>
    <div style="margin-top:20px;">
      <a href="https://www.instagram.com/mayankmaliik/" target="_blank" rel="noopener" style="color:var(--blue);text-decoration:underline;font-size:14px;font-weight:500;">Follow Mayank Malik on Instagram</a>
    </div>
  </div>"""

bank_article = """  <p>Watch the video below to understand in-depth, with examples, how your website should look for easy bank and payment gateway approval.</p>

  <div style="margin:40px 0;border-radius:var(--r);overflow:hidden;border:1px solid var(--border);aspect-ratio:16/9;box-shadow:0 8px 24px rgba(0,0,0,0.06);">
    <iframe width="100%" height="100%" src="https://www.youtube.com/embed/-ipUrr53ttE?si=Cgxm4TXHf9VC1We2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="display:block;"></iframe>
  </div>

  <h2>Store Setup Checklist for Approval</h2>
  
  <div class="alert" style="margin-bottom:24px;">
    <h3 style="margin-top:0;margin-bottom:12px;color:#111;">1. Complete Company Info</h3>
    <ul style="margin-bottom:0;">
      <li>Add full company details (Name, Address, Email, Phone) in the footer.</li>
      <li>Include your professional logo clearly in both the header/footer and the checkout page.</li>
      <li>Ensure all required target countries are added in the market settings of your Shopify store.</li>
    </ul>
  </div>

  <div class="alert" style="margin-bottom:24px;">
    <h3 style="margin-top:0;margin-bottom:12px;color:#111;">2. Proper Product &amp; Store Setup</h3>
    <ul style="margin-bottom:0;">
      <li>Have a minimum of 15\u201320 products actively listed.</li>
      <li>Properly display featured products directly on the homepage.</li>
      <li>Do <strong>not</strong> keep all products on sale or at the exact same price (banks flag this as suspicious or temporary).</li>
    </ul>
  </div>

  <div class="alert" style="margin-bottom:24px;">
    <h3 style="margin-top:0;margin-bottom:12px;color:#111;">3. Realistic Checkout Experience</h3>
    <ul style="margin-bottom:0;">
      <li>Show the PayPal option visually (even if it isn't fully active yet, displaying the badge builds trust).</li>
      <li>Clearly display your shipping methods, including any FREE shipping offers.</li>
      <li>Include all vital trust links systematically in both the header and footer (Home, Shop, Contact Us, Privacy Policy, Terms of Service, Refunds).</li>
    </ul>
  </div>
  
  <p style="margin-top:32px;">Following these guidelines demonstrates to compliance officers that your business is legitimate, reducing your chances of arbitrary rejections when applying for banking or Stripe integration.</p>"""

create_page('llc-taxes-non-resident.html', 'US LLC Taxes For Non-US Resident', 'US Taxation', 'US LLC Taxes For Non-US Resident', 'Understand the tax advantages of a US-based LLC for foreign entrepreneurs and how to handle annual filings.', taxes_article)

create_page('bank-approval-website.html', 'SBO LLC - Bank Approval Website', 'Bank Compliance', 'SBO LLC - Bank Approval Website', 'An in-depth guide with examples on how your website should look for easy bank and payment gateway approval.', bank_article)
