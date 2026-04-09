import os

base_file = "/Users/mayankmalik/Documents/SBO WEBSITE /index.html"
with open(base_file, "r", encoding="utf-8") as f:
    html = f.read()

# Extract head (up to </nav>)
head_split = html.split('</nav>', 1)
head_nav = head_split[0] + '</nav>\n'

# Add an extra CSS class for comparison tables/cards to the head
custom_css = """
/* ── COMPARISON CARDS ── */
.comp-grid {
  display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:40px;max-width:900px;margin-inline:auto;
}
@media(max-width:768px) {
  .comp-grid { grid-template-columns:1fr; }
}
.state-card {
  background:#fff;border:2px solid var(--border);border-radius:var(--r);padding:40px 32px;
  position:relative;box-shadow:0 12px 32px rgba(0,0,0,.04);
  transition: transform 0.3s, box-shadow 0.3s;
}
.state-card:hover {
  transform: translateY(-4px);
  box-shadow:0 24px 48px rgba(0,0,0,.08);
}
.state-card.winner {
  border-color:var(--blue);
}
.state-badge {
  position:absolute;top:-14px;left:50%;transform:translateX(-50%);
  background:var(--blue);color:#fff;font-size:12px;font-weight:700;padding:6px 16px;border-radius:50px;
  text-transform:uppercase;letter-spacing:1px;
}
.state-name { font-size:32px;font-weight:800;color:#111;margin-bottom:8px;text-align:center;}
.state-price { font-size:42px;font-weight:800;color:var(--blue);text-align:center;line-height:1;}
.state-price span { font-size:16px;color:var(--gray-500);font-weight:500;}
.state-features { margin-top:24px;display:flex;flex-direction:column;gap:16px; }
.sf-row { display:flex;align-items:flex-start;gap:12px;font-size:14px;color:var(--gray-700);line-height:1.5;}
.sf-row svg { width:18px;height:18px;stroke:var(--green);stroke-width:2.5;flex-shrink:0;fill:none;margin-top:1px;}
.sf-row.bad svg { stroke:#e11d48; }

/* ── NEO/GLASS SECTIONS ── */
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
</style>
"""
head_nav = head_nav.replace('</style>', custom_css)

# Extract footer
footer_split = html.split('<!-- FOOTER -->', 1)
footer = '<!-- FOOTER -->' + footer_split[1]

# We need to change the absolute links/CTAs back to main page if needed, or leave them as absolute.
# "href=\"#pricing\"" should become "href=\"//index.html#pricing\""
head_nav = head_nav.replace('href="#pricing"', 'href="/index.html#pricing"')

