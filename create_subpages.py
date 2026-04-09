import os

base_file = "/Users/mayankmalik/Documents/SBO WEBSITE /index.html"
with open(base_file, "r", encoding="utf-8") as f:
    html = f.read()

# Extract head (up to </nav>)
head_split = html.split('</nav>', 1)
head_nav = head_split[0] + '</nav>\n'

custom_css = """
<style>
.article-wrap { max-width:800px; margin:0 auto; padding:64px 20px; }
.article-wrap h2 { font-size:28px; line-height:1.2; margin-top:40px; margin-bottom:16px; color:#111; font-weight:800; letter-spacing:-0.02em; }
.article-wrap h3 { font-size:20px; font-weight:700; margin-top:32px; margin-bottom:12px; color:#111; }
.article-wrap p, .article-wrap li { font-size:16px; color:var(--gray-700); line-height:1.75; margin-bottom:16px; }
.article-wrap ul { margin-bottom:24px; padding-left:24px; }
.article-wrap ol { margin-bottom:24px; padding-left:24px; }
.article-wrap ol li { margin-bottom:12px; }
.article-wrap .alert { background:var(--gray-50); border-left:4px solid var(--blue); padding:16px 24px; margin:24px 0; border-radius:4px; }
.article-wrap .alert strong { color:#111; }
</style>
"""
head_nav = head_nav.replace('</head>', custom_css + '\n</head>')

# Extract footer
footer_split = html.split('<!-- FOOTER -->', 1)
footer = '<!-- FOOTER -->' + footer_split[1]

# 1. Get an EIN page
ein_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">LLC Essentials</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">Get an EIN (Tax ID): When You Need One and How to Apply</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Everything you need to know about Employer Identification Numbers, from when you need one to the application process.</p>
  </div>
</section>

<section class="article-wrap">
  <h2>What Is an EIN?</h2>
  <p>An EIN (Employer Identification Number) is a 9-digit number assigned by the IRS to identify your business for tax purposes. It's also called a Tax ID Number, Federal Tax ID, or FEIN.</p>
  <p>Think of it as a Social Security Number for your business. While individuals use SSNs, businesses use EINs to identify themselves to the IRS, banks, and other entities.</p>
  
  <h2>When You Need an EIN</h2>
  <p>Even single-member LLCs should get an EIN. It's free, takes minutes, and protects your SSN from being shared with banks, clients, and vendors.</p>
  <p>Your LLC legally needs an EIN if you:</p>
  <ul>
    <li>Have employees or plan to hire</li>
    <li>Have multiple members (multi-member LLC)</li>
    <li>Choose to be taxed as a corporation (S-Corp or C-Corp election)</li>
    <li>Need to open a US business bank account (most banks require it)</li>
  </ul>
  
  <h2>Getting an EIN Without an SSN</h2>
  <div class="alert">
    <strong>For International Founders:</strong> You do NOT need an ITIN or SSN to get an EIN for your LLC! The EIN is for the business entity, not you personally. You can also use a foreign address on the application.
  </div>
  <p>International founders without a Social Security Number cannot use the IRS online application, so the process requires faxing or mailing Form SS-4. But don't worry, <strong>our LLC formation package handles this entirely for you</strong>. We will acquire your EIN directly from the IRS rapidly on your behalf, so you don't need to deal with the paperwork or long wait times.</p>
  
  <h2>Using Your EIN</h2>
  <p>Once you have your EIN, you can use it for opening your business bank accounts, filing zero-tax informational returns (Forms 1120/5472) for non-residents, and connecting to global payment processors like Stripe and PayPal.</p>
  
  <div style="margin-top:48px;text-align:center;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0;margin-bottom:12px;">Let us handle your EIN application</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:24px;">Start your business in minutes with Smart Biz Owner. We handle the IRS paperwork so you can focus on building.</p>
    <a class="btn-green" href="/index.html#pricing" style="display:inline-flex;padding:16px 32px;">Start Your LLC Now &rarr;</a>
  </div>
