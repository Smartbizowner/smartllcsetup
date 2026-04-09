import os

filepath = "/Users/mayankmalik/Documents/SBO WEBSITE /sbo-llc-final.html"
with open(filepath, "r") as f:
    lines = f.readlines()

A = lines[0:491] # 0 to 490
B = lines[491:534] # 4. PROCESS (491 is empty line before it)
C = lines[534:561] # SERVICES WE PROVIDE
D = lines[561:681] # 5. PRICING WIZARD
E = lines[681:714] # 7. TRUST
F = lines[714:729] # VIDEO REVIEWS
G = lines[729:]    # ABOUT + SOCIAL and rest

# Let's adjust D background
# D starts at index 0 of its array (empty line), then 1: <!-- 5. PRICING WIZARD -->, 2: <section style="background:var(--gray-50)" id="pricing">
for i, line in enumerate(D):
    if '<section style="background:var(--gray-50)" id="pricing">' in line:
        D[i] = line.replace('style="background:var(--gray-50)"', 'style="background:#fff"')

# Let's adjust E background (Text Testimonial). Change to #fff
for i, line in enumerate(E):
    if '<section style="background:var(--gray-50)">' in line:
        E[i] = line.replace('style="background:var(--gray-50)"', 'style="background:#fff"')

# Let's adjust B background (3 Steps). Change to gray-50
for i, line in enumerate(B):
    if '<section>' in line:
        B[i] = line.replace('<section>', '<section style="background:var(--gray-50)">')

# C is already <section style="background:#fff;border-bottom:1px solid var(--border);">
# F needs to be split into F1 and F2
F_str = "".join(F)
# Split F manually since we know the exact HTML
F1_html = """
<!-- VIDEO REVIEWS -->
<section style="background:var(--gray-50)">
  <div class="wrap">
    <div class="label center">Video proof</div>
    <h2 class="center">Hear It From Clients</h2>
    <div class="vid-grid">
      <div class="vid-wrap"><iframe src="https://player.vimeo.com/video/622112840?badge=0&autopause=0" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Client review 1"></iframe></div>
      <div class="vid-wrap"><iframe src="https://player.vimeo.com/video/664157351?badge=0&autopause=0" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Client review 2"></iframe></div>
    </div>
  </div>
</section>
"""

F2_html = """
<!-- BONUS EDUCATIONAL CONTENT -->
<section style="background:#fff">
  <div class="wrap">
    <div class="label center">Bonus</div>
    <h2 class="center">How to open a US bank account as a non-resident</h2>
    <p class="sub center" style="max-width:580px;margin:0 auto 0;">Use it for Shopify, Facebook Ads, Google Ads — without paying currency conversion fees every time.</p>
    <div class="vid-single" style="margin-top:28px;"><iframe src="https://www.youtube.com/embed/644GQThGFrI?si=JB2Xg6Xn7OKiinbh" title="US bank account for non-residents" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
  </div>
</section>
"""

# Reconstruct
new_content = "".join(A) + "".join(D) + F1_html + "".join(E) + "".join(B) + "".join(C) + F2_html + "".join(G)

with open(filepath, "w") as f:
    f.write(new_content)

print("Done")
