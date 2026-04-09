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
.article-wrap .warn { background:#eff6ff; border-left:4px solid var(--blue); padding:16px 24px; margin:24px 0; border-radius:4px; }
.article-wrap .warn strong { color:#111; }
.article-wrap table { width:100%; border-collapse:collapse; margin:24px 0; font-size:15px; }
.article-wrap table th { background:var(--gray-50); text-align:left; padding:12px 16px; border:1px solid var(--border); font-weight:700; color:#111; }
.article-wrap table td { padding:12px 16px; border:1px solid var(--border); color:var(--gray-700); }
.article-wrap .pricing-card { background:#fff; border:1px solid var(--border); border-radius:var(--r); padding:32px; margin:32px 0; box-shadow:0 8px 24px rgba(0,0,0,0.04); }
.article-wrap .pricing-card .price { font-size:42px; font-weight:800; color:var(--blue); letter-spacing:-0.02em; }
.article-wrap .pricing-card .price-sub { font-size:14px; color:var(--gray-500); margin-bottom:16px; }
.contact-form { max-width:640px; margin:40px auto 0; background:#fff; padding:32px; border:1px solid var(--border); border-radius:var(--r); box-shadow:0 8px 24px rgba(0,0,0,0.04); }
.contact-form .form-row { margin-bottom:20px; }
.contact-form label { display:block; font-size:14px; font-weight:700; color:#111; margin-bottom:8px; }
.contact-form input, .contact-form select, .contact-form textarea { width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:8px; font-size:15px; font-family:'Inter',sans-serif; color:#111; background:#fff; transition:border-color .18s; }
.contact-form input:focus, .contact-form select:focus, .contact-form textarea:focus { outline:none; border-color:var(--blue); }
.contact-form textarea { resize:vertical; min-height:120px; }
.contact-form .form-submit { width:100%; background:var(--green); color:#fff; font-size:16px; font-weight:700; font-family:'Inter',sans-serif; padding:15px 28px; border-radius:50px; border:none; cursor:pointer; transition:background .18s; box-shadow:0 2px 12px rgba(22,163,74,.2); display:flex; align-items:center; justify-content:center; gap:8px; }
.contact-form .form-submit:hover { background:var(--green-d); }
.contact-form .form-submit svg { width:18px; height:18px; fill:#fff; }
.contact-form .form-note { font-size:12px; color:var(--gray-500); text-align:center; margin-top:14px; }
</style>
"""
head_nav = head_nav.replace('</head>', custom_css + '\n</head>')

# Extract footer
footer_split = html.split('<!-- FOOTER -->', 1)
footer = '<!-- FOOTER -->' + footer_split[1]


# ============================================================
# 1. ANNUAL RENEWAL
# ============================================================
annual_renewal_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">LLC Management</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">LLC Annual Renewal &amp; Annual Reports</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Keep your US LLC in good standing. Annual report filing, registered agent renewal, state fee payments — handled for you end to end.</p>
  </div>
</section>

<section class="article-wrap">
  <h2>What Is an Annual Report?</h2>
  <p>An annual report is an administrative filing that keeps your state records current. It typically confirms your registered agent, business address, and member/manager information. Despite the name, some states require these filings every two years rather than yearly.</p>
  <p>Annual reports are <strong>not tax returns</strong>. They are compliance documents that confirm your business still exists and the state's records are up to date. Filing your annual report is separate from filing your federal tax return with the IRS.</p>

  <div class="alert">
    <strong>Important:</strong> Every US LLC must complete its annual renewal on time. Missing this deadline can result in late fees, loss of good standing, or eventual administrative dissolution of your company.
  </div>

  <h2>State-by-State Requirements</h2>
  <p>Each state has its own due dates, frequency, and fees. Here are the most common states we help form LLCs in:</p>

  <table>
    <thead>
      <tr><th>State</th><th>Frequency</th><th>Due Date</th><th>State Fee</th></tr>
    </thead>
    <tbody>
      <tr><td>Wyoming</td><td>Annual</td><td>Anniversary month</td><td>$60 minimum ($135 typical)</td></tr>
      <tr><td>Delaware</td><td>Annual</td><td>June 1</td><td>$300 franchise tax</td></tr>
      <tr><td>New Mexico</td><td>Not required</td><td>N/A</td><td>$0 (only agent)</td></tr>
      <tr><td>Florida</td><td>Annual</td><td>May 1</td><td>$138.75</td></tr>
      <tr><td>Texas</td><td>Annual (franchise)</td><td>May 15</td><td>$0 (under $2.47M)</td></tr>
      <tr><td>Colorado</td><td>Annual (periodic)</td><td>Anniversary month</td><td>$10</td></tr>
    </tbody>
  </table>

  <h2>The Filing Process</h2>
  <ol>
    <li><strong>Reminder notification:</strong> Most states send a reminder 60-90 days before the deadline to your registered agent.</li>
    <li><strong>Access the state portal:</strong> Each state has its own online filing system.</li>
    <li><strong>Verify or update your details:</strong> Confirm the business address, registered agent, and member/manager information.</li>
    <li><strong>Submit payment:</strong> Pay the state fee via credit card or bank transfer.</li>
    <li><strong>Save your confirmation:</strong> Keep proof of filing for your records.</li>
  </ol>

  <h2>What Happens If You Miss the Deadline?</h2>
  <p>Missing your annual renewal can be expensive and damaging to your business:</p>
  <ul>
    <li><strong>Late fees:</strong> States typically charge $25-$200+ depending on location and how overdue you are.</li>
    <li><strong>Loss of good standing:</strong> Your LLC's status is compromised. This affects your ability to open bank accounts, obtain loans, register in other states, execute contracts, or pursue litigation.</li>
    <li><strong>Administrative dissolution:</strong> After 1-2 years of continued non-compliance, the state may dissolve your LLC — eliminating your liability protection entirely.</li>
    <li><strong>Stripe / Shopify flags:</strong> A dissolved LLC can trigger account freezes on payment processors.</li>
  </ul>

  <div class="warn">
    <strong>Heads up:</strong> Once your LLC is administratively dissolved, reinstating it is expensive and time-consuming — sometimes costing hundreds of dollars in back fees plus reinstatement charges.
  </div>

  <h2>Our Annual Renewal Service</h2>
  <p>We manage the full annual renewal process for you so you never miss a deadline or let your LLC fall out of good standing. For Wyoming LLCs — our most popular state — annual maintenance looks like this:</p>

  <div class="pricing-card">
    <div class="price">$160<span style="font-size:18px;color:var(--gray-500);font-weight:600;">/year</span></div>
    <div class="price-sub">Wyoming LLC annual maintenance</div>
    <ul style="padding-left:20px;">
      <li><strong>$135</strong> — Wyoming state annual report fee</li>
      <li><strong>$25</strong> — Registered agent renewal (required by law)</li>
    </ul>
    <p style="font-size:14px;color:var(--gray-500);margin-top:16px;margin-bottom:0;">Remember: Annual report filing does not cover your IRS tax filing. Form 5472 + Pro Forma 1120 is a separate requirement for foreign-owned LLCs.</p>
  </div>

  <h3>What's Included</h3>
  <ul>
    <li>Deadline tracking &amp; reminders before your renewal date</li>
    <li>Preparation and filing of your annual report with the state</li>
    <li>Payment of state filing fees</li>
    <li>Registered agent renewal for the next year</li>
    <li>Confirmation &amp; filing receipts sent to you</li>
  </ul>

  <div style="margin-top:48px;text-align:center;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0;margin-bottom:12px;">Don't let your LLC fall out of good standing</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:24px;">Message us on WhatsApp and we'll handle your annual renewal before the deadline.</p>
    <a class="btn-green" href="https://wa.me/917566631566" target="_blank" rel="noopener" style="display:inline-flex;padding:16px 32px;">Renew My LLC Now &rarr;</a>
  </div>
</section>
"""
page_ar = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>LLC Annual Renewal | Smart LLC Setup</title>') + annual_renewal_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /annual-renewal.html", "w", encoding="utf-8") as f:
    f.write(page_ar)


# ============================================================
# 2. IRS RETURN FILING
# ============================================================
irs_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">LLC Management</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">IRS Federal Tax Filing: Form 5472 &amp; Pro Forma 1120</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Foreign-owned US LLCs must file Form 5472 + Pro Forma 1120 every year — even with zero revenue. We handle the entire filing for you through our experienced CPA.</p>
  </div>
</section>

<section class="article-wrap">
  <div class="warn">
    <strong>Heads up — it's tax filing season.</strong> Your US LLC must file with the IRS by the deadline. As a foreign-owned US LLC, you're required to submit Form 5472 + Pro Forma 1120 every year. This applies even if your company had zero revenue. Not filing triggers a <strong>$25,000 penalty</strong> directly from the IRS.
  </div>

  <h2>Who Must File Form 5472?</h2>
  <p>Every Single-Member US LLC with a foreign owner is classified by the IRS as a "Disregarded Entity" (DE). Under IRS rules, every foreign-owned DE must file Form 5472 together with a Pro Forma Form 1120 every single year, regardless of whether your LLC had any income, transactions, or activity.</p>

  <p>This applies to you if:</p>
  <ul>
    <li>You are a non-US resident who owns 25% or more of a US LLC</li>
    <li>Your LLC is a single-member LLC with a foreign owner</li>
    <li>Your LLC had any "reportable transactions" during the year (including formation, capital contributions, or payments to you)</li>
    <li>Your LLC had zero revenue — you STILL must file</li>
  </ul>

  <h2>The $25,000 Penalty</h2>
  <p>The IRS is unforgiving about Form 5472. The penalty for failing to file — or filing late, or filing incomplete information — is <strong>$25,000 per failure, per year</strong>. This is not a percentage of owed tax. It's a flat penalty that applies even when your tax liability is $0.</p>

  <div class="alert">
    <strong>Good news:</strong> For most non-US founders with no physical presence in the United States (the "Not ETBUS" rule), your actual US tax liability is $0. The filing itself is purely informational. But the filing is mandatory — and that's where we come in.
  </div>

  <h2>Filing Deadline</h2>
  <p>Form 5472 + Pro Forma 1120 is due by <strong>April 15</strong> each year for the previous tax year. If your LLC operates on a calendar year (which most do), that's the hard deadline.</p>
  <p>An automatic 6-month extension is available by filing Form 7004 — pushing the deadline to October 15. We can file this extension for you as part of our service.</p>

  <h2>Our Federal Tax Filing Service</h2>
  <p>We handle the entire filing for you — fully managed, no stress. Our experienced CPA prepares and files your Form 5472 and Pro Forma 1120 directly with the IRS so you stay compliant and avoid penalties.</p>

  <div class="pricing-card">
    <div class="price">$170<span style="font-size:18px;color:var(--gray-500);font-weight:600;">/year</span></div>
    <div class="price-sub">Form 5472 + Pro Forma 1120 filing</div>
    <ul style="padding-left:20px;">
      <li>Prepared and filed by our experienced CPA</li>
      <li>Covers both Form 5472 and the required Pro Forma 1120</li>
      <li>Extension filing (Form 7004) included if needed</li>
      <li>Direct IRS submission with confirmation</li>
      <li>Support and answers on your tax position</li>
    </ul>
  </div>

  <h2>What We Need From You</h2>
  <p>To proceed with your IRS federal filing, we need the following information from your side:</p>
  <ol>
    <li><strong>Passport</strong> — a copy of the main page</li>
    <li><strong>Country of tax residence</strong></li>
    <li><strong>Percentage of ownership</strong> in the LLC</li>
    <li><strong>Primary revenue sources</strong> (dropshipping, SaaS, freelance, agency, etc.)</li>
    <li><strong>Payment processors used</strong> (Stripe, PayPal, Shopify Payments, Wise, etc.)</li>
    <li><strong>Approximate breakdown by platform</strong> if you sell across multiple channels</li>
    <li><strong>Bank statement of the last year</strong> for the LLC's business account</li>
  </ol>

  <h2>Why Not File It Yourself?</h2>
  <p>Form 5472 and Pro Forma 1120 are not forms you can file on common DIY tax software like TurboTax. They must be paper-filed or e-filed through an authorized IRS provider. The instructions are dense, and a single mistake — wrong EIN placement, missed transaction, incomplete disclosure — can trigger the $25,000 penalty.</p>
  <p>Our CPA has filed these forms for hundreds of non-US founders. We know exactly what the IRS expects.</p>

  <h2>Common Questions</h2>

  <h3>My LLC had no income. Do I still need to file?</h3>
  <p>Yes. Form 5472 is required even if your LLC had zero revenue, zero transactions, and zero activity. The formation itself counts as a reportable transaction.</p>

  <h3>Will I owe US taxes?</h3>
  <p>For most non-US residents with no physical presence in the US (no US office, employees, or dependent agents), the answer is no — thanks to the "Not Engaged in Trade or Business in the US" (Not ETBUS) rule. The filing is purely informational.</p>

  <h3>What if I've already missed past years?</h3>
  <p>You can still come into compliance through late filing. Penalties may apply, but we can help you catch up and submit a reasonable cause statement. Message us on WhatsApp to discuss your situation.</p>

  <div style="margin-top:48px;text-align:center;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0;margin-bottom:12px;">Let's get you compliant before the deadline</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:24px;">Message us on WhatsApp with your details and we'll handle the filing end to end. $170, one-time per year.</p>
    <a class="btn-green" href="https://wa.me/917566631566" target="_blank" rel="noopener" style="display:inline-flex;padding:16px 32px;">Start My IRS Filing &rarr;</a>
  </div>
</section>
"""
page_irs = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>IRS Federal Tax Filing (Form 5472 + 1120) | Smart LLC Setup</title>') + irs_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /irs-return-filing.html", "w", encoding="utf-8") as f:
    f.write(page_irs)


# ============================================================
# 3. MAINTAIN YOUR LLC
# ============================================================
maintain_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">LLC Guide</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">How to Maintain Your LLC and Keep It Alive</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Forming your LLC is just the beginning. Here's how to keep your company in good standing, protect your liability shield, and stay compliant year after year.</p>
  </div>
</section>

<section class="article-wrap">
  <h2>Why Maintenance Matters</h2>
  <p>The liability shield your LLC provides isn't automatic. Courts can "pierce the corporate veil" if you fail to maintain proper separation between yourself and your business. Done right, ongoing maintenance gives you:</p>
  <ul>
    <li><strong>Asset protection</strong> from business debts and lawsuits</li>
    <li><strong>Good standing</strong> with state regulators</li>
    <li><strong>Preserved business opportunities</strong> for contracts, partnerships, and payment processors</li>
    <li><strong>Cleaner tax records</strong> and accounting</li>
    <li><strong>Enhanced credibility</strong> with clients, suppliers, and banks</li>
  </ul>

  <h2>Separating Personal and Business Finances</h2>
  <p>This is the single most important maintenance task. Mixing personal and business money is the #1 reason courts disregard LLC protection.</p>

  <h3>Open a Dedicated Business Bank Account</h3>
  <p>All business income and expenses should flow through a separate account — never commingle with personal transactions. Use Relay, Mercury, Wise, or Payoneer if you're a non-US founder.</p>

  <h3>Get a Business Credit or Debit Card</h3>
  <p>Use a card exclusively for business purchases. This creates a clean audit trail that holds up under scrutiny.</p>

  <h3>Pay Yourself Properly</h3>
  <p>Don't withdraw money ad hoc. Document distributions in your records and follow your Operating Agreement guidelines.</p>

  <div class="warn">
    <strong>Avoid at all costs:</strong> Paying personal bills from business accounts, depositing business income into personal accounts, using business funds for personal expenses, or letting family members access the business account.
  </div>

  <h2>Record Keeping Requirements</h2>
  <p>Maintain these documents organized and accessible for at least <strong>seven years</strong>:</p>

  <h3>Formation Documents</h3>
  <ul>
    <li>Articles of Organization</li>
    <li>Operating Agreement</li>
    <li>EIN confirmation letter (IRS CP 575)</li>
    <li>State certificates and filing receipts</li>
  </ul>

  <h3>Meeting &amp; Decision Records</h3>
  <ul>
    <li>Meeting minutes (yes, even single-member LLCs should keep these)</li>
    <li>Resolutions for major decisions</li>
    <li>Member and manager voting records</li>
  </ul>

  <h3>Financial Records</h3>
  <ul>
    <li>Bank statements</li>
    <li>Tax returns (Form 5472 + 1120 copies)</li>
    <li>Receipts and invoices</li>
    <li>Contracts and agreements</li>
  </ul>

  <h3>Compliance Records</h3>
  <ul>
    <li>Annual report filings</li>
    <li>Business license copies</li>
    <li>Registered agent correspondence</li>
    <li>State communications</li>
  </ul>

  <h2>Annual Compliance Checklist</h2>
  <p>Every year, a foreign-owned US LLC needs to complete the following:</p>
  <ol>
    <li><strong>File your state annual report</strong> (e.g. Wyoming — due in your anniversary month)</li>
    <li><strong>Renew your registered agent</strong> (required by law in every state)</li>
    <li><strong>File Form 5472 + Pro Forma 1120</strong> with the IRS by April 15 — even with zero revenue</li>
    <li><strong>Reconcile your books</strong> and keep clean records of all transactions</li>
    <li><strong>Verify state records</strong> — make sure your address, agent, and member info are still accurate</li>
  </ol>

  <div class="alert">
    <strong>Simple math for Wyoming LLCs:</strong> $160/year state + agent renewal + $170/year IRS filing = <strong>$330 total annual compliance cost</strong>. That's the full cost of keeping your US LLC alive and in good standing.
  </div>

  <h2>Protecting the Corporate Veil</h2>
  <p>Courts examine these factors when deciding whether to pierce your LLC's liability protection:</p>

  <h3>Financial Separation</h3>
  <p>Distinct bank accounts, financial records, and clear documentation of transactions between you and the LLC.</p>

  <h3>Following Formalities</h3>
  <p>An Operating Agreement exists, major decisions are authorized properly, and state compliance requirements are met on time.</p>

  <h3>Adequate Capitalization</h3>
  <p>The business should have sufficient funds for foreseeable obligations. Don't strip all assets out the moment they arrive.</p>

  <h3>Avoiding Fraud</h3>
  <p>Don't use the LLC to defraud creditors, misrepresent dealings, or intentionally undercapitalize to evade debts.</p>

  <h2>Common Mistakes to Avoid</h2>
  <ul>
    <li>Mixing personal and business finances (the #1 liability risk)</li>
    <li>Operating without a signed Operating Agreement</li>
    <li>Missing annual report deadlines</li>
    <li>Ignoring registered agent notices</li>
    <li>Skipping Form 5472 filing because the LLC "had no revenue"</li>
    <li>Failing to update member information after changes</li>
    <li>Not documenting major business decisions in writing</li>
    <li>Operating in other US states without proper registration</li>
  </ul>

  <h2>Frequently Asked Questions</h2>

  <h3>What is "piercing the corporate veil"?</h3>
  <p>When a court ignores your LLC's liability protection and holds you personally responsible for business debts. This usually happens when you fail to keep the LLC separate from yourself.</p>

  <h3>How do I keep finances separate?</h3>
  <p>Open a dedicated business bank account, pay yourself documented distributions rather than informal withdrawals, maintain separate business and personal cards, and document all transactions between you and the LLC.</p>

  <h3>What records must I keep?</h3>
  <p>Formation documents, meeting minutes and resolutions, financial statements, tax returns, contracts, and state correspondence. Retain all records for a minimum of seven years.</p>

  <h3>How much does it cost to keep a Wyoming LLC alive each year?</h3>
  <p>$160 for state + registered agent renewal, plus $170 for IRS Form 5472 + 1120 filing. Total: $330/year for full compliance.</p>

  <div style="margin-top:48px;text-align:center;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0;margin-bottom:12px;">Let us handle the maintenance for you</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:24px;">Annual renewal, IRS filing, registered agent — we take care of all of it so your LLC stays healthy.</p>
    <a class="btn-green" href="https://wa.me/917566631566" target="_blank" rel="noopener" style="display:inline-flex;padding:16px 32px;">Talk to Us on WhatsApp &rarr;</a>
  </div>
</section>
"""
page_maintain = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>How to Maintain Your LLC and Keep It Alive | Smart LLC Setup</title>') + maintain_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /maintain-llc.html", "w", encoding="utf-8") as f:
    f.write(page_maintain)


# ============================================================
# 4. PRIVACY POLICY
# ============================================================
privacy_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">Legal</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">Privacy Policy</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">How Smart LLC Setup collects, uses, and protects your personal information.</p>
  </div>
</section>

<section class="article-wrap">
  <p style="color:var(--gray-500);font-size:14px;">Last updated: April 9, 2026</p>

  <p>This Privacy Policy describes how Smart LLC Setup (operated by Mayank Malik, doing business as Smart Biz Owner) ("we", "us", "our") collects, uses, and discloses your Personal Information when you visit our website, contact us, or purchase our LLC formation and management services.</p>

  <h2>Collecting Personal Information</h2>
  <p>When you visit or interact with our Site, we collect certain information about your device, your interaction with the Site, and information necessary to deliver our services. We refer to any information that can uniquely identify an individual as "Personal Information."</p>

  <h3>Device Information</h3>
  <ul>
    <li><strong>Examples collected:</strong> web browser version, IP address, time zone, cookie data, pages viewed, search terms, and how you interact with the Site.</li>
    <li><strong>Purpose:</strong> to load the Site properly for you and analyze Site usage.</li>
    <li><strong>Source:</strong> collected automatically when you access our Site through cookies, log files, and analytics tags.</li>
  </ul>

  <h3>Contact &amp; Order Information</h3>
  <ul>
    <li><strong>Examples collected:</strong> name, email address, phone number, WhatsApp number, country of residence, passport details (for LLC formation), company preferences, and payment information processed by our third-party payment gateway.</li>
    <li><strong>Purpose:</strong> to provide LLC formation, EIN acquisition, IRS filing, and related services; to process payments; to communicate with you; and to meet our contractual obligations.</li>
    <li><strong>Source:</strong> collected directly from you through WhatsApp, our contact form, or email.</li>
  </ul>

  <h3>Customer Support Information</h3>
  <ul>
    <li><strong>Examples collected:</strong> support messages, questions, and any documents you choose to share with us.</li>
    <li><strong>Purpose:</strong> to provide customer support and answer your questions about US LLC formation and compliance.</li>
    <li><strong>Source:</strong> collected directly from you.</li>
  </ul>

  <h2>Sharing Personal Information</h2>
  <p>We share your Personal Information only with service providers that help us deliver our services, and only to the extent necessary. For example:</p>
  <ul>
    <li>With the <strong>US Secretary of State</strong> of the state where your LLC is formed, to file your Articles of Organization.</li>
    <li>With the <strong>Internal Revenue Service (IRS)</strong>, to obtain your EIN and file Form 5472 + Pro Forma 1120.</li>
    <li>With our <strong>registered agent partners</strong>, to fulfil the mandatory registered agent requirement in your state.</li>
    <li>With our <strong>CPA partners</strong>, who prepare your federal tax filings.</li>
    <li>With our <strong>payment processor</strong>, to process your payment for our services.</li>
    <li>To comply with applicable laws, lawful subpoenas, or government requests, or to protect our rights.</li>
  </ul>
  <p>We do not sell your Personal Information to third parties for marketing purposes.</p>

  <h2>Using Your Personal Information</h2>
  <p>We use your Personal Information to provide our services — including forming your LLC, obtaining your EIN, filing annual reports, handling IRS filings, and communicating with you about your account. We may also send you occasional updates about our services, compliance deadlines, and relevant guidance.</p>

  <h2>Data Retention</h2>
  <p>We retain your Personal Information for as long as needed to provide our services and meet legal, accounting, or reporting requirements. IRS-related records are retained for a minimum of seven years in line with US federal requirements.</p>

  <h2>Cookies</h2>
  <p>Our Site uses cookies and similar technologies to improve your browsing experience, analyze traffic, and remember your preferences. You can disable cookies through your browser settings, but some parts of the Site may not function properly.</p>

  <h2>Your Rights</h2>
  <p>You have the right to access, correct, update, or request deletion of the Personal Information we hold about you. To exercise these rights, please message us on WhatsApp at +91 7566631566. We will respond within a reasonable timeframe.</p>
  <p>If you are a resident of the European Economic Area (EEA), you also have the right to lodge a complaint with your local data protection authority.</p>

  <h2>Data Security</h2>
  <p>We take reasonable precautions to protect your Personal Information. However, no method of transmission over the internet or electronic storage is 100% secure. While we strive to protect your information, we cannot guarantee absolute security.</p>

  <h2>Children</h2>
  <p>Our services are not intended for individuals under the age of 18. We do not knowingly collect Personal Information from children. If you believe a child has provided us with Personal Information, please contact us so we can delete it.</p>

  <h2>Changes to This Privacy Policy</h2>
  <p>We may update this Privacy Policy from time to time to reflect changes in our practices or for legal reasons. The updated version will be posted on this page with a revised "Last updated" date.</p>

  <h2>Contact Us</h2>
  <p>For questions about this Privacy Policy or your Personal Information, contact us:</p>
  <ul>
    <li><strong>Business:</strong> Smart LLC Setup (Smart Biz Owner)</li>
    <li><strong>Owner:</strong> Mayank Malik</li>
    <li><strong>WhatsApp:</strong> <a href="https://wa.me/917566631566" style="color:var(--blue);text-decoration:underline;">+91 7566631566</a></li>
  </ul>
</section>
"""
page_privacy = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>Privacy Policy | Smart LLC Setup</title>') + privacy_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /privacy-policy.html", "w", encoding="utf-8") as f:
    f.write(page_privacy)


# ============================================================
# 5. TERMS OF SERVICE
# ============================================================
terms_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">Legal</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">Terms of Service</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">The terms that govern your use of the Smart LLC Setup website and services.</p>
  </div>
</section>

<section class="article-wrap">
  <p style="color:var(--gray-500);font-size:14px;">Last updated: April 9, 2026</p>

  <h2>Overview</h2>
  <p>This website is operated by Smart LLC Setup (a service of Smart Biz Owner, owned by Mayank Malik). Throughout the site, the terms "we", "us", and "our" refer to Smart LLC Setup. We offer this website and all the information, tools, and services available from it to you, the user, conditioned upon your acceptance of all terms, conditions, policies, and notices stated here.</p>
  <p>By visiting our site, engaging with us on WhatsApp, or purchasing any service from us, you engage in our "Service" and agree to be bound by the following Terms of Service, including any additional terms and policies referenced here or linked from this page.</p>
  <p>Please read these Terms carefully before using our website or services. If you do not agree to all the terms and conditions, you may not access the website or use our services.</p>

  <h2>Section 1 — Online Use</h2>
  <p>By agreeing to these Terms, you represent that you are at least 18 years old and legally capable of entering into a binding agreement in your jurisdiction.</p>
  <p>You may not use our services for any illegal or unauthorized purpose, nor may you violate any laws in your jurisdiction (including tax laws, import/export laws, and financial regulations) while using our Service.</p>
  <p>A breach or violation of any of these Terms will result in immediate termination of your Services.</p>

  <h2>Section 2 — General Conditions</h2>
  <p>We reserve the right to refuse service to anyone for any reason at any time.</p>
  <p>You agree not to reproduce, duplicate, copy, sell, resell, or exploit any portion of our website, content, or services without express written permission from us.</p>
  <p>The headings used in this agreement are included for convenience only and will not limit or otherwise affect these Terms.</p>

  <h2>Section 3 — Accuracy of Information</h2>
  <p>We are not responsible if information made available on this site is not accurate, complete, or current. Material on this site is provided for general information only and should not be relied upon as the sole basis for making business, legal, or tax decisions without consulting qualified professionals.</p>
  <p>Any reliance on the material on this site is at your own risk. We reserve the right to modify the contents of this site at any time, but have no obligation to update any information.</p>

  <h2>Section 4 — Modifications to Services and Pricing</h2>
  <p>Prices for our services are subject to change without notice. We reserve the right at any time to modify or discontinue any service (or any part of it) without notice.</p>
  <p>We shall not be liable to you or to any third party for any modification, price change, suspension, or discontinuance of our Service.</p>

  <h2>Section 5 — Services Provided</h2>
  <p>Smart LLC Setup provides the following services:</p>
  <ul>
    <li>US LLC formation in various states (Wyoming, Delaware, New Mexico, Florida, Texas, Colorado, etc.)</li>
    <li>EIN (Employer Identification Number) application with the IRS</li>
    <li>Registered agent services</li>
    <li>Annual report and state renewal filings</li>
    <li>Federal tax filing assistance (Form 5472 + Pro Forma 1120) via our CPA partners</li>
    <li>Guidance on opening US business bank accounts and connecting to payment processors</li>
  </ul>
  <p>We make every effort to describe our services accurately but do not warrant that service descriptions, pricing, or timelines will always be error-free, or that any errors will be corrected.</p>

  <h2>Section 6 — Not Legal or Tax Advice</h2>
  <p>Smart LLC Setup is not a law firm, and we do not provide legal advice. We are also not a CPA or tax advisory firm — our CPA partners prepare tax filings, but any information we share on the website or via WhatsApp is general guidance only.</p>
  <p>For specific legal or tax advice regarding your situation, we strongly recommend consulting a licensed attorney or certified public accountant in your jurisdiction.</p>

  <h2>Section 7 — Payment and Refunds</h2>
  <p>All fees for our services are payable in advance. Once we begin work on your LLC formation, EIN application, or tax filing, fees are generally non-refundable because the underlying state and IRS fees are paid on your behalf immediately.</p>
  <p>If you have a concern about a charge or service, please contact us on WhatsApp to discuss your specific situation. We handle refund requests on a case-by-case basis.</p>

  <h2>Section 8 — Client Responsibilities</h2>
  <p>You agree to provide current, complete, and accurate information when engaging our services. This includes:</p>
  <ul>
    <li>Valid passport and identification documents</li>
    <li>Accurate company name, address, and ownership details</li>
    <li>Truthful tax residence and ownership percentage disclosures</li>
    <li>Timely responses to our requests for additional documents or information</li>
  </ul>
  <p>You are responsible for maintaining your LLC in good standing after formation — including annual reports, IRS filings, and registered agent renewals — either through us or independently.</p>

  <h2>Section 9 — Third-Party Links and Tools</h2>
  <p>Our Service may include links to third-party websites, tools, or services (such as Stripe, Shopify, Mercury, Relay, etc.). We are not responsible for examining or evaluating the content or accuracy of these third-party services and do not warrant or have any liability for them.</p>
  <p>Any use of third-party tools or services is entirely at your own risk and discretion. Please review the terms and privacy policies of any third party before engaging with them.</p>

  <h2>Section 10 — Limitation of Liability</h2>
  <p>In no event shall Smart LLC Setup, its owner Mayank Malik, or our partners be liable for any indirect, incidental, special, consequential, or punitive damages, including without limitation loss of profits, data, or business, arising out of your use of our services.</p>
  <p>Our total liability to you for any claim arising from or related to these Terms or our services shall not exceed the amount you paid us for the specific service in question.</p>

  <h2>Section 11 — Indemnification</h2>
  <p>You agree to indemnify, defend, and hold harmless Smart LLC Setup and Mayank Malik from any claim or demand, including reasonable attorneys' fees, made by any third party due to your breach of these Terms or your violation of any law or the rights of a third party.</p>

  <h2>Section 12 — Termination</h2>
  <p>These Terms are effective unless and until terminated by either you or us. You may terminate these Terms at any time by notifying us that you no longer wish to use our Services, or when you cease using our Site.</p>
  <p>If in our sole judgment you fail to comply with any term or provision of these Terms, we may also terminate this agreement at any time without notice.</p>

  <h2>Section 13 — Governing Law</h2>
  <p>These Terms of Service and any separate agreements shall be governed by and construed in accordance with the laws applicable to the jurisdiction in which Smart LLC Setup operates.</p>

  <h2>Section 14 — Changes to Terms of Service</h2>
  <p>We reserve the right to update, change, or replace any part of these Terms by posting updates to our website. It is your responsibility to check this page periodically for changes. Your continued use of the website following the posting of any changes constitutes acceptance of those changes.</p>

  <h2>Contact Information</h2>
  <p>Questions about the Terms of Service should be sent to us via WhatsApp:</p>
  <ul>
    <li><strong>Business:</strong> Smart LLC Setup (Smart Biz Owner)</li>
    <li><strong>Owner:</strong> Mayank Malik</li>
    <li><strong>WhatsApp:</strong> <a href="https://wa.me/917566631566" style="color:var(--blue);text-decoration:underline;">+91 7566631566</a></li>
  </ul>
</section>
"""
page_terms = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>Terms of Service | Smart LLC Setup</title>') + terms_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /terms-of-service.html", "w", encoding="utf-8") as f:
    f.write(page_terms)


# ============================================================
# 6. CONTACT FORM
# ============================================================
contact_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">Get in Touch</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">Contact Smart LLC Setup</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Tell us about your business and we'll reply on WhatsApp within a few hours. No call centres, you'll speak with Mayank or the team directly.</p>
  </div>
</section>

<section class="article-wrap">
  <h2>Send Us a Message</h2>
  <p>Fill out the form below and click "Send on WhatsApp". Your message will open directly in WhatsApp with all your details pre-filled so we can respond fast.</p>

  <form class="contact-form" onsubmit="return sendToWhatsApp(event)">
    <div class="form-row">
      <label for="cf-name">Full Name *</label>
      <input type="text" id="cf-name" name="name" required placeholder="e.g. Rahul Sharma">
    </div>

    <div class="form-row">
      <label for="cf-email">Email Address *</label>
      <input type="email" id="cf-email" name="email" required placeholder="you@example.com">
    </div>

    <div class="form-row">
      <label for="cf-country">Country of Residence *</label>
      <input type="text" id="cf-country" name="country" required placeholder="e.g. India">
    </div>

    <div class="form-row">
      <label for="cf-service">What do you need help with? *</label>
      <select id="cf-service" name="service" required>
        <option value="">-- Please select --</option>
        <option value="LLC Formation">LLC Formation (new company)</option>
        <option value="EIN Application">Get an EIN (Tax ID)</option>
        <option value="US Bank Account">US Business Bank Account</option>
        <option value="Stripe / Shopify Setup">Stripe / Shopify Setup</option>
        <option value="Annual Renewal">Annual Renewal</option>
        <option value="IRS Filing (5472 + 1120)">IRS Filing (Form 5472 + 1120)</option>
        <option value="General Question">General Question</option>
      </select>
    </div>

    <div class="form-row">
      <label for="cf-business">Business Type (optional)</label>
      <input type="text" id="cf-business" name="business" placeholder="e.g. Dropshipping, Freelance, Agency, SaaS">
    </div>

    <div class="form-row">
      <label for="cf-message">Your Message *</label>
      <textarea id="cf-message" name="message" required placeholder="Tell us a bit about your situation and what you're trying to achieve..."></textarea>
    </div>

    <button type="submit" class="form-submit">
      <svg viewBox="0 0 24 24"><path d="M20.52 3.48A11.94 11.94 0 0 0 12.06 0C5.48 0 .14 5.33.14 11.91c0 2.1.55 4.15 1.6 5.96L0 24l6.28-1.65a11.88 11.88 0 0 0 5.78 1.47h.01c6.57 0 11.9-5.33 11.9-11.9 0-3.18-1.24-6.17-3.45-8.44zM12.07 21.8h-.01a9.86 9.86 0 0 1-5.03-1.38l-.36-.21-3.73.98 1-3.64-.24-.38a9.86 9.86 0 0 1-1.52-5.26c0-5.46 4.45-9.91 9.9-9.91 2.65 0 5.13 1.03 7 2.9a9.82 9.82 0 0 1 2.9 7c0 5.46-4.44 9.9-9.91 9.9zm5.43-7.42c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15s-.77.97-.94 1.17c-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.05 1.02-1.05 2.5 0 1.47 1.07 2.89 1.22 3.09.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.23 1.35.2 1.86.12.57-.08 1.76-.72 2.01-1.42.25-.7.25-1.3.17-1.42-.07-.12-.27-.2-.57-.35z"/></svg>
      Send on WhatsApp
    </button>
    <p class="form-note">No data is stored on our servers. Clicking "Send" opens WhatsApp with your message pre-filled.</p>
  </form>

  <div style="margin-top:48px;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:var(--gray-50);">
    <h3 style="margin-top:0;margin-bottom:12px;">Prefer direct WhatsApp?</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:16px;">Skip the form and message us directly — we're available 7 days a week.</p>
    <a class="btn-green" href="https://wa.me/917566631566" target="_blank" rel="noopener" style="display:inline-flex;padding:14px 28px;">Chat on WhatsApp &rarr;</a>
  </div>
</section>

<script>
function sendToWhatsApp(e) {
  e.preventDefault();
  var name = document.getElementById('cf-name').value.trim();
  var email = document.getElementById('cf-email').value.trim();
  var country = document.getElementById('cf-country').value.trim();
  var service = document.getElementById('cf-service').value.trim();
  var business = document.getElementById('cf-business').value.trim();
  var message = document.getElementById('cf-message').value.trim();

  var text = '*New Enquiry from Smart LLC Setup Website*' + '\\n\\n';
  text += '*Name:* ' + name + '\\n';
  text += '*Email:* ' + email + '\\n';
  text += '*Country:* ' + country + '\\n';
  text += '*Service:* ' + service + '\\n';
  if (business) text += '*Business Type:* ' + business + '\\n';
  text += '\\n*Message:*\\n' + message;

  var encoded = encodeURIComponent(text);
  var url = 'https://wa.me/917566631566?text=' + encoded;
  window.open(url, '_blank');
  return false;
}
</script>
"""
page_contact = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>Contact Us | Smart LLC Setup</title>') + contact_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /contact.html", "w", encoding="utf-8") as f:
    f.write(page_contact)


# ============================================================
# 7. LLC REINSTATEMENT
# ============================================================
reinstatement_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">LLC Management</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">LLC Reinstatement: Bring Your Dissolved LLC Back to Good Standing</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Missed annual reports? LLC administratively dissolved by the state? We file your back reports, pay the penalties, and get your company reinstated — fully managed for a flat $290 for Wyoming. Other states: pricing on enquiry.</p>
  </div>
</section>

<section class="article-wrap">
  <div class="warn">
    <strong>Don't panic if your LLC was dissolved.</strong> Administrative dissolution is reversible in most states. The faster you act, the simpler and cheaper the reinstatement becomes — waiting too long can turn a fixable problem into a permanent one.
  </div>

  <h2>What Is LLC Reinstatement?</h2>
  <p>Reinstatement is the process of restoring an LLC to good standing after it has been administratively dissolved by the state. When an LLC misses too many compliance deadlines, the state formally dissolves the entity — meaning it "no longer legally exists" on the state's records.</p>
  <p>The good news: most states allow you to reinstate a dissolved LLC by filing all overdue reports, paying back fees and penalties, and submitting a reinstatement application. Once reinstated, your LLC is treated as if it had never lapsed — keeping your original formation date, EIN, and business history intact.</p>

  <h2>Why Does the State Dissolve an LLC?</h2>
  <p>States administratively dissolve LLCs for a handful of reasons, and they're almost always tied to compliance:</p>
  <ul>
    <li><strong>Missed annual reports</strong> — the #1 reason. After 1-2 years of missed filings, the state takes action.</li>
    <li><strong>Unpaid state fees or franchise taxes</strong> — Delaware franchise tax is a common trigger.</li>
    <li><strong>No registered agent on file</strong> — if your agent resigns and you don't appoint a new one, the state can dissolve the LLC.</li>
    <li><strong>Failure to respond to state notices</strong> — if the state sends compliance warnings and gets no response.</li>
  </ul>

  <h2>What Happens If You Don't Reinstate?</h2>
  <p>A dissolved LLC is not just an administrative issue — it has real consequences:</p>
  <ul>
    <li><strong>Loss of liability protection.</strong> If your LLC doesn't legally exist, your personal assets are no longer shielded from business lawsuits or debts.</li>
    <li><strong>Payment processor freezes.</strong> Stripe, PayPal, and Shopify regularly verify business status. A dissolved LLC can trigger an account freeze and held funds.</li>
    <li><strong>Bank account closure.</strong> Your US business bank may freeze or close your account once they learn of the dissolution.</li>
    <li><strong>Inability to do business.</strong> You cannot legally sign contracts, sue, or conduct business under a dissolved entity.</li>
    <li><strong>Name loss.</strong> If you wait too long, someone else can register your LLC's name.</li>
  </ul>

  <h2>The Reinstatement Process</h2>
  <p>Reinstating a dissolved LLC is more than just paying a single fee. Here's what it actually involves:</p>
  <ol>
    <li><strong>Assessment:</strong> We check your LLC's current status with the state and identify exactly what's missing — back reports, unpaid fees, agent issues, etc.</li>
    <li><strong>File all overdue annual reports:</strong> Every year you missed has to be filed retroactively. Most states require these before accepting a reinstatement application.</li>
    <li><strong>Pay back fees and penalties:</strong> State filing fees for each year plus late penalties. These are paid directly to the state on your behalf.</li>
    <li><strong>Submit the reinstatement application:</strong> A formal application to restore your LLC to active status, signed and submitted to the Secretary of State.</li>
    <li><strong>Re-establish registered agent:</strong> If your agent resigned, we appoint a new one to satisfy state requirements.</li>
    <li><strong>Confirmation of reinstatement:</strong> Once the state approves, we send you the official certificate showing your LLC is back in good standing.</li>
  </ol>

  <h2>Our LLC Reinstatement Service</h2>
  <p>We handle the entire reinstatement end-to-end. You provide the information, we do the paperwork and dealing with the state.</p>

  <div class="pricing-card">
    <div class="price">$290<span style="font-size:18px;color:var(--gray-500);font-weight:600;">&nbsp;flat fee</span></div>
    <div class="price-sub">Wyoming LLC reinstatement</div>
    <ul style="padding-left:20px;">
      <li>Status assessment with the Secretary of State</li>
      <li>Preparation and filing of all overdue annual reports</li>
      <li>Handling of back penalties and fee calculations</li>
      <li>Reinstatement application preparation and submission</li>
      <li>Registered agent reappointment (if needed)</li>
      <li>Direct state communication throughout the process</li>
      <li>Official reinstatement confirmation sent to you</li>
    </ul>
    <p style="font-size:14px;color:var(--gray-500);margin-top:16px;margin-bottom:8px;"><strong>Note:</strong> The $290 flat fee covers Wyoming LLC reinstatement. State filing fees, back report fees, and late penalties are separate and paid directly to the state.</p>
    <p style="font-size:14px;color:var(--gray-500);margin-top:0;margin-bottom:20px;"><strong>Other states:</strong> Reinstatement pricing for non-Wyoming LLCs depends on multiple factors — number of missed years, state filing fees, registered agent status, franchise tax balance, and state-specific penalties. <a href="https://wa.me/917566631566" target="_blank" rel="noopener" style="color:var(--blue);text-decoration:underline;">Message us on WhatsApp</a> with your state and we'll calculate a quote for you.</p>
    <a class="btn-green" href="https://buy.stripe.com/9B6dRaeee3FVdu17fY8EM3f" target="_blank" rel="noopener" style="display:inline-flex;padding:16px 32px;">Pay $290 &amp; Start Wyoming Reinstatement &rarr;</a>
  </div>

  <h2>What We Need From You</h2>
  <p>To start the reinstatement process, we'll need:</p>
  <ol>
    <li>Your LLC name and state of formation</li>
    <li>EIN (Tax ID number)</li>
    <li>Current member/owner information</li>
    <li>Any notices you received from the state about the dissolution</li>
    <li>Copy of your passport (for identity verification)</li>
  </ol>

  <h2>How Long Does Reinstatement Take?</h2>
  <p>Processing time depends on the state and the volume of back reports. For most states, reinstatement completes within <strong>2-4 weeks</strong> from the date we submit the paperwork. Wyoming and New Mexico are typically on the faster end; Delaware and California can take longer.</p>

  <h2>Common Questions</h2>

  <h3>Is my EIN still valid after reinstatement?</h3>
  <p>Yes. Your EIN stays with the LLC even through dissolution. Once reinstated, the same EIN continues to work.</p>

  <h3>Do I still owe IRS Form 5472 for the dissolved years?</h3>
  <p>Yes — Form 5472 is required for every year your LLC existed, including the years it was dissolved. We can handle those filings as a separate service at $170/year.</p>

  <h3>What if my LLC has been dissolved for several years?</h3>
  <p>Some states have a time limit on reinstatement (often 2-5 years). If you're past the limit, we may need to form a new LLC with the same name. Message us to assess your specific situation.</p>

  <h3>Will Stripe / Shopify re-enable my account after reinstatement?</h3>
  <p>Usually yes — once you provide proof of good standing, most processors reactivate accounts. We provide you with the reinstatement certificate to submit.</p>

  <div style="margin-top:48px;text-align:center;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0;margin-bottom:12px;">Ready to bring your LLC back to life?</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:24px;">Wyoming LLC? Pay $290 via Stripe and we'll start within 24 hours. Other state? Message us on WhatsApp for a quote.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
      <a class="btn-green" href="https://buy.stripe.com/9B6dRaeee3FVdu17fY8EM3f" target="_blank" rel="noopener" style="display:inline-flex;padding:16px 32px;">Pay $290 (Wyoming) &rarr;</a>
      <a class="btn-outline" href="https://wa.me/917566631566" target="_blank" rel="noopener" style="display:inline-flex;padding:16px 32px;">Get Quote (Other States)</a>
    </div>
  </div>
</section>
"""
page_reinstate = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>LLC Reinstatement Service | Smart LLC Setup</title>') + reinstatement_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /llc-reinstatement.html", "w", encoding="utf-8") as f:
    f.write(page_reinstate)


# ============================================================
# 8. LLC CLOSING / DISSOLUTION
# ============================================================
closing_content = """
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">LLC Management</div>
    <h1 style="font-size:clamp(26px,5vw,42px);font-weight:800;margin-bottom:12px;">Close Your US LLC Properly: Dissolution Done Right</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Winding down your business? We file the Articles of Dissolution, close your company officially with the state, and stop the annual-fee bleeding — for a flat $100.</p>
  </div>
</section>

<section class="article-wrap">
  <h2>Why Formal Dissolution Matters</h2>
  <p>If you're done with your US LLC, you can't simply stop using it and hope it goes away. Unless you formally dissolve the entity, you remain on the hook for:</p>
  <ul>
    <li>Annual state reports and renewal fees (even if you have zero revenue)</li>
    <li>Registered agent fees, every year</li>
    <li>Franchise taxes in states like Delaware and California</li>
    <li>IRS Form 5472 + Pro Forma 1120 filings — with <strong>$25,000 penalties</strong> for missing them</li>
    <li>Compounding late fees and penalties as those obligations pile up</li>
  </ul>

  <div class="warn">
    <strong>Letting it "just die" is expensive.</strong> Without formal dissolution, the obligations keep accruing. You may think the LLC is gone, but the state and the IRS still see it as active — and the bill keeps growing until you clean it up with a reinstatement-then-dissolution process that costs far more than doing it right now.
  </div>

  <h2>When Should You Dissolve?</h2>
  <p>Formal dissolution is the right move if any of the following applies:</p>
  <ul>
    <li>You're no longer using the LLC for any business activity</li>
    <li>You've pivoted to a different entity or country</li>
    <li>The business didn't work out and you want to stop the annual costs</li>
    <li>You're consolidating multiple LLCs into one</li>
    <li>You want to cleanly retire the company name and EIN</li>
  </ul>

  <h2>The Dissolution Process</h2>
  <p>Properly closing an LLC takes more than one filing. Here's what we handle for you:</p>
  <ol>
    <li><strong>Status check:</strong> We verify the LLC is in good standing first (if it's not, we handle reinstatement first — required in most states before dissolution).</li>
    <li><strong>Member authorization:</strong> Prepare the required written consent from members to dissolve the LLC.</li>
    <li><strong>File Articles of Dissolution:</strong> The official document filed with the Secretary of State that ends the LLC's legal existence.</li>
    <li><strong>Cancel registered agent:</strong> Terminate the registered agent appointment to stop future billing.</li>
    <li><strong>Close state accounts:</strong> Handle any final state obligations (franchise tax account closures, etc.).</li>
    <li><strong>Final IRS filing guidance:</strong> Advise on the final Form 5472 + 1120 filing marked "Final" — required in the year of dissolution.</li>
  </ol>

  <h2>Our LLC Closing Service</h2>
  <div class="pricing-card">
    <div class="price">$100<span style="font-size:18px;color:var(--gray-500);font-weight:600;">&nbsp;flat fee</span></div>
    <div class="price-sub">LLC dissolution &amp; closing service</div>
    <ul style="padding-left:20px;">
      <li>Preparation of Articles of Dissolution</li>
      <li>Filing with the Secretary of State</li>
      <li>Member consent documentation</li>
      <li>Registered agent cancellation</li>
      <li>State account closure</li>
      <li>Final filing guidance (Form 5472/1120 final year)</li>
      <li>Official dissolution certificate sent to you</li>
    </ul>
    <p style="font-size:14px;color:var(--gray-500);margin-top:16px;margin-bottom:0;"><strong>Note:</strong> State dissolution filing fees are separate and paid directly to the state. These are typically $0-$100 depending on the state (Wyoming: $60, Delaware: $200, New Mexico: $25).</p>
  </div>

  <h2>What We Need From You</h2>
  <ol>
    <li>Your LLC name and state of formation</li>
    <li>EIN (Tax ID number)</li>
    <li>Current member information</li>
    <li>Confirmation that all US business activity has stopped</li>
    <li>Copy of your passport (for verification)</li>
  </ol>

  <h2>Common Questions</h2>

  <h3>Do I still need to file IRS Form 5472 for my final year?</h3>
  <p>Yes. You must file a final Form 5472 + Pro Forma 1120 marked "Final Return" for the year you dissolve. This is required by the IRS and skipping it can still trigger the $25,000 penalty. We can handle this filing for $170 as a separate service.</p>

  <h3>What about my US bank account?</h3>
  <p>You should close your US business bank account (Relay, Mercury, Wise, etc.) before dissolution. Transfer out any remaining funds and notify the bank that the business is being dissolved. Most banks close the account quickly once notified.</p>

  <h3>Can I reopen the LLC later?</h3>
  <p>Once formally dissolved, the LLC is permanently closed. If you want to do business again later, you'd need to form a brand new LLC — with a new EIN. That's why dissolution should be a clear decision, not a temporary pause.</p>

  <h3>What if I have outstanding contracts or debts?</h3>
  <p>Settle all business obligations before filing dissolution. Most states require you to notify known creditors and resolve claims. We'll walk you through this step as part of our service.</p>

  <h3>How long does dissolution take?</h3>
  <p>Typical timeline is <strong>2-4 weeks</strong> from the date we file, depending on the state's processing speed.</p>

  <h2>Dissolve vs Reinstate — Which Do You Need?</h2>
  <p>If your LLC is currently in good standing and you want to shut it down, you need <strong>dissolution</strong> ($100).</p>
  <p>If your LLC has already been administratively dissolved by the state due to missed filings and you want to revive it, you need <a href="llc-reinstatement.html" style="color:var(--blue);text-decoration:underline;">reinstatement</a> ($290).</p>
  <p>If your LLC was administratively dissolved but you want to close it out completely (not revive it), message us on WhatsApp — we'll assess your specific state and advise whether reinstatement-then-dissolution or a simpler path applies.</p>

  <div style="margin-top:48px;text-align:center;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:#fff;box-shadow:0 8px 24px rgba(0,0,0,0.04);">
    <h3 style="margin-top:0;margin-bottom:12px;">Ready to close your LLC for good?</h3>
    <p style="font-size:15px;color:var(--gray-500);margin-bottom:24px;">Flat $100. We handle the filings, you stop paying annual fees and avoid future IRS penalties. Message us to get started.</p>
    <a class="btn-green" href="https://wa.me/917566631566" target="_blank" rel="noopener" style="display:inline-flex;padding:16px 32px;">Close My LLC Now &rarr;</a>
  </div>
</section>
"""
page_closing = head_nav.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>LLC Closing &amp; Dissolution Service | Smart LLC Setup</title>') + closing_content + footer
with open("/Users/mayankmalik/Documents/SBO WEBSITE /llc-closing.html", "w", encoding="utf-8") as f:
    f.write(page_closing)


print("Generated 8 service pages successfully:")
print("  - annual-renewal.html")
print("  - irs-return-filing.html")
print("  - maintain-llc.html")
print("  - privacy-policy.html")
print("  - terms-of-service.html")
print("  - contact.html")
print("  - llc-reinstatement.html")
print("  - llc-closing.html")
