import os

base_file = "/Users/mayankmalik/Documents/SBO WEBSITE /index.html"
with open(base_file, "r", encoding="utf-8") as f:
    html = f.read()

# Extract head (up to </nav>)
head_split = html.split('</nav>', 1)
head_nav = head_split[0] + '</nav>\n'

custom_css = """
/* ── CALCULATOR STYLES ── */
.calc-grid {
  display:grid;grid-template-columns:3fr 2fr;gap:48px;max-width:1100px;margin:64px auto;
}
@media(max-width:850px) {
  .calc-grid { grid-template-columns:1fr; }
}
.c-group { margin-bottom: 24px; }
.c-label { font-size:14px;font-weight:700;color:#111;margin-bottom:8px;display:block;}
.c-sub { font-size:13px;color:var(--gray-500);margin-bottom:12px;line-height:1.5;}
.c-select, .c-input {
  width:100%;padding:14px 16px;font-size:15px;font-family:'Inter',sans-serif;
  border:1px solid var(--border);border-radius:var(--r);background:#fff;
  transition:border-color 0.2s, box-shadow 0.2s;
  outline:none;
}
.c-select:focus, .c-input:focus { border-color:var(--blue);box-shadow:0 0 0 3px #eff6ff;}

/* Custom Radio Cards */
.radio-cards { display:grid;grid-template-columns:1fr 1fr;gap:12px; }
.r-card {
  border:1px solid var(--border);border-radius:var(--r);padding:16px;cursor:pointer;
  transition:all 0.2s;background:#fff;position:relative;
}
.r-card:hover { border-color:var(--gray-400); }
.r-card input { position:absolute;opacity:0;cursor:pointer; }
.r-card.active { border-color:var(--blue);background:#eff6ff;box-shadow:inset 0 0 0 1px var(--blue);}
.r-title { font-weight:700;font-size:14px;color:#111;margin-bottom:4px;}
.r-desc { font-size:12px;color:var(--gray-500);line-height:1.4;}

/* Result Card Sticky */
.result-box {
  background:#fff;border:2px solid #111;border-radius:var(--r);padding:32px;
  position:sticky;top:90px;
  box-shadow:0 12px 32px rgba(0,0,0,0.06);
}
.res-title { font-size:18px;font-weight:800;color:#111;margin-bottom:24px;text-align:center;}
.res-row { display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;font-size:14px;}
.res-lbl { color:var(--gray-700);font-weight:500;}
.res-val { font-weight:700;color:#111;}
.res-total { font-size:42px;font-weight:800;color:var(--blue);text-align:center;margin:16px 0 24px;line-height:1;}
.res-total span { font-size:16px;color:var(--gray-500);font-weight:500;}

/* Tag/Badge for Effective Rate */
.eff-rate {
  display:inline-block;padding:6px 12px;font-size:13px;font-weight:700;
  color:#16a34a;background:#dcfce7;border-radius:50px;margin-bottom:24px;
}
</style>
"""

head_nav = head_nav.replace('</style>', custom_css)

# Extract footer
footer_split = html.split('<!-- FOOTER -->', 1)
footer = '<!-- FOOTER -->' + footer_split[1]