</section>
"""
page1 = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>Get an EIN (Tax ID) | Smart Biz Owner</title>') + ein_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /get-an-ein.html", "w", encoding="utf-8") as f:
    f.write(page1)


# 2. Start a US company
start_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">Getting Started</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">Start a US Company: The Ultimate Guide</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Everything you need to know about forming and running a US LLC. From choosing the right state to protecting your personal assets.</p>
  </div>
</section>

<section class="article-wrap">
  <h2>What is an LLC?</h2>
  <p>An LLC (Limited Liability Company) is a U.S. business structure that protects your personal assets (your house, car, personal bank accounts) from business debts and lawsuits. It separates you personally from the business entity, granting you peace of mind.</p>
  
  <h2>Why Form a US LLC?</h2>
  <ul>
    <li><strong>Limited Liability Protection:</strong> If the business faces a lawsuit or debt, your personal savings are entirely safe.</li>
    <li><strong>Tax Benefits (Pass-Through Taxation):</strong> For non-US residents with no physical operations inside the USA (No ETBUS), the US LLC essentially acts as a tax-free vehicle (0% corporate tax, 0% personal tax).</li>
    <li><strong>Global Credibility:</strong> Having a U.S. company adds massive credibility when dealing with global clients, suppliers, and investors.</li>
    <li><strong>Payment Processing:</strong> Unlocking access to Tier-1 infrastructure like Stripe, PayPal, and US banking.</li>
  </ul>
  
  <h2>The Step-by-Step Formation Process</h2>
  <p>To successfully form and launch your US LLC, you must complete the following critical steps:</p>
  <ol>
    <li><strong>Choose a State:</strong> We highly recommend <a href="wyoming-vs-delaware.html" style="color:var(--blue);text-decoration:underline;">Wyoming</a> for bootstrapped eCommerce/service businesses due to its unbeatable $60 annual fee and premier privacy.</li>
    <li><strong>File Articles of Organization:</strong> This is the official document filed with the Secretary of State.</li>
    <li><strong>Appoint a Registered Agent:</strong> A mandatory physical address in your state of formation that can receive legal documents on your behalf.</li>
    <li><strong>Get an EIN (Tax ID):</strong> Required to open a bank account and operate the business.</li>
  </ol>
  
  <div style="margin-top:48px;text-align:center;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0;margin-bottom:12px;">Ready to launch your U.S. business?</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:24px;">Don't navigate the overwhelming tax laws and state bureaucracy alone. Get it done right the first time.</p>
    <a class="btn-green" href="/index.html#pricing" style="display:inline-flex;padding:16px 32px;">Start Here As Soon As Possible &rarr;</a>
  </div>
</section>
"""
page2 = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>Start a US Company | Smart Biz Owner</title>') + start_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /start-a-us-company.html", "w", encoding="utf-8") as f:
    f.write(page2)


# 3. US Bank Account
bank_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">Business Banking</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">US Business Bank Accounts for International Entrepreneurs</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Open a US business bank account remotely. No SSN required, no US visit needed. Accept payments, pay vendors, and manage finances from anywhere in the world.</p>
  </div>
</section>

<section class="article-wrap">
  <h2>100% Remote Banking Setup</h2>
  <p>Gone are the days when you had to fly to the United States and walk into a physical branch to establish business banking. By forming your LLC with our platform, we unlock access to global digital-first banking networks.</p>
  <p><strong>There is NO Social Security Number (SSN) required</strong> and <strong>NO US visit needed</strong>. All you need is your home country passport, your U.S. LLC formation documents, and your EIN—all of which we provide to you within weeks.</p>
  
  <h2>Our Banking Partners</h2>
  <p>We boast strong relationships and familiarity with the world's most founder-friendly fintech platforms. Once your US company is successfully set up by us, foreigners are fully eligible to apply for business banking accounts via our partners, including:</p>
  
  <div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:16px;margin:32px 0;">
    <div style="padding:24px;border:1px solid var(--border);border-radius:var(--r);background:#fff;text-align:center;font-weight:700;font-size:18px;color:#111;">Relay</div>
    <div style="padding:24px;border:1px solid var(--border);border-radius:var(--r);background:#fff;text-align:center;font-weight:700;font-size:18px;color:#111;">Payoneer</div>
    <div style="padding:24px;border:1px solid var(--border);border-radius:var(--r);background:#fff;text-align:center;font-weight:700;font-size:18px;color:#111;">Wise</div>
    <div style="padding:24px;border:1px solid var(--border);border-radius:var(--r);background:#fff;text-align:center;font-weight:700;font-size:18px;color:#111;">Mercury</div>
    <div style="padding:24px;border:1px solid var(--border);border-radius:var(--r);background:#fff;text-align:center;font-weight:700;font-size:18px;color:#111;grid-column:1 / -1;">Lili</div>
  </div>
  
  <h2>Payment Processor Ready</h2>
  <p>Getting your bank account is the key to unlocking the global economy. By linking your new US bank account, you can instantly begin processing high-trust credit card transactions globally via major gateways such as <strong>Stripe, PayPal, Square, and Shopify Payments.</strong></p>
  
  <div style="margin-top:48px;text-align:center;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0;margin-bottom:12px;">From LLC to bank account in weeks</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:24px;">Start by forming your US LLC and acquiring your EIN. We'll guide you through the rest.</p>
    <a class="btn-green" href="/index.html#pricing" style="display:inline-flex;padding:16px 32px;">Start Your LLC Now &rarr;</a>
  </div>
