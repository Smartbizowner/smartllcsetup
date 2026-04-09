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

itin_article = """  <h2>Required Documents and Information</h2>
  <ul>
    <li>LLC Documents</li>
    <li>EIN Letter - 147-C</li>
    <li>High Quality Scanned Passport - Via Xerox shop or Adobe Scan</li>
    <li>Proof of ownership certificate - If multi-member company</li>
    <li>Home address (completed with Zip code) - Same on the documents and passport</li>
    <li>Phone number - Preferrable US number to receive calls from the IRS</li>
  </ul>
  
  <div class="alert">
    <strong>Important note:</strong><br>
    - ITIN Application Product is only for having a US company as owner or shareholder as a Non-U.S. citizen.<br>
    - Once you order your ITIN, our information request form will be sent to you to fill out to process your order.
  </div>

  <h2>Steps to Apply</h2>
  <ol>
    <li>Payment</li>
    <li>Filling the information request form</li>
    <li>Online passport verification</li>
    <li>We will prepare your application form</li>
    <li>You will sign the form that we will prepare, and send back to us via e-mail</li>
    <li>We will submit your signed application form and documents to the IRS</li>
    <li>We will notify you after your result is received</li>
  </ol>

  <h2>Time Required to process ITIN</h2>
  <p>ITIN processing time depends on IRS processing time exactly. ITIN currently takes 12-14 weeks. This information varies on IRS processing time.</p>

  <h2>Unlock US PayPal with ITIN</h2>
  <p>If you are planning to operate a US PayPal business account, an ITIN is <strong>mandatory</strong>. US PayPal will not operate and will hold your funds without it. Creating a <a href="/us-paypal.html" style="color:var(--blue);text-decoration:underline;font-weight:600;">US PayPal Setup</a> allows you to collect payments completely remotely, but the first step is securing your ITIN with us.</p>

  <div style="margin-top:48px;display:flex;align-items:flex-start;gap:20px;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <div style="flex-shrink:0;width:48px;height:48px;background:var(--gray-50);border-radius:50%;display:flex;align-items:center;justify-content:center;">
       <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--gray-500)"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
    </div>
    <div>
      <h3 style="margin-top:0;margin-bottom:8px;">ITIN Application Service &mdash; $450</h3>
      <p style="font-size:15px;color:var(--gray-600);margin-bottom:20px;">Having an ITIN will allow you easier banking and payment processing options, and even enable credit card applications. Included is end-to-end assistance with ITIN application, document preparation, and IRS submission for non-residents. All remote.</p>
      <a class="btn-green" href="https://buy.stripe.com/3cs02Sef6eSi0ta4gD" target="_blank" rel="noopener" style="display:inline-flex;padding:14px 28px;">Purchase ITIN Service &rarr;</a>
    </div>
  </div>"""