def make_page(title, meta_desc, h1, sub_hero, state1_data, state2_data, dropshipping_content, tax_content, cta_title):
    page = head_nav + f"""
<!-- HERO -->
<section class="hero" style="background:#f9fafb;padding:80px 20px 60px;">
  <div class="wrap">
    <div class="hero-pill"><span class="hero-pill-dot"></span>State Comparison Guide</div>
    <h1>{h1}</h1>
    <p class="hero-sub" style="max-width:680px;font-size:18px;">{sub_hero}</p>
  </div>
</section>

<!-- COMPARISON CARDS -->
<section>
  <div class="wrap">
    <div class="label center">The Face-off</div>
    <h2 class="center">Filing Fees, Annual Maintenance & Privacy</h2>
    
    <div class="comp-grid">
      <!-- STATE 1 -->
      <div class="state-card {state1_data['winner_class']}">
        {state1_data['badge']}
        <div class="state-name">{state1_data['name']}</div>
        <div class="state-price">${state1_data['annual_fee']} <span>/ year</span></div>
        <p style="text-align:center;font-size:13px;color:var(--gray-500);margin-top:8px;">Annual State Maintenance</p>
        <div class="state-features">
          {state1_data['features']}
        </div>
      </div>
      
      <!-- STATE 2 -->
      <div class="state-card {state2_data['winner_class']}">
        {state2_data['badge']}
        <div class="state-name">{state2_data['name']}</div>
        <div class="state-price">${state2_data['annual_fee']} <span>/ year</span></div>
        <p style="text-align:center;font-size:13px;color:var(--gray-500);margin-top:8px;">Annual State Maintenance</p>
        <div class="state-features">
          {state2_data['features']}
        </div>
      </div>
    </div>
    <p style="text-align:center;font-size:14px;color:var(--gray-500);margin-top:24px;max-width:700px;margin-left:auto;margin-right:auto;line-height:1.6;">
      * Please note: The amounts above are the mandatory state fees. We charge a minimal $170/year filing fee for the IRS return (Forms 1120/5472) on top of the state fee to keep your LLC 100% compliant and provide ongoing support throughout the year.
    </p>
  </div>
</section>

<!-- DROPSHIPPING & FREELANCING -->
<section style="background:var(--gray-50)">
  <div class="wrap">
    <div class="label">Industry Specifics</div>
    <h2>{state1_data['name']} vs {state2_data['name']} for E-Commerce & Freelancers</h2>
    <div class="glass-box" style="margin-top:32px;">
      <p style="font-size:16px;color:var(--gray-700);line-height:1.7;">{dropshipping_content}</p>
    </div>
  </div>
</section>

<!-- TAX LIABILITY FOR NON-US RESIDENTS -->
<section>
  <div class="wrap">
    <div class="label">Taxation</div>
    <h2>Do I have to pay US Taxes? (ETBUS Rules)</h2>
    <p class="sub" style="max-width:800px;margin-top:16px;">This is the most common question we get: "If I choose {state1_data['name']} or {state2_data['name']}, do I pay zero taxes?"</p>
    
    <div class="tax-highlight">
      <h3 style="font-size:18px;color:#111;margin-bottom:8px;">The "No physical presence" Rule (Not ETBUS)</h3>
      <p style="font-size:15px;color:var(--gray-700);line-height:1.6;margin:0;">
        For a non-US resident running an online business (dropshipping, software, freelancing, agency), 
        your LLC is considered a "Disregarded Entity" by the IRS. As long as you have <strong>no physical presence in the US</strong> 
        (no US employees, no physical office, no dependent agents operating in the US), you are classed as <em>Not Engaged in a Trade or Business in the US (No ETBUS)</em>.
        <br><br>
        This means <strong>you owe 0% US Federal Income Tax</strong> on your business profits, regardless of whether you form in {state1_data['name']} or {state2_data['name']}. You only pay the Annual State Maintenance Fees listed above, and file <strong>Forms 1120 and 5472</strong> every year (which we can help you with).
      </p>
    </div>
    <p style="font-size:15px;color:var(--gray-700);line-height:1.7;">{tax_content}</p>
  </div>
</section>

<!-- FINAL CTA -->
<section class="cta-btm" style="background:#fff;">
  <div class="cta-inner" style="max-width:500px;">
    <div class="label">Ready to start?</div>
    <h2>{cta_title}</h2>
    <p class="sub" style="margin-bottom:28px">Form your LLC securely today and start processing global payments in 48 hours.</p>
    <div class="cta-stack">
      <a class="btn-green" href="/index.html#pricing" style="font-size:16px;padding:16px 28px">Go to Checkout &mdash; Pick your state &rarr;</a>
      <a class="btn-outline" href="https://wa.me/917566631566" target="_blank" rel="noopener">Have a question? WhatsApp us</a>
    </div>
  </div>
</section>
""" + footer

    # Fix <title> tag
    page = page.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', f'<title>{title}</title>')
    page = page.replace('content="Open a US LLC in 48 hours from anywhere. Starts from $299. EIN, registered agent, bank guidance — all included. 500+ LLCs delivered since 2021."', f'content="{meta_desc}"')
    
    return page

bad_svg = '<svg viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>'
good_svg = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>'

