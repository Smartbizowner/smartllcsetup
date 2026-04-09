import sys

file_path = "/Users/mayankmalik/Documents/SBO WEBSITE /sbo-llc-final.html"

with open(file_path, "r") as f:
    lines = f.readlines()

# 1. Slider integration
for i, line in enumerate(lines):
    if "<!-- 4. PROCESS -->" in line:
        slider_code = """    <div style="margin-top:40px;background:#fff;border:1px solid var(--border);border-radius:var(--r);padding:32px 24px;text-align:center;box-shadow:0 8px 24px rgba(0,0,0,.04);">
      <h3 style="font-size:20px;font-weight:800;color:#111;margin-bottom:8px;">Forex Loss Calculator</h3>
      <p style="font-size:14px;color:var(--gray-500);margin-bottom:24px;">See how much an Indian card charges you in hidden markup over time.</p>
      
      <div style="max-width:400px;margin:0 auto;">
        <label for="adSpend" style="display:block;font-size:15px;font-weight:600;color:var(--gray-700);margin-bottom:12px;">Total Ad Spend (INR)</label>
        <input type="range" id="adSpend" min="100000" max="10000000" step="100000" value="1000000" style="width:100%;cursor:pointer;accent-color:var(--blue);">
        <div style="font-size:18px;font-weight:800;color:var(--blue);margin-top:12px;" id="adSpendValue">₹10 Lakhs</div>
        
        <div style="margin-top:24px;padding:20px;background:#fff1f2;border:1px solid #fecdd3;border-radius:12px;">
          <div style="font-size:13px;color:#e11d48;font-weight:600;text-transform:uppercase;letter-spacing:0.5px;">You Lose in Bank Fees</div>
          <div id="forexLossValue" style="font-size:32px;font-weight:800;color:#be123c;margin:6px 0;line-height:1;">₹50,000</div>
          <p style="font-size:13px;color:#9f1239;margin:0;line-height:1.5;">A US LLC saves this 100%.</p>
        </div>
      </div>
      
      <script>
        const slider = document.getElementById('adSpend');
        const spendOutput = document.getElementById('adSpendValue');
        const lossOutput = document.getElementById('forexLossValue');
        
        slider.addEventListener('input', function() {
          const val = parseInt(this.value);
          const loss = Math.round(val * 0.05); // 5% total fees (forex + markup)
          
          let displaySpend = "₹" + val.toLocaleString('en-IN');
          if (val === 100000) displaySpend = "₹1 Lakh";
          else if (val >= 100000 && val < 10000000) {
            displaySpend = "₹" + (val/100000).toFixed(1).replace('.0', '') + " Lakhs";
          } else if (val === 10000000) displaySpend = "₹1 Crore";
          
          spendOutput.innerText = displaySpend;
          lossOutput.innerText = "₹" + loss.toLocaleString('en-IN');
        });
      </script>
    </div>
"""
        # Insert before closing wrap and section
        # The line "  </div>\n</section>\n" is right before line 421.
        # So we insert at i-2
        lines.insert(i-2, slider_code)
        break

# 2. Process Workflow Graphics Redesign
start_workflow = -1
end_workflow = -1
for i, line in enumerate(lines):
    if '<div class="proc-list">' in line:
        start_workflow = i
    if 'alt="LLC Formation Process"' in line:
        end_workflow = i + 2 # include the closing div
        break

