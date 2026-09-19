with open('index.html', 'r') as f:
    html = f.read()

import re

# Replace Hero
html = re.sub(r'(<h1[^>]*>).*?(</h1>)', r'\1Loading...\2', html, count=1, flags=re.DOTALL)
html = re.sub(r'(<p class="text-xl md:text-2xl text-slate-700 mb-10 leading-relaxed max-w-2xl font-medium">).*?(</p>)', r'\1Loading...\2', html, count=1, flags=re.DOTALL)

# Let's not risk regex mangling the entire file. Let's just instruct the user.