page_html = head_nav + """
<!-- HEADER -->
<section style="background:#f9fafb;padding:64px 20px;border-bottom:1px solid var(--border);">
  <div class="wrap center">
    <div class="label">Free Calculator</div>
    <h1 style="font-size:clamp(26px,5vw,36px);font-weight:800;margin-bottom:12px;">US LLC Tax Estimator for Non-Residents</h1>
    <p class="sub" style="max-width:680px;margin:0 auto;">Answer a few quick questions to estimate your exact US tax liability and annual state fees.</p>
  </div>
</section>

<!-- MAIN CALCULATOR AREA -->
<section style="padding:0 20px; background:#fff;">
  <div class="calc-grid">
    
    <!-- LEFT: FORM -->
    <div class="calc-form">
      <h3 style="font-size:20px;font-weight:800;margin-bottom:24px;">Your Business Profile</h3>
      
      <div class="c-group">
        <label class="c-label">1. Are you a US Resident or Citizen?</label>
        <p class="c-sub">If you spend 183+ days in the US, you are considered a US tax resident.</p>
        <div class="radio-cards">
          <label class="r-card active" id="rc-res-no">
            <input type="radio" name="residency" value="no" checked onchange="updateCalc()">
            <div class="r-title">No, Non-US Resident</div>
            <div class="r-desc">I live outside the USA</div>
          </label>
          <label class="r-card" id="rc-res-yes">
            <input type="radio" name="residency" value="yes" onchange="updateCalc()">
            <div class="r-title">Yes, US Resident</div>
            <div class="r-desc">I am a US citizen or resident alien</div>
          </label>
        </div>
      </div>

      <div class="c-group">
        <label class="c-label">2. LLC Structure</label>
        <p class="c-sub">Single-member LLCs are "disregarded entities". Multi-member LLCs are taxed as partnerships.</p>
        <div class="radio-cards">
          <label class="r-card active" id="rc-struct-single">
            <input type="radio" name="structure" value="single" checked onchange="updateCalc()">
            <div class="r-title">One Owner</div>
            <div class="r-desc">100% owned by you</div>
          </label>
          <label class="r-card" id="rc-struct-multi">
            <input type="radio" name="structure" value="multi" onchange="updateCalc()">
            <div class="r-title">Two or more Owners</div>
            <div class="r-desc">Partnership structure</div>
          </label>
        </div>
      </div>
      
      <div class="c-group" id="group-presence">
        <label class="c-label">3. US Business Presence (ETBUS)</label>
        <p class="c-sub">Do you have physical operations in the US? (e.g., US employees, a physical US office/warehouse, dependent agents closing contracts in the US)</p>
        <div class="radio-cards">
          <label class="r-card active" id="rc-pres-no">
            <input type="radio" name="presence" value="no" checked onchange="updateCalc()">
            <div class="r-title">No Physical Presence</div>
            <div class="r-desc">100% remote / online business</div>
          </label>
          <label class="r-card" id="rc-pres-yes">
            <input type="radio" name="presence" value="yes" onchange="updateCalc()">
            <div class="r-title">Yes, I have physical presence</div>
            <div class="r-desc">US offices, warehouse, employees</div>
          </label>
        </div>
      </div>
      
      <div class="c-group">
        <label class="c-label">4. State of Formation</label>
        <p class="c-sub">Select the state where you plan to form or have formed your LLC.</p>
        <select class="c-select" id="calc-state" onchange="updateCalc()">
          <option value="wyoming">Wyoming</option>
          <option value="delaware">Delaware</option>
          <option value="new_mexico">New Mexico</option>
          <option value="florida">Florida</option>
          <option value="texas">Texas</option>
          <option value="colorado">Colorado</option>
        </select>
      </div>

      <div class="c-group">
        <label class="c-label">5. Estimated Annual Business Profit ($ USD)</label>
        <p class="c-sub">Your expected profit from US business operations (Revenue minus expenses).</p>
        <input type="number" class="c-input" id="calc-profit" value="50000" oninput="updateCalc()">
      </div>
      
      <div style="background:#eff6ff;padding:20px;border-radius:var(--r);margin-top:32px;">
        <h4 style="font-size:15px;color:var(--blue);margin-bottom:8px;">💡 What is ETBUS?</h4>
        <p style="font-size:13px;color:var(--gray-700);margin:0;line-height:1.6;">"Engaged in a Trade or Business in the US". If you are a non-US resident with an online business (dropshipping, freelancing, SaaS) and <strong>no physical operations/employees</strong> in the US, you are generally not ETBUS, meaning your business income is <strong>not subject to US federal income tax</strong>.</p>
      </div>
    </div>
    
    <!-- RIGHT: ESTIMATE RESULT -->
    <div>
      <div class="result-box">
        <div class="res-title">Your Tax Estimate</div>
        
        <div style="text-align:center;">
          <div class="eff-rate" id="res-rate">0% effective tax rate</div>
        </div>

        <div class="res-row">
          <div class="res-lbl">Federal Income Tax:</div>
          <div class="res-val" id="res-fed">$0</div>
        </div>
        
        <div class="res-row">
          <div class="res-lbl" id="state-lbl-fee">Annual State Maintenance:</div>
          <div class="res-val" id="res-state-fee">$160</div>
        </div>
        
        <div class="res-row">
          <div class="res-lbl">IRS Return Filing (Forms 1120/5472):</div>
          <div class="res-val">$170</div>
        </div>
        <hr style="margin:20px 0; border:none; border-top:1px solid var(--border);">
        
        <div style="text-align:center;font-size:12px;font-weight:700;color:var(--gray-400);text-transform:uppercase;letter-spacing:1px;">Estimated Total Due / Year</div>
        <div class="res-total" id="res-total">$330</div>
        
        <p id="res-warning" style="font-size:13px;color:#e11d48;line-height:1.5;text-align:center;display:none;background:#ffe4e6;padding:12px;border-radius:var(--r);font-weight:500;">
          Since you have US Residency or Physical Presence, your profits may be subject to US Federal Income Tax at graduated rates. We highly recommend consulting a US CPA for an exact calculation.
        </p>

        <a class="btn-green" href="/index.html#pricing" style="width:100%;font-size:16px;padding:18px 0;margin-top:16px;">Form your LLC Today &rarr;</a>
        
        <p style="font-size:11px;color:var(--gray-400);margin-top:20px;text-align:center;line-height:1.5;">This calculator provides estimates based on standard interpretations of US tax codes for non-residents (No ECI/ETBUS). This is not legal or tax advice. You must still file informational forms (1120/5472) annually.</p>
      </div>
    </div>
    
  </div>
</section>

<script>
function updateCalc() {
  // Update Radio Active States
  document.querySelectorAll('.r-card').forEach(c => c.classList.remove('active'));
  document.querySelector('#rc-res-' + document.querySelector('input[name="residency"]:checked').value).classList.add('active');
  document.querySelector('#rc-struct-' + document.querySelector('input[name="structure"]:checked').value).classList.add('active');
  document.querySelector('#rc-pres-' + document.querySelector('input[name="presence"]:checked').value).classList.add('active');

  let isResident = document.querySelector('input[name="residency"]:checked').value === 'yes';
  let hasPresence = document.querySelector('input[name="presence"]:checked').value === 'yes';
  let state = document.getElementById('calc-state').value;
  let profit = parseFloat(document.getElementById('calc-profit').value) || 0;

  let fedTax = 0;
  let stateFee = 0;
  let supportFee = 170;
  
  // State Fees lookup
  const sf = {
    'wyoming': 160,
    'delaware': 300,
    'new_mexico': 0,
    'florida': 138,
    'texas': 0, // Simplified!
    'colorado': 10
  };
  stateFee = sf[state];

  // Logic
  if (isResident || hasPresence) {
    // Subject to US Tax (roughly estimate 21% blended income tax just for demo purposes)
    fedTax = profit * 0.21;
    document.getElementById('res-warning').style.display = 'block';
  } else {
    // Non-resident, no physical presence = $0 federal tax
    fedTax = 0;
    document.getElementById('res-warning').style.display = 'none';
  }

  // Update DOM
  document.getElementById('res-fed').textContent = fedTax > 0 ? '$' + fedTax.toLocaleString(undefined, {maximumFractionDigits:0}) : '$0';
  document.getElementById('res-state-fee').textContent = '$' + stateFee;
  
  let total = fedTax + stateFee + supportFee;
  document.getElementById('res-total').textContent = '$' + total.toLocaleString(undefined, {maximumFractionDigits:0});

  let rate = profit > 0 ? (fedTax / profit) * 100 : 0;
  let rateEl = document.getElementById('res-rate');
  rateEl.textContent = rate.toFixed(1) + '% effective tax rate';
  
  if(rate > 0) {
    rateEl.style.background = '#fee2e2';
    rateEl.style.color = '#b91c1c';
  } else {
    rateEl.style.background = '#dcfce7';
    rateEl.style.color = '#16a34a';
  }
}

// Initial calculation
updateCalc();
</script>
""" + footer

page_html = page_html.replace('<title>US LLC Formation — Smart Biz Owner by Mayank Malik</title>', '<title>US LLC Tax Estimator Calculator | Smart Biz Owner</title>')
page_html = page_html.replace('content="Open a US LLC in 48 hours from anywhere. Starts from $299. EIN, registered agent, bank guidance — all included. 500+ LLCs delivered since 2021."', 'content="Calculate your US LLC taxes and state maintenance fees easily with our free non-resident tax estimator calculator."')

with open("/Users/mayankmalik/Documents/SBO WEBSITE /llc-tax-estimator.html", "w", encoding="utf-8") as f:
    f.write(page_html)