</section>
"""
page3 = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>US Business Bank Account | Smart Biz Owner</title>') + bank_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /us-bank-account.html", "w", encoding="utf-8") as f:
    f.write(page3)

# 4. Stripe & Shopify
stripe_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">Global E-Commerce</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">Unlock Stripe & Shopify with a US LLC</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Bypass geographical restrictions, eliminate massive foreign exchange fees, and process payments globally by utilizing a US entity.</p>
  </div>
</section>

<section class="article-wrap">
  <h2>The Payment Gateway Problem for Non-US Founders</h2>
  <p>If you live outside of a supported Tier-1 country, relying on local payment gateways for global e-commerce can completely destroy your business margins. Local payment processors often have low conversion rates, high decline rates from international cards, and severely limit what platforms you can use.</p>
  
  <h2>Why an LLC Solves the Shopify Paradox</h2>
  <p>Shopify actively geo-restricts <strong>Shopify Payments</strong>. If you use a third-party gateway (like a local provider in your unsupported country), Shopify completely punishes you by charging an additional 0.5% to 2.0% transaction fee just for using their platform.</p>
  <div class="alert">
    <strong>The Solution:</strong> Forming a US LLC grants you a US Federal Tax ID (EIN). With an EIN and a US Business Bank Account, you can instantly register for standard Shopify Payments. You entirely bypass the 2% non-native transaction penalty.
  </div>
  
  <h2>Unlocking Stripe with Confidence</h2>
  <p>Stripe is notorious for aggressively verifying offshore businesses or completely shutting down accounts that trigger risk algorithms in unsupported territories. Having a fully registered US LLC with a pristine formation record completely changes your risk profile.</p>
  <ul>
    <li><strong>Higher Approval Rates:</strong> Processing directly through a legitimate US entity puts you in the safest merchant category.</li>
    <li><strong>No Payout Holds:</strong> Since you link Stripe to an actual Tier-1 US Bank Account (like Mercury or Relay), your funds secure rapidly.</li>
    <li><strong>Stripe Capital Access:</strong> US entities natively qualify for internal algorithmic loans and working capital based directly on processing volume.</li>
  </ul>
  
  <h2>Stopping the Bleed on Currency Conversion (FX)</h2>
  <p>When you sell globally, your customers pay in USD. If you use a non-US gateway, that USD is converted to your local currency at a poor exchange rate. When you need to pay suppliers (often in USD again), you convert back from your local currency—losing 3-6% of your total revenue on invisible FX fees alone.</p>
  <p>Your LLC fixes this instantly. You collect USD via Stripe, the payout goes directly to your US Business Bank Account via ACH (staying in USD), and you wire payouts to your global suppliers in USD. Zero conversion loss.</p>
  
  <div style="margin-top:48px;text-align:center;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0;margin-bottom:12px;">Get Your US Payment Infrastructure</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:24px;">Start your US LLC natively with us. We secure your EIN and guarantee banking connections so you can launch Stripe & Shopify fast.</p>
    <a class="btn-green" href="/index.html#pricing" style="display:inline-flex;padding:16px 32px;">Start Your Setup Today &rarr;</a>
  </div>
</section>
"""
page4 = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>US LLC For Stripe & Shopify | Smart Biz Owner</title>') + stripe_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /stripe-shopify.html", "w", encoding="utf-8") as f:
    f.write(page4)

print("Generated 4 sub-pages successfully")
