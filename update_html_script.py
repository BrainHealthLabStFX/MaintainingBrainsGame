with open("index.html", "r") as f:
    html = f.read()

import re

# We will replace the entire try/catch block with a new one that fetches each file separately.
new_script = """            try {
                const fetchYaml = async (url) => {
                    const res = await fetch(url);
                    if (res.ok) {
                        const text = await res.text();
                        return jsyaml.load(text);
                    }
                    return null;
                };

                // 1. Hero
                const hero = await fetchYaml('/_data/hero.yml');
                if (hero) {
                    const section = document.querySelector('section#about');
                    if (section && hero.section_id) section.id = hero.section_id;

                    if (hero.headline) {
                        const h1 = document.querySelector('h1');
                        if (h1) h1.innerHTML = hero.headline;
                    }
                    if (hero.body) {
                        const p = document.querySelector('.max-w-2xl p');
                        if (p) p.innerHTML = hero.body;
                    }
                    if (hero.image) {
                        const img = document.querySelector('#hero-image');
                        if (img) {
                            img.src = hero.image;
                            if (hero.focal_point) img.className = `w-full h-auto object-cover ${hero.focal_point} group-hover:scale-105 transition-transform duration-700`;
                        }
                    }
                    if (hero.highlights && Array.isArray(hero.highlights)) {
                        const highlightsContainer = document.querySelector('#hero-highlights');
                        if (highlightsContainer) {
                            highlightsContainer.innerHTML = hero.highlights.map(item => `
                                <div class="flex items-center gap-3">
                                    ${item.icon ? `<span class="w-10 h-10 rounded-2xl bg-pink-200/80 text-brand-darkPink flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-xl">${item.icon}</span>
                                    </span>` : ''}
                                    <span>${item.text}</span>
                                </div>
                            `).join('');
                        }
                    }
                    
                    const heroBtns = document.querySelectorAll('.flex.flex-col.sm\\\\:flex-row a');
                    if (heroBtns.length >= 2) {
                        if (hero.button1_text) heroBtns[0].childNodes[2].nodeValue = " " + hero.button1_text;
                        if (hero.button1_url) heroBtns[0].href = hero.button1_url;
                        if (hero.button2_text) heroBtns[1].childNodes[2].nodeValue = " " + hero.button2_text;
                        if (hero.button2_url) heroBtns[1].href = hero.button2_url;
                    }
                }

                // 2. Menu Links
                const menuData = await fetchYaml('/_data/menu.yml');
                if (menuData && menuData.menu_links && Array.isArray(menuData.menu_links)) {
                    const nav = document.querySelector('header nav');
                    const mobileNav = document.querySelector('#mobile-menu nav');
                    if (nav) {
                        nav.innerHTML = menuData.menu_links.map(link => 
                            `<a href="${link.url}" class="nav-link hover:text-brand-darkPink transition-colors px-1.5 py-1">${link.label}</a>`
                        ).join('');
                    }
                    if (mobileNav) {
                        mobileNav.innerHTML = menuData.menu_links.map(link => 
                            `<a href="${link.url}" class="mobile-nav-link hover:text-brand-lightPink transition-colors py-2 border-b border-slate-800">${link.label}</a>`
                        ).join('') + `<a href="mailto:emazerol@stfx.ca" class="mt-2 bg-brand-pink hover:bg-brand-darkPink text-white font-black text-center py-3 rounded-full flex items-center justify-center gap-2"><span class="material-symbols-outlined text-lg">mail</span><span>Contact Us</span></a>`;
                    }
                }

                // 3. Creators Section
                const c = await fetchYaml('/_data/creators.yml');
                if (c) {
                    const section = document.querySelector('section#creators');
                    if (section) {
                        if (c.section_id) section.id = c.section_id;
                        
                        if (c.title) {
                            const titleEl = document.querySelector('#creators-title');
                            if (titleEl) titleEl.textContent = c.title;
                        }
                        if (c.p1) {
                            const p1El = document.querySelector('#creators-p1');
                            if (p1El) p1El.innerHTML = c.p1;
                        }
                        if (c.p2) {
                            const p2El = document.querySelector('#creators-p2');
                            if (p2El) p2El.innerHTML = c.p2;
                        }
                        if (c.image) {
                            const img = document.querySelector('#creators-image');
                            if (img) {
                                img.src = c.image;
                                if (c.focal_point) img.className = `w-full h-80 object-cover ${c.focal_point}`;
                            }
                        }
                        if (c.badges && Array.isArray(c.badges)) {
                            // Find the badges grid inside this section using relative or specific selector
                            const badgeContainer = section.querySelector('.grid.grid-cols-3');
                            if (badgeContainer) {
                                badgeContainer.innerHTML = c.badges.map(b => `
                                    <div class="bg-pink-50/80 rounded-3xl p-4 border border-pink-200/80 hover:border-brand-pink transition-colors">
                                        <div class="text-2xl font-black text-brand-pink">${b.title}</div>
                                        <div class="text-xs text-slate-600 font-bold mt-1">${b.subtitle}</div>
                                    </div>
                                `).join('');
                            }
                        }
                        if (c.image_title) {
                            const titleEl = section.querySelector('h4');
                            if (titleEl) titleEl.textContent = c.image_title;
                        }
                        if (c.image_caption) {
                            const pEl = section.querySelector('.photo-card p');
                            if (pEl) pEl.textContent = c.image_caption;
                        }
                    }
                }

                // 4. Teachers Section
                const t = await fetchYaml('/_data/teachers.yml');
                if (t) {
                    const section = document.querySelector('section#teachers');
                    if (section) {
                        if (t.section_id) section.id = t.section_id;

                        if (t.title) {
                            const titleEl = section.querySelector('h2');
                            if (titleEl) titleEl.textContent = t.title;
                        }
                        if (t.body) {
                            const bodyEl = section.querySelector('.max-w-3xl p');
                            if (bodyEl) bodyEl.textContent = t.body;
                        }
                        if (t.curriculum_title) {
                            const titleEl = section.querySelector('h3');
                            if (titleEl) titleEl.innerHTML = `<span class="material-symbols-outlined text-brand-pink text-2xl">workspace_premium</span> ${t.curriculum_title}`;
                        }
                        if (t.curriculum_body) {
                            const bodyEl = section.querySelector('h3 + p');
                            if (bodyEl) bodyEl.innerHTML = t.curriculum_body;
                        }
                        if (t.discussion_questions_title) {
                            const titleEl = section.querySelector('h4.text-brand-fuschiaText');
                            if (titleEl) titleEl.textContent = t.discussion_questions_title;
                        }
                        if (t.questions && Array.isArray(t.questions)) {
                            const listEl = section.querySelector('ul');
                            if (listEl) {
                                listEl.innerHTML = t.questions.map(q => 
                                    `<li class="flex items-start gap-3 text-sm text-slate-800 bg-pink-50/80 p-4 rounded-3xl border border-pink-200/70 font-semibold hover:border-pink-300 transition-colors">
                                        <span class="material-symbols-outlined text-brand-pink text-xl shrink-0 mt-0.5">help_outline</span>
                                        <span>${q.question || q}</span>
                                    </li>`
                                ).join('');
                            }
                        }
                        if (t.feedback_title) {
                            const titleEl = section.querySelector('.lg\\\\:col-span-5 h4');
                            if (titleEl) titleEl.textContent = t.feedback_title;
                        }
                        if (t.feedback_body) {
                            const bodyEl = section.querySelector('.lg\\\\:col-span-5 h4 + p');
                            if (bodyEl) bodyEl.textContent = t.feedback_body;
                        }
                        if (t.feedback_button_text) {
                            const btn = section.querySelector('.lg\\\\:col-span-5 a');
                            if (btn) btn.innerHTML = `<span class="material-symbols-outlined text-lg">mail</span> ${t.feedback_button_text}`;
                        }
                        if (t.image) {
                            const img = section.querySelector('.photo-card img');
                            if (img) img.src = t.image;
                        }
                        if (t.image_caption) {
                            const caption = section.querySelector('.photo-card .p-4');
                            if (caption) caption.textContent = t.image_caption;
                        }
                    }
                }

                // 5. Download Section
                const d = await fetchYaml('/_data/download.yml');
                if (d) {
                    const section = document.querySelector('section#download');
                    if (section) {
                        if (d.section_id) section.id = d.section_id;

                        if (d.title) {
                            const titleEl = section.querySelector('h2');
                            if (titleEl) titleEl.textContent = d.title;
                        }
                        if (d.body) {
                            const bodyEl = section.querySelector('.max-w-2xl p');
                            if (bodyEl) bodyEl.textContent = d.body;
                        }
                        if (d.button_label) {
                            const btnSpan = section.querySelector('a span:last-child');
                            if (btnSpan) btnSpan.textContent = d.button_label;
                        }
                        if (d.button_url) {
                            const btn = section.querySelector('a');
                            if (btn) btn.href = d.button_url;
                        }
                        if (d.printing_tips && Array.isArray(d.printing_tips)) {
                            const listEl = section.querySelector('ul');
                            if (listEl) {
                                listEl.innerHTML = d.printing_tips.map(tip => `
                                    <li class="flex items-start gap-2.5">
                                        <span class="material-symbols-outlined text-brand-pink text-xl shrink-0">check_circle</span>
                                        <span>${tip.tip || tip}</span>
                                    </li>
                                `).join('');
                            }
                        }
                        if (d.materials_needed && Array.isArray(d.materials_needed)) {
                            const gridEl = section.querySelector('.grid.grid-cols-2');
                            if (gridEl) {
                                gridEl.innerHTML = d.materials_needed.map(m => `
                                    <div class="bg-white p-3.5 rounded-3xl border border-pink-200/80 flex items-center gap-2.5 shadow-sm">
                                        ${m.icon ? `<span class="material-symbols-outlined text-brand-pink text-lg">${m.icon}</span> ` : ''}${m.name}
                                    </div>
                                `).join('');
                            }
                        }
                    }
                }

                // 6. Research Section
                const r = await fetchYaml('/_data/research.yml');
                if (r) {
                    const section = document.querySelector('section#research');
                    if (section) {
                        if (r.section_id) section.id = r.section_id;

                        if (r.title) {
                            const titleEl = section.querySelector('h2');
                            if (titleEl) titleEl.textContent = r.title;
                        }
                        if (r.items && Array.isArray(r.items)) {
                            const gridEl = section.querySelector('.grid');
                            if (gridEl) {
                                gridEl.innerHTML = r.items.map(item => `
                                    <div class="bg-white rounded-3xl p-8 border border-pink-200/80 shadow-sm flex flex-col justify-between">
                                        <div>
                                            <div class="inline-block bg-pink-100 text-brand-darkPink text-xs font-black px-3.5 py-1 rounded-full mb-4">
                                                ${item.category}
                                            </div>
                                            <h3 class="text-lg font-bold text-slate-900 mb-2">${item.title}</h3>
                                            <p class="text-xs text-slate-600 font-medium mb-4">${item.authors}</p>
                                        </div>
                                        <a href="${item.link_url}" target="_blank" class="inline-flex items-center gap-2 text-sm font-extrabold text-brand-pink hover:text-brand-darkPink transition-colors mt-4">
                                            <span class="material-symbols-outlined text-lg">menu_book</span> ${item.link_text}
                                        </a>
                                    </div>
                                `).join('');
                            }
                        }
                    }
                }

                // 7. Tools Section
                const tools = await fetchYaml('/_data/tools.yml');
                if (tools) {
                    const section = document.querySelector('section#tools');
                    if (section) {
                        if (tools.section_id) section.id = tools.section_id;

                        if (tools.title) {
                            const titleEl = section.querySelector('h3');
                            if (titleEl) titleEl.textContent = tools.title;
                        }
                        if (tools.body) {
                            const bodyEl = section.querySelector('p');
                            if (bodyEl) bodyEl.textContent = tools.body;
                        }
                        if (tools.button_label) {
                            const btnSpan = section.querySelector('a span:last-child');
                            if (btnSpan) btnSpan.textContent = tools.button_label;
                        }
                        if (tools.button_url) {
                            const btn = section.querySelector('a');
                            if (btn) btn.href = tools.button_url;
                        }
                    }
                }

                // 8. Partners (Collaborators) Section
                const col = await fetchYaml('/_data/collaborators.yml');
                if (col) {
                    const section = document.querySelector('section#partners');
                    if (section) {
                        if (col.section_id) section.id = col.section_id;

                        if (col.title) {
                            const titleEl = section.querySelector('h2');
                            if (titleEl) titleEl.textContent = col.title;
                        }
                        if (col.body) {
                            const bodyEl = section.querySelector('.max-w-3xl p');
                            if (bodyEl) bodyEl.textContent = col.body;
                        }
                        if (col.items && Array.isArray(col.items)) {
                            const gridEl = section.querySelector('.grid');
                            if (gridEl) {
                                gridEl.innerHTML = col.items.map(item => `
                                    <div class="bg-white border border-pink-200/80 rounded-3xl p-8 flex flex-col justify-between shadow-sm">
                                        <div>
                                            ${item.icon ? `<div class="w-12 h-12 rounded-2xl bg-brand-pink text-white flex items-center justify-center text-xl font-bold mb-4 shadow-md shadow-pink-200">
                                                <span class="material-symbols-outlined text-2xl">${item.icon}</span>
                                            </div>` : ''}
                                            <h3 class="text-xl font-bold text-slate-900 mb-2">${item.name}</h3>
                                            <p class="text-sm text-slate-700 leading-relaxed font-medium">${item.description}</p>
                                        </div>
                                    </div>
                                `).join('');
                            }
                        }
                        if (col.feedback_title) {
                            const titleEl = section.querySelector('h4');
                            if (titleEl) titleEl.textContent = col.feedback_title;
                        }
                        if (col.feedback_body) {
                            const bodyEl = section.querySelector('h4 + p');
                            if (bodyEl) bodyEl.textContent = col.feedback_body;
                        }
                        if (col.feedback_button_text) {
                            const btn = section.querySelector('a');
                            if (btn) btn.innerHTML = `<span class="material-symbols-outlined text-lg">mail</span> ${col.feedback_button_text}`;
                        }
                    }
                }

                // 9. Fetch supporters
                const sup = await fetchYaml('/_data/partners.yml');
                if (sup) {
                    // It's possible sup is just an object containing `partners` array
                    const supportersArray = sup.partners ? sup.partners : sup;
                    
                    const section = document.querySelector('section#supporters');
                    if (section && sup.section_id) section.id = sup.section_id;

                    if (supportersArray && Array.isArray(supportersArray)) {
                        const supportersContainer = document.querySelector('#supporters-container');
                        if (supportersContainer) {
                            supportersContainer.innerHTML = supportersArray.map(supporter => `
                                <div class="w-full flex items-center justify-center h-44 md:h-52 p-2">
                                    <a href="${supporter.link || '#'}" target="${supporter.link && supporter.link !== '#' ? '_blank' : '_self'}" aria-label="${supporter.name}">
                                        <img src="${supporter.logo}" alt="${supporter.name}" class="max-h-36 md:max-h-44 max-w-full object-contain filter drop-shadow-sm hover:scale-105 transition-transform duration-300">
                                    </a>
                                </div>
                            `).join('');
                        }
                    }
                }

                // 10. Fetch global settings
                const settings = await fetchYaml('/_data/settings.yml');
                if (settings && settings.email) {
                    document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
                        link.href = `mailto:${settings.email}`;
                        if (link.textContent.includes('@')) link.textContent = settings.email;
                    });
                }

            } catch (e) {
"""

new_html = re.sub(r'            try \{.*?            \} catch \(e\) \{', new_script, html, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(new_html)

print("Updated index.html")
