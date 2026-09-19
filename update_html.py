with open("index.html", "r") as f:
    content = f.read()

# Highlights replacement
content = content.replace("""
                                <div class="flex items-center gap-3">
                                    <span class="w-10 h-10 rounded-2xl bg-pink-200/80 text-brand-darkPink flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-xl">${item.icon}</span>
                                    </span>
                                    <span>${item.text}</span>
                                </div>""", """
                                <div class="flex items-center gap-3">
                                    ${item.icon ? `<span class="w-10 h-10 rounded-2xl bg-pink-200/80 text-brand-darkPink flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-xl">${item.icon}</span>
                                    </span>` : ''}
                                    <span>${item.text}</span>
                                </div>""")

# Materials replacement
content = content.replace("""
                                    <div class="bg-white p-3.5 rounded-3xl border border-pink-200/80 flex items-center gap-2.5 shadow-sm">
                                        <span class="material-symbols-outlined text-brand-pink text-lg">${m.icon}</span> ${m.name}
                                    </div>""", """
                                    <div class="bg-white p-3.5 rounded-3xl border border-pink-200/80 flex items-center gap-2.5 shadow-sm">
                                        ${m.icon ? `<span class="material-symbols-outlined text-brand-pink text-lg">${m.icon}</span> ` : ''}${m.name}
                                    </div>""")

# Collaborators replacement
content = content.replace("""
                                        <div>
                                            <div class="w-12 h-12 rounded-2xl bg-brand-pink text-white flex items-center justify-center text-xl font-bold mb-4 shadow-md shadow-pink-200">
                                                <span class="material-symbols-outlined text-2xl">${item.icon}</span>
                                            </div>
                                            <h3 class="text-xl font-bold text-slate-900 mb-2">${item.name}</h3>""", """
                                        <div>
                                            ${item.icon ? `<div class="w-12 h-12 rounded-2xl bg-brand-pink text-white flex items-center justify-center text-xl font-bold mb-4 shadow-md shadow-pink-200">
                                                <span class="material-symbols-outlined text-2xl">${item.icon}</span>
                                            </div>` : ''}
                                            <h3 class="text-xl font-bold text-slate-900 mb-2">${item.name}</h3>""")

with open("index.html", "w") as f:
    f.write(content)
