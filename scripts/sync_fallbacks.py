import os
import re

try:
    import yaml
except ImportError:
    yaml = None

def parse_simple_yaml(filepath):
    data = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_key = None
    multiline_val = []
    in_multiline = False

    for line in lines:
        if in_multiline:
            if line.startswith('  ') or line.strip() == '':
                multiline_val.append(line[2:] if line.startswith('  ') else line)
                continue
            else:
                data[current_key] = ''.join(multiline_val).strip()
                in_multiline = False
                multiline_val = []
        
        match = re.match(r'^([a-zA-Z0-9_]+):\s*(.*)', line)
        if match:
            key, val = match.groups()
            val = val.strip()
            if val in ('|', '|-', '>', '>-'):
                current_key = key
                in_multiline = True
                multiline_val = []
            else:
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1]
                data[key] = val
    
    if in_multiline:
        data[current_key] = ''.join(multiline_val).strip()

    return data

def load_yaml(filepath):
    if yaml:
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return parse_simple_yaml(filepath)

def sync():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Hero
    if os.path.exists('_data/hero.yml'):
        hero = load_yaml('_data/hero.yml')
        if hero:
            if hero.get('headline'):
                html = re.sub(
                    r'(<h1 class="text-4xl md:text-6xl font-black tracking-tight mb-6 leading-tight">\s*).*?(</h1>)',
                    rf'\1{hero["headline"]}\2',
                    html, flags=re.DOTALL
                )
            if hero.get('highlights') and isinstance(hero['highlights'], list):
                items = []
                for item in hero['highlights']:
                    icon = item.get('icon', '')
                    text = item.get('text', '')
                    icon_html = f'<span class="w-10 h-10 rounded-2xl bg-pink-200/80 text-brand-darkPink flex items-center justify-center shrink-0"><span class="material-symbols-outlined text-xl">{icon}</span></span>' if icon else ''
                    items.append(f'<div class="flex items-center gap-3">{icon_html}<span>{text}</span></div>')
                highlights_html = f'<div id="hero-highlights" class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-6 text-pink-950 text-xs font-extrabold">\n            ' + '\n            '.join(items) + '\n        </div>'
                html = re.sub(r'<div id="hero-highlights"[^>]*>.*?</div>\s*</div>', highlights_html + '\n    ', html, flags=re.DOTALL)

    # 2. Creators
    if os.path.exists('_data/creators.yml'):
        creators = load_yaml('_data/creators.yml')
        if creators:
            if creators.get('title'):
                html = re.sub(r'(<h2 id="creators-title"[^>]*>).*?(</h2>)', rf'\1{creators["title"]}\2', html, flags=re.DOTALL)
            if creators.get('p1'):
                html = re.sub(r'(<p id="creators-p1"[^>]*>).*?(</p>)', rf'\1{creators["p1"]}\2', html, flags=re.DOTALL)
            if creators.get('p2'):
                html = re.sub(r'(<p id="creators-p2"[^>]*>).*?(</p>)', rf'\1{creators["p2"]}\2', html, flags=re.DOTALL)
            if 'image_title' in creators:
                img_title = creators['image_title'] or ''
                html = re.sub(r'(<div class="photo-card[^>]*>\s*<img[^>]*>\s*<div class="p-6">\s*<h4[^>]*>).*?(</h4>)', rf'\1{img_title}\2', html, flags=re.DOTALL)
            if 'image_caption' in creators:
                img_cap = creators['image_caption'] or ''
                html = re.sub(r'(<div class="photo-card[^>]*>\s*<img[^>]*>\s*<div class="p-6">\s*<h4[^>]*>.*?</h4>\s*<p[^>]*>).*?(</p>)', rf'\1{img_cap}\2', html, flags=re.DOTALL)

    # 3. Educators
    if os.path.exists('_data/educators.yml'):
        edu = load_yaml('_data/educators.yml')
        if edu and edu.get('feedback_body'):
            html = re.sub(
                r'(<h4 class="font-bold text-slate-900 text-lg mb-2">Are you an educator using the game\?</h4>\s*<p class="text-slate-700 text-sm leading-relaxed font-medium">\s*).*?(</p>)',
                rf'\1{edu["feedback_body"]}\2',
                html, flags=re.DOTALL
            )

    # 4. Customize
    if os.path.exists('_data/customize.yml'):
        cust = load_yaml('_data/customize.yml')
        if cust and cust.get('title'):
            html = re.sub(
                r'(<section id="customize".*?<h3 class="[^"]*">)(.*?)(</h3>)',
                rf'\1{cust["title"]}\3',
                html, flags=re.DOTALL
            )

    # 5. Attribution
    if os.path.exists('_data/attribution.yml'):
        attr = load_yaml('_data/attribution.yml')
        if attr and attr.get('text'):
            formatted_text = attr["text"].strip().replace('\n', '\n                    ')
            html = re.sub(
                r'(<p class="text-xs text-pink-200 leading-relaxed font-medium footer-attribution-text">\s*).*?(</p>)',
                rf'\1{formatted_text}\2',
                html, flags=re.DOTALL
            )

    # 6. Settings
    if os.path.exists('_data/settings.yml'):
        st = load_yaml('_data/settings.yml')
        if st:
            if st.get('title'):
                html = re.sub(r'(<span id="footer-title"[^>]*>).*?(</span>)', rf'\1{st["title"]}\2', html, flags=re.DOTALL)
            if st.get('tagline'):
                html = re.sub(r'(<span id="footer-tagline"[^>]*>).*?(</span>)', rf'\1{st["tagline"]}\2', html, flags=re.DOTALL)

    # 7. Configuration (Site Title)
    if os.path.exists('_data/configuration.yml'):
        cfg = load_yaml('_data/configuration.yml')
        if cfg and cfg.get('site_title'):
            site_title = cfg['site_title']
            html = re.sub(r'(<title>).*?(</title>)', rf'\1{site_title} | Mazerolle Lab at StFX\2', html, flags=re.DOTALL)
            html = re.sub(r'(<span id="header-site-title"[^>]*>).*?(</span>)', rf'\1{site_title}\2', html, flags=re.DOTALL)

    # 8. Menu Links
    if os.path.exists('_data/menu.yml'):
        menu = load_yaml('_data/menu.yml')
        if menu and menu.get('menu_links'):
            links = menu['menu_links']
            desktop_nav = '\n                '.join([f'<a href="{l["url"]}" class="nav-link hover:text-brand-darkPink transition-colors px-1.5 py-1">{l["label"]}</a>' for l in links])
            mobile_nav = '\n                '.join([f'<a href="{l["url"]}" class="mobile-nav-link hover:text-brand-lightPink transition-colors py-2 border-b border-slate-800">{l["label"]}</a>' for l in links])
            
            html = re.sub(r'(<!-- Desktop Navigation -->\s*<nav[^>]*>).*?(</nav>)', rf'\1\n                {desktop_nav}\n            \2', html, flags=re.DOTALL)
            html = re.sub(r'(<div id="mobile-menu"[^>]*>\s*<nav[^>]*>).*?(<a href="mailto:)', rf'\1\n                {mobile_nav}\n                \2', html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Static placeholders successfully synchronized.")

if __name__ == '__main__':
    sync()