# 1. WYOMING VS DELAWARE
wy_vs_de = make_page(
    title="Wyoming vs Delaware LLC For Non-US Residents | Smart Biz Owner",
    meta_desc="Comparing Wyoming vs Delaware LLCs for non-US residents. Look at hidden fees, maintenance costs, and dropshipping business structures before paying.",
    h1="Wyoming vs Delaware LLC:<br><span>Which is Best for Non-US Residents?</span>",
    sub_hero="Discover the hidden annual costs, privacy factors, and exact tax implications of opening an LLC in Wyoming versus Delaware if you live outside the USA.",
    state1_data={
        'name': 'Wyoming',
        'annual_fee': '160',
        'winner_class': 'winner',
        'badge': '<div class="state-badge">BEST OVERALL</div>',
        'features': f"""
          <div class="sf-row">{good_svg} <div><strong>Cost Effective</strong><br>Only ~$160/year (State + Agent). Unbeatable for cash-flow businesses.</div></div>
          <div class="sf-row">{good_svg} <div><strong>Absolute Privacy</strong><br>Members and Managers are completely shielded. Your name isn't on public registries.</div></div>
          <div class="sf-row">{good_svg} <div><strong>Zero State Income Tax</strong><br>No corporate or personal income tax on a state level.</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>Not for VC Funding</strong><br>Angel investors prefer Delaware. Not ideal if you're building a massive tech startup.</div></div>
        """
    },
    state2_data={
        'name': 'Delaware',
        'annual_fee': '300',
        'winner_class': '',
        'badge': '',
        'features': f"""
          <div class="sf-row">{good_svg} <div><strong>Investor Friendly</strong><br>The ultimate state for raising Venture Capital and issuing C-Corp shares.</div></div>
          <div class="sf-row">{good_svg} <div><strong>Court of Chancery</strong><br>Highly respected dedicated business court system.</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>Expensive Franchise Tax</strong><br>Minimum $300 annual franchise tax just to keep the entity alive, every single year.</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>More Compliance</strong><br>Complex fee structures based on authorized shares if structured as a corporation later on.</div></div>
        """
    },
    dropshipping_content="For internet-based businesses like dropshippers, Amazon FBA sellers, freelancers, consultants, and course creators, <strong>Wyoming is the clear winner</strong>. E-commerce and service businesses prioritize cash flow and simplicity. Paying Delaware's $300/year Franchise Tax provides zero benefit to a Shopify store owner, whereas Wyoming's low $60 annual fee keeps overhead nearly non-existent while offering top-tier privacy. Delaware is strictly recommended if you are building an aggressive tech startup (SaaS) and plan to pitch to Silicon Valley investors who require a Delaware C-Corp.",
    tax_content="Both Wyoming and Delaware have no state income tax for out-of-state entities, so from a tax perspective on non-US residents operating entirely outside the US, they are identical. The only financial difference is the annual maintenance cost (Wyoming: ~$160 vs Delaware: ~$300).",
    cta_title="Choose your State to Begin"
)

