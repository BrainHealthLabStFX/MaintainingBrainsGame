with open('index.html', 'r') as f:
    html = f.read()

replacements = [
    ('<span class="material-symbols-outlined text-brand-pink text-lg">science</span> Plastic Straws', ''),
    ('<span class="material-symbols-outlined text-brand-pink text-lg">hub</span> Pipe Cleaners', ''),
    ('<span class="material-symbols-outlined text-brand-pink text-lg">circle</span> Glass Marbles', ''),
    ('<span class="material-symbols-outlined text-brand-pink text-lg">masks</span> Face Masks', ''),
    ('In addition to printed card decks and instruction sheets, game tables use simple low-cost physical items available at dollar stores:', '')
]

for old, new in replacements:
    html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
print("Icons and text wiped.")