workflow_code = """    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(min(100%, 280px), 1fr));gap:24px;margin-top:40px;">
      <!-- STEP 1 -->
      <div style="background:#fff;border:1px solid var(--border);border-radius:var(--r);padding:32px 24px;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.02);position:relative;">
        <div style="width:64px;height:64px;background:#eff6ff;color:var(--blue);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 20px;">
          <!-- Document Icon -->
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
        </div>
        <div style="position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:var(--blue);color:#fff;font-size:13px;font-weight:700;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;">1</div>
        <h3 style="font-size:18px;font-weight:800;color:#111;margin-bottom:12px;">Submit Details</h3>
        <p style="font-size:14px;color:var(--gray-600);line-height:1.6;margin:0;">Just 5 minutes. Enter your desired LLC name, state choice, passport legal name, and non-US address.</p>
      </div>

      <!-- STEP 2 -->
      <div style="background:#fff;border:1px solid var(--border);border-radius:var(--r);padding:32px 24px;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.02);position:relative;">
        <div style="width:64px;height:64px;background:#f3f4f6;color:var(--gray-700);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 20px;">
          <!-- Settings/Cogs -->
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
        </div>
        <div style="position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:var(--gray-700);color:#fff;font-size:13px;font-weight:700;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;">2</div>
        <h3 style="font-size:18px;font-weight:800;color:#111;margin-bottom:12px;">We File Everything</h3>
        <p style="font-size:14px;color:var(--gray-600);line-height:1.6;margin:0;">Sit back and relax. We handle state LLC filing, fast EIN application, and assign your registered agent.</p>
      </div>

      <!-- STEP 3 -->
      <div style="background:#fff;border:1px solid var(--border);border-radius:var(--r);padding:32px 24px;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.02);position:relative;">
        <div style="width:64px;height:64px;background:#fdf2f8;color:#be123c;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 20px;">
          <!-- Heart Icon -->
          <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
        </div>
        <div style="position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:#e11d48;color:#fff;font-size:13px;font-weight:700;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;">3</div>
        <h3 style="font-size:18px;font-weight:800;color:#111;margin-bottom:12px;">Hand-Off With Care</h3>
        <p style="font-size:14px;color:var(--gray-600);line-height:1.6;margin:0;">All documents are emailed directly, then we'll personally help you apply for your US bank, Stripe, and Shopify accounts.</p>
      </div>

    </div>\n"""

lines = lines[:start_workflow] + [workflow_code] + lines[end_workflow+1:]

# 3. Fix Typo "LLC Reinstatement Fee"
for i, line in enumerate(lines):
    if "LLC Reinstatement Fee" in line:
        lines[i] = line.replace("LLC Reinstatement Fee", "LLC Reinstatement")
        break

# 4. PRICING WIZARD
start_pricing = -1
end_pricing = -1
for i, line in enumerate(lines):
    if "<!-- 5. STATES -->" in line:
        start_pricing = i
    if "<!-- 7. TRUST -->" in line:
        end_pricing = i