# 2. WYOMING VS NEW MEXICO
wy_vs_nm = make_page(
    title="Wyoming vs New Mexico LLC For Non-US Residents | Smart Biz Owner",
    meta_desc="Wyoming vs New Mexico LLCs. The two best privacy states for non-US residents compared side-by-side. See full costs, 0% taxes, and e-commerce setups.",
    h1="Wyoming vs New Mexico LLC:<br><span>Privacy on a Budget</span>",
    sub_hero="Two states offer the absolute best privacy for non-US residents. But New Mexico charges $0 in annual fees, while Wyoming has a stronger brand. Here's how to choose.",
    state1_data={
        'name': 'New Mexico',
        'annual_fee': '0',
        'winner_class': 'winner',
        'badge': '<div class="state-badge">MOST AFFORDABLE</div>',
        'features': f"""
          <div class="sf-row">{good_svg} <div><strong>Zero Annual Fees</strong><br>New Mexico has no annual report fees and no franchise tax. You only pay for your Registered Agent.</div></div>
          <div class="sf-row">{good_svg} <div><strong>Total Anonymity</strong><br>Like Wyoming, New Mexico DOES NOT require you to list directors or managers in public databases.</div></div>
          <div class="sf-row">{good_svg} <div><strong>Zero State Income Tax</strong><br>No corporate or personal income tax on a state level.</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>Lesser Known</strong><br>Not as famous as Wyoming in the corporate world, slight friction explaining NM occasionally.</div></div>
        """
    },
    state2_data={
        'name': 'Wyoming',
        'annual_fee': '160',
        'winner_class': '',
        'badge': '<div class="state-badge">BEST REPUTATION</div>',
        'features': f"""
          <div class="sf-row">{good_svg} <div><strong>The 'Gold Standard'</strong><br>Considered the best state for small businesses. Recognized globally.</div></div>
          <div class="sf-row">{good_svg} <div><strong>Extremely Strong Asset Protection</strong><br>Long legal history of protecting members from "charging orders".</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>Small Annual Fee</strong><br>A minimal ~$160 annual fee is required every single year to stay compliant.</div></div>
        """
    },
    dropshipping_content="For internet companies testing the waters (dropshipping on a massive budget, digital agencies, consulting), <strong>New Mexico</strong> is a brilliant, sleeper-hit state. Because New Mexico charges $0 for an annual report, your only yearly maintenance cost is renewing your registered agent (usually $49-$99). This makes it the most affordable US LLC in existence. However, if you prefer the established pedigree of a widely recognized business haven and don't mind a small $160/year fee, Wyoming's asset protection laws are unmatched.",
    tax_content="Both states offer the exact same tax haven strategy for non-US residents under the ETBUS classification. Since neither state has a state-level income tax on out-of-state operators, they are functionally identical for your tax bill: $0.",
    cta_title="Setup Your Private LLC Today"
)

# 3. DELAWARE VS FLORIDA
de_vs_fl = make_page(
    title="Delaware vs Florida LLC For Non-US Residents | Smart Biz Owner",
    meta_desc="Delaware vs Florida LLCs. Compare physical presence, LatAm business implications, taxes, fees, and privacy for a non-resident of the USA.",
    h1="Delaware vs Florida LLC:<br><span>Prestige vs Physical Footprint</span>",
    sub_hero="If you want to raise capital, Delaware is the default. If you do business predominantly in Latin America or intend to visit the US, Florida is king. Let's compare.",
    state1_data={
        'name': 'Delaware',
        'annual_fee': '300',
        'winner_class': '',
        'badge': '',
        'features': f"""
          <div class="sf-row">{good_svg} <div><strong>Institutional Respect</strong><br>Accepted globally by every bank, investor, and payment processor without friction.</div></div>
          <div class="sf-row">{good_svg} <div><strong>High Privacy</strong><br>Ownership details remain highly confidential on the public registry.</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>Expensive Taxes</strong><br>The $300 minimum annual franchise tax represents a high ongoing fixed cost.</div></div>
        """
    },
    state2_data={
        'name': 'Florida',
        'annual_fee': '138',
        'winner_class': '',
        'badge': '',
        'features': f"""
          <div class="sf-row">{good_svg} <div><strong>Strategic Location</strong><br>The financial hub for operations connecting the US to Latin America and the Caribbean.</div></div>
          <div class="sf-row">{good_svg} <div><strong>No Personal Income Tax</strong><br>Excellent if you ever plan to immigrate or establish residency in the United States.</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>Zero Privacy</strong><br>Sunbiz.org lists owner names and addresses completely publicly. Absolutely no anonymity.</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>Higher Annual Report Fees</strong><br>Costs roughly $138.75 in state fees every year.</div></div>
        """
    },
    dropshipping_content="For dropshippers and purely remote freelancers, neither of these states is the #1 choice compared to Wyoming (which is vastly cheaper). However, if you run a physical goods business importing through Miami ports, or run an agency heavily entrenched in the South American market, a <strong>Florida LLC</strong> provides a degree of local trust and banking proximity. Beware: Florida strips you of all privacy. Your name will be a public record.",
    tax_content="Florida has a state corporate income tax, but if you have a single-member LLC (disregarded entity) and you are a non-resident with no physical operations in Florida, you still fall under the ETBUS \"not engaged\" rule, making your US tax bill effectively zero.",
    cta_title="Choose the Best State for Your Goals"
)