paypal_article = """  <div class="alert" style="display:flex;align-items:flex-start;gap:16px;">
    <div style="flex-shrink:0;margin-top:2px;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--gray-500)"><path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path></svg>
    </div>
    <div>
      <strong style="font-size:16px;display:block;margin-bottom:8px;">Things Needed For US PayPal:</strong>
      <ul style="margin-bottom:0;">
        <li>US Company + EIN</li>
        <li>ITIN of LLC owner</li>
        <li>US Phone Number</li>
        <li>Working US Address</li>
        <li>Working Website and Fully compliant with PayPal Policies</li>
      </ul>
    </div>
  </div>
  
  <p style="margin-top:32px;">Setting up a US PayPal account as a non-resident requires precise setup to ensure you remain fully compliant and avoid unexpected fund holds. The single most important requirement is an ITIN number. <a href="/itin.html" style="color:var(--blue);text-decoration:underline;font-weight:600;">Apply for your ITIN here</a> if you don't have one yet.</p>

  <h2>Questions &amp; Answers:</h2>
  
  <div style="margin-bottom:24px;">
    <h3 style="font-size:17px;margin-bottom:6px;color:#111;">Q. What to enter when PayPal asks for SSN?</h3>
    <p style="margin-bottom:0;">A. You need to enter the ITIN of the LLC owner.</p>
  </div>
  
  <div style="margin-bottom:24px;">
    <h3 style="font-size:17px;margin-bottom:6px;color:#111;">Q. Should I sign up for business PayPal account or personal?</h3>
    <p style="margin-bottom:0;">A. For the US, your LLC is the main entity and representative, so you should only open a Business PayPal account.</p>
  </div>
  
  <div style="margin-bottom:24px;">
    <h3 style="font-size:17px;margin-bottom:6px;color:#111;">Q. I do not have an ITIN number right now. Can I still open it?</h3>
    <p style="margin-bottom:0;">A. ITIN is mandatory to open a US PayPal account. If you want to apply for an ITIN, <a href="/itin.html" style="color:var(--blue);text-decoration:underline;">contact our team or purchase our ITIN package</a>.</p>
  </div>
  
  <div style="margin-bottom:24px;">
    <h3 style="font-size:17px;margin-bottom:6px;color:#111;">Q. How long does an ITIN number take if I apply through Smartbizowner?</h3>
    <p style="margin-bottom:0;">A. We have the most expedited timeline of ITIN delivery: 7-9 weeks (IRS processing time applies). Other companies take anywhere from 6-8 months.</p>
  </div>
  
  <div style="margin-bottom:24px;">
    <h3 style="font-size:17px;margin-bottom:6px;color:#111;">Q. What exactly is an ITIN?</h3>
    <p style="margin-bottom:0;">A. An Individual Taxpayer Identification Number is a United States tax processing number issued by the Internal Revenue Service. For non-residents, it acts as an equivalent to an SSN.</p>
  </div>
  
  <div style="margin-bottom:24px;">
    <h3 style="font-size:17px;margin-bottom:6px;color:#111;">Q. I am not receiving the OTP sent by PayPal. What do I do?</h3>
    <p style="margin-bottom:0;">A. Many online phone number providers' VOIP numbers are not acceptable by US PayPal. Try to test multiple companies, or best, use a physical SIM/eSIM phone number for the US.</p>
  </div>
  
  <div style="margin-bottom:24px;">
    <h3 style="font-size:17px;margin-bottom:6px;color:#111;">Q. Can I use my relative's phone number living in the USA?</h3>
    <p style="margin-bottom:0;">A. Yes, you can use a relative's phone number. Just make sure to turn on the authenticator app method so in the future you don't have to ask them for an OTP every time you log into your PayPal.</p>
  </div>
  
  <div style="margin-bottom:24px;">
    <h3 style="font-size:17px;margin-bottom:6px;color:#111;">Q. What if PayPal puts a hold on my funds?</h3>
    <p style="margin-bottom:0;">A. It is possible that PayPal may temporarily hold funds to verify your business. To solve the issue, simply submit the relevant LLC information and ITIN as laid down in the email sent by PayPal to swiftly restore your account.</p>
  </div>
  
  <div style="margin-top:48px;text-align:center;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0;margin-bottom:12px;">Need your ITIN for PayPal First?</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:24px;">Get end-to-end assistance with document preparation and IRS submission.</p>
    <a class="btn-green" href="/itin.html" style="display:inline-flex;padding:14px 28px;">Go to ITIN Application &rarr;</a>
  </div>"""

create_page('itin.html', 'ITIN Application', 'IRS Compliance', 'ITIN Application for Non-US Residents', 'An ITIN is required to secure US PayPal, access US credit cards, and simplify taxes. Get it done securely and reliably.', itin_article)

create_page('us-paypal.html', 'US PayPal Setup', 'Payment Gateways', 'US PayPal Setup for Non-Residents', 'Operate a legitimate US PayPal business account to accept global payments and run your e-commerce store with zero geo-restrictions.', paypal_article)
