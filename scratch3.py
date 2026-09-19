import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace js-yaml block from `try {` to `} catch (e) {`
js_logic = """            try {
                // Fetch hero section edits
                const heroRes = await fetch('/_data/hero.yml');
                if (heroRes.ok) {
                    const heroText = await heroRes.text();
                    const hero = jsyaml.load(heroText);
                    
                    if (hero.headline) {
                        const h1 = document.querySelector('#about h1');
                        if (h1) h1.innerHTML = hero.headline;
                    }
                    if (hero.body) {
                        const p = document.querySelector('#about p');
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
                                    <span class="w-10 h-10 rounded-2xl bg-pink-200/80 text-brand-darkPink flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-xl">${item.icon}</span>
                                    </span>
                                    <span>${item.text}</span>
                                </div>
                            `).join('');
                        }
                    }
                    
                    const heroBtns = document.querySelectorAll('#about .flex.flex-col a');
                    if (heroBtns.length >= 2) {
                        if (hero.button1_text) heroBtns[0].childNodes[2].nodeValue = " " + hero.button1_text;
                        if (hero.button1_url) heroBtns[0].href = hero.button1_url;
                        if (hero.button2_text) heroBtns[1].childNodes[2].nodeValue = " " + hero.button2_text;
                        if (hero.button2_url) heroBtns[1].href = hero.button2_url;
                    }
                }

                // Fetch comprehensive site content edits
                const contentRes = await fetch('/_data/content.yml');
                if (contentRes.ok) {
                    const contentText = await contentRes.text();
                    const content = jsyaml.load(contentText);

                    // 1. Menu Links
                    if (content.menu_links && Array.isArray(content.menu_links)) {
                        const nav = document.querySelector('header nav');
                        const mobileNav = document.querySelector('#mobile-menu nav');
                        if (nav) {
                            nav.innerHTML = content.menu_links.map(link => 
                                `<a href="${link.url}" class="nav-link hover:text-brand-darkPink transition-colors px-1.5 py-1">${link.label}</a>`
                            ).join('');
                        }
                        if (mobileNav) {
                            mobileNav.innerHTML = content.menu_links.map(link => 
                                `<a href="${link.url}" class="mobile-nav-link hover:text-brand-lightPink transition-colors py-2 border-b border-slate-800">${link.label}</a>`
                            ).join('') + `<a href="mailto:emazerol@stfx.ca" class="mt-2 bg-brand-pink hover:bg-brand-darkPink text-white font-black text-center py-3 rounded-full flex items-center justify-center gap-2"><span class="material-symbols-outlined text-lg">mail</span><span>Contact Us</span></a>`;
                        }
                    }

                    // 2. Creators Section
                    if (content.creators) {
                        const c = content.creators;
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
                            const badgeContainer = document.querySelector('#creators .grid-cols-3');
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
                            const titleEl = document.querySelector('#creators h4');
                            if (titleEl) titleEl.textContent = c.image_title;
                        }
                        if (c.image_caption) {
                            const pEl = document.querySelector('#creators .photo-card p');
                            if (pEl) pEl.textContent = c.image_caption;
                        }
                    }

                    // 3. Teachers Section
                    if (content.teachers) {
                        const t = content.teachers;
                        if (t.title) {
                            const titleEl = document.querySelector('#teachers h2');
                            if (titleEl) titleEl.textContent = t.title;
                        }
                        if (t.body) {
                            const bodyEl = document.querySelector('#teachers .max-w-3xl p');
                            if (bodyEl) bodyEl.textContent = t.body;
                        }
                        if (t.curriculum_title) {
                            const titleEl = document.querySelector('#teachers h3');
                            if (titleEl) titleEl.innerHTML = `<span class="material-symbols-outlined text-brand-pink text-2xl">workspace_premium</span> ${t.curriculum_title}`;
                        }
                        if (t.curriculum_body) {
                            const bodyEl = document.querySelector('#teachers h3 + p');
                            if (bodyEl) bodyEl.innerHTML = t.curriculum_body;
                        }
                        if (t.discussion_questions_title) {
                            const titleEl = document.querySelector('#teachers h4.text-brand-fuschiaText');
                            if (titleEl) titleEl.textContent = t.discussion_questions_title;
                        }
                        if (t.questions && Array.isArray(t.questions)) {
                            const listEl = document.querySelector('#teachers ul');
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
                            const titleEl = document.querySelector('#teachers .lg\\\\:col-span-5 h4');
                            if (titleEl) titleEl.textContent = t.feedback_title;
                        }
                        if (t.feedback_body) {
                            const bodyEl = document.querySelector('#teachers .lg\\\\:col-span-5 h4 + p');
                            if (bodyEl) bodyEl.textContent = t.feedback_body;
                        }
                        if (t.feedback_button_text) {
                            const btn = document.querySelector('#teachers .lg\\\\:col-span-5 a');
                            if (btn) btn.innerHTML = `<span class="material-symbols-outlined text-lg">mail</span> ${t.feedback_button_text}`;
                        }
                        if (t.image) {
                            const img = document.querySelector('#teachers .photo-card img');
                            if (img) img.src = t.image;
                        }
                        if (t.image_caption) {
                            const caption = document.querySelector('#teachers .photo-card .p-4');
                            if (caption) caption.textContent = t.image_caption;
                        }
                    }

                    // 4. Download Section
                    if (content.download) {
                        const d = content.download;
                        if (d.title) {
                            const titleEl = document.querySelector('#download h2');
                            if (titleEl) titleEl.textContent = d.title;
                        }
                        if (d.body) {
                            const bodyEl = document.querySelector('#download .max-w-2xl p');
                            if (bodyEl) bodyEl.textContent = d.body;
                        }
                        if (d.button_label) {
                            const btnSpan = document.querySelector('#download a span:last-child');
                            if (btnSpan) btnSpan.textContent = d.button_label;
                        }
                        if (d.button_url) {
                            const btn = document.querySelector('#download a');
                            if (btn) btn.href = d.button_url;
                        }
                        if (d.printing_tips && Array.isArray(d.printing_tips)) {
                            const listEl = document.querySelector('#download ul');
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
                            const gridEl = document.querySelector('#download .grid.grid-cols-2');
                            if (gridEl) {
                                gridEl.innerHTML = d.materials_needed.map(m => `
                                    <div class="bg-white p-3.5 rounded-3xl border border-pink-200/80 flex items-center gap-2.5 shadow-sm">
                                        <span class="material-symbols-outlined text-brand-pink text-lg">${m.icon}</span> ${m.name}
                                    </div>
                                `).join('');
                            }
                        }
                    }

                    // 5. Research Section
                    if (content.research) {
                        const r = content.research;
                        if (r.title) {
                            const titleEl = document.querySelector('#research h2');
                            if (titleEl) titleEl.textContent = r.title;
                        }
                        if (r.items && Array.isArray(r.items)) {
                            const gridEl = document.querySelector('#research .grid');
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

                    // 6. Tools Section
                    if (content.tools) {
                        const tools = content.tools;
                        if (tools.title) {
                            const titleEl = document.querySelector('#tools h3');
                            if (titleEl) titleEl.textContent = tools.title;
                        }
                        if (tools.body) {
                            const bodyEl = document.querySelector('#tools p');
                            if (bodyEl) bodyEl.textContent = tools.body;
                        }
                        if (tools.button_label) {
                            const btnSpan = document.querySelector('#tools a span:last-child');
                            if (btnSpan) btnSpan.textContent = tools.button_label;
                        }
                        if (tools.button_url) {
                            const btn = document.querySelector('#tools a');
                            if (btn) btn.href = tools.button_url;
                        }
                    }

                    // 7. Partners (Collaborators) Section
                    if (content.collaborators) {
                        const c = content.collaborators;
                        if (c.title) {
                            const titleEl = document.querySelector('#partners h2');
                            if (titleEl) titleEl.textContent = c.title;
                        }
                        if (c.body) {
                            const bodyEl = document.querySelector('#partners .max-w-3xl p');
                            if (bodyEl) bodyEl.textContent = c.body;
                        }
                        if (c.items && Array.isArray(c.items)) {
                            const gridEl = document.querySelector('#partners .grid');
                            if (gridEl) {
                                gridEl.innerHTML = c.items.map(item => `
                                    <div class="bg-white border border-pink-200/80 rounded-3xl p-8 flex flex-col justify-between shadow-sm">
                                        <div>
                                            <div class="w-12 h-12 rounded-2xl bg-brand-pink text-white flex items-center justify-center text-xl font-bold mb-4 shadow-md shadow-pink-200">
                                                <span class="material-symbols-outlined text-2xl">${item.icon}</span>
                                            </div>
                                            <h3 class="text-xl font-bold text-slate-900 mb-2">${item.name}</h3>
                                            <p class="text-sm text-slate-700 leading-relaxed font-medium">${item.description}</p>
                                        </div>
                                    </div>
                                `).join('');
                            }
                        }
                        if (c.feedback_title) {
                            const titleEl = document.querySelector('#partners h4');
                            if (titleEl) titleEl.textContent = c.feedback_title;
                        }
                        if (c.feedback_body) {
                            const bodyEl = document.querySelector('#partners h4 + p');
                            if (bodyEl) bodyEl.textContent = c.feedback_body;
                        }
                        if (c.feedback_button_text) {
                            const btn = document.querySelector('#partners a');
                            if (btn) btn.innerHTML = `<span class="material-symbols-outlined text-lg">mail</span> ${c.feedback_button_text}`;
                        }
                    }
                }

                // Fetch global settings
                const settingsRes = await fetch('/_data/settings.yml');
                if (settingsRes.ok) {
                    const settingsText = await settingsRes.text();
                    const settings = jsyaml.load(settingsText);

                    if (settings.email) {
                        document.querySelectorAll('a[href^="mailto:"]').forEach(link => {
                            link.href = `mailto:${settings.email}`;
                            if (link.textContent.includes('@')) link.textContent = settings.email;
                        });
                    }
                }

                // Fetch supporters
                const supportersRes = await fetch('/_data/partners.yml');
                if (supportersRes.ok) {
                    const supportersText = await supportersRes.text();
                    const supporters = jsyaml.load(supportersText);
                    
                    if (supporters && Array.isArray(supporters)) {
                        const supportersContainer = document.querySelector('#supporters-container');
                        if (supportersContainer) {
                            supportersContainer.innerHTML = supporters.map(supporter => `
                                <div class="w-full flex items-center justify-center h-44 md:h-52 p-2">
                                    <a href="${supporter.link || '#'}" target="${supporter.link && supporter.link !== '#' ? '_blank' : '_self'}" aria-label="${supporter.name}">
                                        <img src="${supporter.logo}" alt="${supporter.name}" class="max-h-36 md:max-h-44 max-w-full object-contain filter drop-shadow-sm hover:scale-105 transition-transform duration-300">
                                    </a>
                                </div>
                            `).join('');
                        }
                    }
                }"""

# Use regex to replace the inner body of the try block
new_content = re.sub(r'            try \{.*?            \} catch \(e\) \{', js_logic + '\n            } catch (e) {', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(new_content)

print("index.html updated")