# 4. TEXAS VS COLORADO
tx_vs_co = make_page(
    title="Texas vs Colorado LLC For Non-US Residents | Smart Biz Owner",
    meta_desc="Texas vs Colorado LLCs for non-US residents. Extremely cheap setups vs premium reputation setups. The definitive guide on maintenance and taxes.",
    h1="Texas vs Colorado LLC:<br><span>Premium Reputation vs Low Cost</span>",
    sub_hero="Texas offers a top-tier business environment with an expensive setup cost, whereas Colorado allows you to set up and maintain a company for pocket change.",
    state1_data={
        'name': 'Texas',
        'annual_fee': '0',
        'winner_class': '',
        'badge': '',
        'features': f"""
          <div class="sf-row">{good_svg} <div><strong>Incredible Reputation</strong><br>Texas is an economic powerhouse. Having a TX address commands massive corporate respect.</div></div>
          <div class="sf-row">{good_svg} <div><strong>Zero Annual Franchise Tax</strong><br>As long as your global revenue is under $2.47 Million, your TX franchise tax is $0.</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>Expensive Initial Setup</strong><br>The state charges a massive $300 filing fee upfront.</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>Filing Complexity</strong><br>You still must file a 'No Tax Due' & Public Information Report annually, making compliance annoying.</div></div>
        """
    },
    state2_data={
        'name': 'Colorado',
        'annual_fee': '10',
        'winner_class': 'winner',
        'badge': '<div class="state-badge">LOWEST LIFETIME COST</div>',
        'features': f"""
          <div class="sf-row">{good_svg} <div><strong>Extremely Cheap Setup</strong><br>Only $50 in initial state filing fees.</div></div>
          <div class="sf-row">{good_svg} <div><strong>$10 Annual Fee</strong><br>The annual periodic report fee to the state of Colorado is literally a ten-dollar bill.</div></div>
          <div class="sf-row bad">{bad_svg} <div><strong>No Privacy</strong><br>Your name and business address are extremely public and searchable in the Colorado database.</div></div>
        """
    },
    dropshipping_content="For internet startups, dropshippers, and course creators, <strong>Colorado is a fantastic alternative to Wyoming</strong> if you don't care about having your name on public records. The $10 annual fee makes the lifetime cost of a Colorado LLC among the cheapest in America. Texas, on the other hand, is generally avoided by remote sole-proprietors simply because the $300 setup fee is brutally expensive, and maintaining the annual reporting requires jumping through unnecessary bureaucratic hoops—despite it eventually costing $0 in actual taxes.",
    tax_content="Both Texas and Colorado have local tax structures, but single-member foreign-owned LLCs with purely digital operations outside the US once again bypass this via the ETBUS structure. That means your ultimate tax rate stays at 0%, but the ease of maintaining that status is much simpler in Colorado.",
    cta_title="Secure Your US LLC Today"
)

# Write all files
import pathlib
folder = "/Users/mayankmalik/Documents/SBO WEBSITE "

with open(os.path.join(folder, "wyoming-vs-delaware.html"), "w", encoding="utf-8") as f:
    f.write(wy_vs_de)

with open(os.path.join(folder, "wyoming-vs-new-mexico.html"), "w", encoding="utf-8") as f:
    f.write(wy_vs_nm)

with open(os.path.join(folder, "delaware-vs-florida.html"), "w", encoding="utf-8") as f:
    f.write(de_vs_fl)

with open(os.path.join(folder, "texas-vs-colorado.html"), "w", encoding="utf-8") as f:
    f.write(tx_vs_co)

print("Created 4 HTML files")
