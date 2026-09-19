import re

with open('index.html', 'r') as f:
    html = f.read()

# I will use a simple regex to replace the content of elements that are hydrated
# But I must be careful not to delete child elements that are required for hydration like the container grid!
# Actually, since I confirmed the JS hydration perfectly replaces the content, I can just leave the HTML as-is. Wait, the user ASKED to remove placeholders!

# A safer approach: I will revert to the previous `wipe_text.py` but add the <em> tags to the find/replace.

replacements = [
    ("Everything you need to facilitate and play the <em>Maintaining Brains Game</em> in your classroom or community group. Download complete PDF card packages and instruction sheets.", "")
]

for old, new in replacements:
    html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
print("Finished wiping.")