wizard_code = """<!-- 5. PRICING WIZARD -->
<section style="background:var(--gray-50)" id="pricing">
  <div class="wrap center">
    <div class="label">Get Started</div>
    <h2>Pick Your State & Checkout</h2>
    <p class="sub" style="max-width:440px;margin:0 auto 0">Select your preferred state below. Pricing reflects your final cost including state fees. No hidden markups.</p>
    
    <div style="max-width:800px;margin:40px auto 0;display:flex;flex-wrap:wrap;gap:12px;justify-content:center;" id="stateSelector">
      <!-- Buttons populated by JS -->
    </div>

    <!-- Dynamic Checkout Card -->
    <div style="max-width:600px;margin:32px auto;background:#fff;border:2px solid var(--blue);border-radius:var(--r);padding:32px 24px;box-shadow:0 8px 32px rgba(0,0,0,0.06);position:relative;text-align:left;" id="checkoutCard">
      <div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;border-bottom:1px solid var(--border);padding-bottom:24px;margin-bottom:24px;gap:16px;">
        <div style="flex:1;">
          <span style="font-size:13px;font-weight:700;color:var(--blue);text-transform:uppercase;letter-spacing:0.5px;" id="selectedStateBadge">WYOMING LLC</span>
          <h3 style="font-size:28px;font-weight:800;color:#111;margin:4px 0 0;" id="selectedStateTitle">Wyoming</h3>
          <p style="font-size:14px;color:var(--gray-600);margin:4px 0 0;max-width:280px;line-height:1.5;" id="selectedStateDesc">Tax-free state. Best for privacy and low maintenance.</p>
        </div>
        <div style="text-align:right;">
          <div style="font-size:13px;color:var(--gray-500);font-weight:600;">Total Setup Cost</div>
          <div style="font-size:36px;font-weight:800;color:#111;line-height:1;margin-top:2px;" id="selectedStatePrice">$379</div>
        </div>
      </div>
      
      <h4 style="font-size:16px;font-weight:700;margin-bottom:16px;">What's included in every package:</h4>
      <div class="price-features" style="margin-bottom:32px;display:grid;grid-template-columns:1fr 1fr;gap:12px;">
        <div class="pf"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg> LLC formation + fees</div>
        <div class="pf"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg> EIN / Tax ID</div>
        <div class="pf"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg> Registered agent</div>
        <div class="pf"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg> Operating agreement</div>
        <div class="pf"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg> Bank account guidance</div>
        <div class="pf"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg> US address &amp; phone</div>
      </div>
      
      <a class="btn-green" href="https://buy.stripe.com/eVacPE1sk39A6RybJm" target="_blank" rel="noopener" id="checkoutBtn" style="font-size:16px;padding:16px 28px;width:100%;text-align:center;">Pay $379 via Stripe &rarr;</a>
      <p style="font-size:12px;color:var(--gray-400);text-align:center;margin-top:12px;display:flex;align-items:center;justify-content:center;gap:6px;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg> Secure 256-bit Stripe Checkout
      </p>
    </div>

    <!-- Script for Dynamic Selection -->
    <script>
      const statesData = [
        { id: "wyoming", name: "Wyoming", price: 379, link: "https://buy.stripe.com/eVacPE1sk39A6RybJm", desc: "Tax-free state. Best for privacy and low maintenance. Our #1 choice.", badge: "MOST POPULAR" },
        { id: "delaware", name: "Delaware", price: 379, link: "#stripe-link-delaware", desc: "Great for raising VC funding, advanced corporate court.", badge: "DELAWARE LLC" },
        { id: "newmexico", name: "New Mexico", price: 329, link: "#stripe-link-new-mexico", desc: "Most affordable. No annual reporting fees. Great privacy.", badge: "NEW MEXICO LLC" },
        { id: "florida", name: "Florida", price: 379, link: "#stripe-link-florida", desc: "Perfect for businesses targeting LatAm or a local footprint.", badge: "FLORIDA LLC" },
        { id: "texas", name: "Texas", price: 579, link: "https://buy.stripe.com/3cscPEc0Q9xY6RybJS", desc: "Strong local economy and no state income tax. Higher setup cost.", badge: "TEXAS LLC" },
        { id: "colorado", name: "Colorado", price: 329, link: "#stripe-link-colorado", desc: "Fast filing times. Low ongoing annual maintenance fees.", badge: "COLORADO LLC" },
        { id: "montana", name: "Montana", price: 299, link: "#stripe-link-montana", desc: "No sales tax. Completely private ownership. Our lowest price.", badge: "MONTANA LLC" }
      ];

      const selectorContainer = document.getElementById('stateSelector');
      const elTitle = document.getElementById('selectedStateTitle');
      const elBadge = document.getElementById('selectedStateBadge');
      const elDesc = document.getElementById('selectedStateDesc');
      const elPrice = document.getElementById('selectedStatePrice');
      const elBtn = document.getElementById('checkoutBtn');

      function selectState(id) {
        document.querySelectorAll('.state-btn').forEach(btn => {
          if (btn.dataset.id === id) {
            btn.style.background = 'var(--blue)';
            btn.style.color = '#fff';
            btn.style.borderColor = 'var(--blue)';
          } else {
            btn.style.background = '#fff';
            btn.style.color = 'var(--gray-700)';
            btn.style.borderColor = 'var(--border)';
          }
        });

        const data = statesData.find(s => s.id === id);
        elTitle.innerText = data.name;
        elBadge.innerText = data.badge;
        elDesc.innerText = data.desc;
        elPrice.innerText = "$" + data.price;
        elBtn.innerText = "Pay $" + data.price + " via Stripe \\u2192";
        elBtn.href = data.link;

        const card = document.getElementById('checkoutCard');
        card.style.opacity = '0.5';
        card.style.transform = 'translateY(4px)';
        setTimeout(() => {
          card.style.opacity = '1';
          card.style.transform = 'translateY(0)';
          card.style.transition = 'all 0.2s ease-out';
        }, 50);
      }

      statesData.forEach(state => {
        const btn = document.createElement('button');
        btn.className = 'state-btn';
        btn.dataset.id = state.id;
        btn.innerText = state.name;
        btn.style.cssText = 'padding:10px 20px;border-radius:50px;border:1px solid var(--border);background:#fff;font-size:14px;font-weight:600;cursor:pointer;color:var(--gray-700);transition:all 0.2s;font-family:inherit;';
        
        btn.onmouseover = function() { if(this.dataset.id !== elTitle.innerText.toLowerCase().replace(' ', '')) this.style.borderColor = 'var(--gray-400)'; };
        btn.onmouseout = function() { if(this.dataset.id !== elTitle.innerText.toLowerCase().replace(' ', '')) this.style.borderColor = 'var(--border)'; };
        btn.onclick = () => selectState(state.id);
        
        selectorContainer.appendChild(btn);
      });

      selectState('wyoming');
    </script>
  </div>
</section>
\n"""

lines = lines[:start_pricing] + [wizard_code] + lines[end_pricing:]

with open(file_path, "w") as f:
    f.writelines(lines)

print("Modification successful.")
