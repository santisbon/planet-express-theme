import random, sys
W, H = 5120, 2880
out = sys.argv[1]
random.seed(3000)

def stars(n, maxr):
    s = []
    for _ in range(n):
        x, y = random.uniform(0, W), random.uniform(0, H)
        r = random.choice([1.2, 1.6, 2, 2.6]) if random.random() > 0.03 else maxr
        c = random.choice(["#f4f2fb", "#e4e1f0", "#8eedf0", "#cfa3ec", "#ffe08f"])
        o = random.uniform(0.35, 1)
        s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{c}" opacity="{o:.2f}"/>')
    return "\n".join(s)

def binary_cols(color, op, ymax):
    t = []
    for i in range(46):
        x = 60 + i * 112 + random.uniform(-20, 20)
        y0 = random.uniform(-400, ymax * 0.6)
        n = random.randint(6, 22)
        for k in range(n):
            ch = random.choice("01")
            fade = (k + 1) / n
            t.append(f'<text x="{x:.0f}" y="{y0 + k*64:.0f}" fill="{color}" opacity="{op*fade:.2f}" '
                     f'font-family="JetBrainsMono Nerd Font, monospace" font-size="48">{ch}</text>')
    return "\n".join(t)

if out.endswith("space.svg"):
    body = f'''
<defs>
 <radialGradient id="sky" cx="30%" cy="25%" r="90%">
  <stop offset="0" stop-color="#24213a"/><stop offset="0.55" stop-color="#15131f"/><stop offset="1" stop-color="#0b0a11"/>
 </radialGradient>
 <radialGradient id="neb" cx="50%" cy="50%" r="50%">
  <stop offset="0" stop-color="#b57edc" stop-opacity="0.22"/><stop offset="1" stop-color="#b57edc" stop-opacity="0"/>
 </radialGradient>
 <radialGradient id="planet" cx="35%" cy="30%" r="75%">
  <stop offset="0" stop-color="#a3e8b2"/><stop offset="0.5" stop-color="#3f9a5a"/><stop offset="1" stop-color="#0f2a1a"/>
 </radialGradient>
 <radialGradient id="moon" cx="35%" cy="30%" r="80%">
  <stop offset="0" stop-color="#cfa3ec"/><stop offset="1" stop-color="#3a2650"/>
 </radialGradient>
 <clipPath id="front"><rect x="0" y="2050" width="{W}" height="900"/></clipPath>
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<ellipse cx="1300" cy="900" rx="1700" ry="900" fill="url(#neb)"/>
<ellipse cx="4300" cy="2500" rx="1400" ry="700" fill="url(#neb)" opacity="0.6"/>
{stars(900, 4)}
{binary_cols("#5ce1e6", 0.10, H)}
<g transform="rotate(-14 3800 2050)">
 <ellipse cx="3800" cy="2050" rx="1150" ry="210" fill="none" stroke="#ff8c42" stroke-width="34" opacity="0.55"/>
</g>
<circle cx="3800" cy="2050" r="620" fill="url(#planet)"/>
<g transform="rotate(-14 3800 2050)" clip-path="url(#front)">
 <ellipse cx="3800" cy="2050" rx="1150" ry="210" fill="none" stroke="#ffd166" stroke-width="34" opacity="0.8"/>
</g>
<circle cx="1050" cy="2250" r="150" fill="url(#moon)"/>
'''
else:
    # CRT perspective grid
    lines = []
    hy = 1750
    for i in range(-40, 41):
        x = W/2 + i * 260
        lines.append(f'<line x1="{W/2 + i*18:.0f}" y1="{hy}" x2="{x:.0f}" y2="{H}" stroke="#7bd88f" stroke-width="4" opacity="0.55"/>')
    y, step = hy, 14
    while y < H:
        lines.append(f'<line x1="0" y1="{y:.0f}" x2="{W}" y2="{y:.0f}" stroke="#7bd88f" stroke-width="4" opacity="0.55"/>')
        step *= 1.22; y += step
    sun = []
    for k in range(9):
        yy = 1120 + k * 70
        sun.append(f'<rect x="{W/2-600:.0f}" y="{yy}" width="1200" height="{8 + k*4}" fill="#24213a"/>')
    scan = "\n".join(f'<rect x="0" y="{y}" width="{W}" height="2" fill="#000" opacity="0.18"/>' for y in range(0, H, 8))
    body = f'''
<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0b0a11"/><stop offset="0.45" stop-color="#24213a"/><stop offset="0.61" stop-color="#3a2650"/><stop offset="0.62" stop-color="#0b0a11"/><stop offset="1" stop-color="#15131f"/>
 </linearGradient>
 <linearGradient id="sun" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#ffd166"/><stop offset="0.5" stop-color="#ff8c42"/><stop offset="1" stop-color="#b57edc"/>
 </linearGradient>
 <clipPath id="sundisc"><circle cx="{W/2}" cy="1350" r="560"/></clipPath>
 <clipPath id="sunclip"><rect x="0" y="0" width="{W}" height="{hy}"/></clipPath>
 <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0b0a11" stop-opacity="0.85"/><stop offset="0.35" stop-color="#0b0a11" stop-opacity="0"/>
 </linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
{stars(500, 3).replace('cy="', 'data-y="').replace('data-y="', 'cy="')}
{binary_cols("#7bd88f", 0.16, hy)}
<g clip-path="url(#sunclip)">
 <circle cx="{W/2}" cy="1350" r="560" fill="url(#sun)"/>
 <g clip-path="url(#sundisc)">{"".join(sun)}</g>
</g>
<rect x="0" y="{hy}" width="{W}" height="{H-hy}" fill="#0b0a11"/>
{"".join(lines)}
<rect x="0" y="{hy}" width="{W}" height="{H-hy}" fill="url(#fade)"/>
<text x="{W/2}" y="2700" text-anchor="middle" fill="#5ce1e6" opacity="0.55" font-family="JetBrainsMono Nerd Font, monospace" font-size="72">01000110 01010010 01011001</text>
{scan}
'''
open(out, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">{body}</svg>')
