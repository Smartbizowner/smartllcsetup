import re

new_content = """<section class="article-wrap">
  <h2>US LLC – A Potential Tax Haven For Foreigners. Why?</h2>
  <p>A US-based LLC can have great tax advantages, especially for foreign entrepreneurs abroad. An LLC is a pass-through tax entity. What this means is that the LLC is not taxed directly. Instead, the profits and losses of the business pass through to its owners, who report them on their personal tax returns.</p>

  <h3>Tax-free LLC income for foreign owners of a US LLC</h3>
  <p>A little-known fact is that the US can be one of the biggest tax havens in the world. A US LLC opened by a non-US citizen or nonresident can arguably allow for earnings that are not taxed in the US.</p>
  <p>Effectively, foreigners are only subject to US tax if they are “engaged in a trade or business in the United States” (ETOB). If your business is <strong>not</strong> ETOB, even if it generates income in the US, the income is not taxed in the US.</p>
  
  <div class="alert" style="margin-top:32px;">
    <strong>However, you are engaged in a trade or business (ETOB) in the US if:</strong>
  </div>
  
  <div class="proc-list" style="margin-top:16px;margin-bottom:32px;">
    <div class="proc-row">
      <div class="proc-n">1</div>
      <div>
        <strong>Dependent Agent in the US</strong>
        <span>You have at least one “dependent agent” in the US, which are employees or companies that work for you almost exclusively.</span>
      </div>
    </div>
    <div class="proc-row">
      <div class="proc-n">2</div>
      <div>
        <strong>Substantial US Activity</strong>
        <span>This dependent agent does something substantial to further your business in the US, as opposed to something purely administrative.</span>
      </div>
    </div>
    <div class="proc-row">
      <div class="proc-n">3</div>
      <div>
        <strong>Continuous Business</strong>
        <span>You are engaged in “considerable, continuous, and regular” business in the US.</span>
      </div>
    </div>
  </div>
  
  <p>If you meet these conditions, you have to pay on those earnings. We analyze the bank statements and nature of the business to confirm whether it is ETOB or NON-ETOB.</p>

  <hr style="margin:48px 0;">

  <h2>What to file, and how much it costs (SBO US Certified CPA)</h2>
  <p>You will transfer all profits and losses of the business to your personal tax return in whichever country you are in. For example, you will file an ITR in India for your earnings.</p>
  <p><strong>But still, you have to pay specific fees in the US to keep your LLC in good standing and active.</strong></p>

  <h3>Annual Fees Breakdown (Wyoming vs Delaware)</h3>
  <p>Below is a visual breakdown of the estimated annual maintenance and tax filing costs for a single-member LLC generating under $100k.</p>

  <!-- Visual CSS Graph blocks -->
  <div style="display:flex;flex-direction:column;gap:24px;margin:32px 0;">
    
    <!-- Wyoming Graph -->
    <div style="border:1px solid var(--border);border-radius:var(--r);padding:24px;background:#fff;box-shadow:0 4px 12px rgba(0,0,0,0.03);">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <h4 style="font-size:18px;font-weight:700;margin:0;">Wyoming Total: <span style="color:var(--green-d);">$330</span></h4>
      </div>
      <!-- Stacked Bar -->
      <div style="display:flex;width:100%;height:32px;border-radius:6px;overflow:hidden;margin-bottom:16px;">
        <div title="State Fee: $60" style="width:18%;background:#3b82f6;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:600;">$60</div>
        <div title="Agent Address: $25" style="width:8%;background:#60a5fa;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:600;">$25</div>
        <div title="IRS Federal Fee: $170" style="width:51%;background:#f59e0b;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:600;"><a href="./irs-return-filing.html" style="color:#fff;text-decoration:none;">$170 IRS</a></div>
        <div title="CPA Fee: $75" style="width:23%;background:#10b981;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:600;">$75</div>
      </div>
      <!-- Legend -->
      <div style="display:flex;flex-wrap:wrap;gap:16px;font-size:12px;color:var(--gray-500);">
        <div style="display:flex;align-items:center;gap:6px;"><div style="width:10px;height:10px;border-radius:2px;background:#3b82f6;"></div>State Fee</div>
        <div style="display:flex;align-items:center;gap:6px;"><div style="width:10px;height:10px;border-radius:2px;background:#60a5fa;"></div>Agent Address</div>
        <div style="display:flex;align-items:center;gap:6px;"><div style="width:10px;height:10px;border-radius:2px;background:#f59e0b;"></div>IRS Federal Fee</div>
        <div style="display:flex;align-items:center;gap:6px;"><div style="width:10px;height:10px;border-radius:2px;background:#10b981;"></div>CPA Filing Fee</div>
      </div>
    </div>

    <!-- Delaware Graph -->
    <div style="border:1px solid var(--border);border-radius:var(--r);padding:24px;background:#fff;box-shadow:0 4px 12px rgba(0,0,0,0.03);">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <h4 style="font-size:18px;font-weight:700;margin:0;">Delaware Total: <span style="color:var(--green-d);">$595</span></h4>
      </div>
      <!-- Stacked Bar -->
      <div style="display:flex;width:100%;height:32px;border-radius:6px;overflow:hidden;margin-bottom:16px;">
        <div title="State Fee: $300" style="width:50%;background:#3b82f6;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:600;">$300</div>
        <div title="Agent Address: $50" style="width:8%;background:#60a5fa;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:600;">$50</div>
        <div title="IRS Federal Fee: $170" style="width:29%;background:#f59e0b;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:600;"><a href="./irs-return-filing.html" style="color:#fff;text-decoration:none;">$170 IRS</a></div>
        <div title="CPA Fee: $75" style="width:13%;background:#10b981;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:600;">$75</div>
      </div>
      <!-- Legend -->
      <div style="display:flex;flex-wrap:wrap;gap:16px;font-size:12px;color:var(--gray-500);">
        <div style="display:flex;align-items:center;gap:6px;"><div style="width:10px;height:10px;border-radius:2px;background:#3b82f6;"></div>State Fee</div>
        <div style="display:flex;align-items:center;gap:6px;"><div style="width:10px;height:10px;border-radius:2px;background:#60a5fa;"></div>Agent Address</div>
        <div style="display:flex;align-items:center;gap:6px;"><div style="width:10px;height:10px;border-radius:2px;background:#f59e0b;"></div>IRS Federal Fee</div>
        <div style="display:flex;align-items:center;gap:6px;"><div style="width:10px;height:10px;border-radius:2px;background:#10b981;"></div>CPA Filing Fee</div>
      </div>
    </div>
    
  </div>

  <h3>Accounting + IRS Filing Fee For Different Revenues</h3>
  <div class="why-grid" style="margin-top:16px;margin-bottom:48px;">
    <div class="why-cell">
      <div class="why-num">$120</div>
      <div class="why-title">Under $300k</div>
      <div class="why-text">Basic transaction volume filing.</div>
    </div>
    <div class="why-cell">
      <div class="why-num">$150</div>
      <div class="why-title">Under $500k</div>
      <div class="why-text">Medium transaction volume filing.</div>
    </div>
    <div class="why-cell">
      <div class="why-num">$250</div>
      <div class="why-title">Under $1M</div>
      <div class="why-text">High transaction volume complex filing.</div>
    </div>
  </div>

  <h3>Documents we need to handle your US taxation:</h3>
  <div class="get-list" style="margin-top:16px;">
    <div class="get-row">
      <div class="get-icon"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"></path></svg></div>
      <div>
        <strong>Company Bank Statements</strong>
        <span>All digital bank statements reflecting incoming/outgoing transactions.</span>
      </div>
    </div>
    <div class="get-row">
      <div class="get-icon"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"></path></svg></div>
      <div>
        <strong>Owner Drawings</strong>
        <span>These are assets you withdraw from your business for your personal use.</span>
      </div>
    </div>
    <div class="get-row">
      <div class="get-icon"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"></path></svg></div>
      <div>
        <strong>Owner Investments</strong>
        <span>Any capital you personally invested into the business to keep it funded.</span>
      </div>
    </div>
    <div class="get-row">
      <div class="get-icon"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"></path></svg></div>
      <div>
        <strong>1099 Forms</strong>
        <span>If any is received or issued. A 1099 Form is a federal income tax form required by the IRS.</span>
      </div>
    </div>
  </div>
  
  <p style="margin-top:24px;">That's it; if we need anything more, we will contact you directly.</p>

  <div style="margin-top:48px;padding:32px;border:1px solid var(--border);border-radius:var(--r);background:var(--gray-50);text-align:center;">
    <h3 style="margin-top:0;margin-bottom:16px;">Ready to start your US taxation with SBO?</h3>
    <p style="margin-bottom:24px;color:var(--gray-700);">Contact us on WhatsApp with the above documents, and we will get it sorted.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
      <a href="https://wa.me/917566631566?text=Hello%2C%20I%20need%20help%20with%20the%20facebook%20solution%20setup.%20" target="_blank" rel="noopener" class="btn-green" style="padding:12px 24px;">Message on WhatsApp</a>
    </div>
    <div style="margin-top:20px;">
      <a href="https://www.instagram.com/mayankmaliik/" target="_blank" rel="noopener" style="color:var(--blue);text-decoration:underline;font-size:14px;font-weight:500;">Follow Mayank Malik on Instagram</a>
    </div>
  </div>
</section>"""

with open('llc-taxes-non-resident.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the whole <section class="article-wrap">
html = re.sub(r'<section class="article-wrap">.*?</section>', new_content, html, flags=re.DOTALL)

with open('llc-taxes-non-resident.html', 'w', encoding='utf-8') as f:
    f.write(html)
