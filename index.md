---
layout: default
title: Home
---

<!-- Hero Section -->
<section id="about" class="relative pt-32 pb-20 md:pt-40 md:pb-28 hero-gradient text-white overflow-hidden">
    <div class="max-w-7xl mx-auto px-6 relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
            <div class="lg:col-span-7 text-center lg:text-left">

                <h1 class="text-4xl md:text-6xl font-black tracking-tight mb-6 leading-tight">
                    Learning how to <span class="text-transparent bg-clip-text bg-gradient-to-r from-pink-200 via-amber-200 to-white">maintain your brain</span> through play!
                </h1>
                
                <p class="text-lg md:text-xl text-pink-100 max-w-2xl mb-8 font-medium leading-relaxed">
                    Lifestyle changes could delay or prevent <strong class="text-white underline decoration-brand-pink decoration-4">45% of cognitive impairment</strong>, but the general public is typically not aware of this potential. We co-created the <strong>Maintaining Brains Game</strong> to bridge this gap!
                </p>

                <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-4">
                    <a href="#gallery" class="w-full sm:w-auto bg-white text-brand-darkPink font-extrabold px-8 py-4 rounded-full shadow-xl hover:bg-pink-50 transition-all flex items-center justify-center gap-2 hover:scale-105">
                        <i class="fa-solid fa-images"></i>
                        View Photo Gallery
                    </a>
                    <a href="#game-details" class="w-full sm:w-auto border-2 border-white/80 hover:border-white text-white font-bold px-8 py-4 rounded-full backdrop-blur-sm hover:bg-white/10 transition-all flex items-center justify-center gap-2">
                        <i class="fa-solid fa-dice"></i>
                        How To Play
                    </a>
                </div>
            </div>

            <div class="lg:col-span-5 relative">
                <div class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white/20 group">
                    <img src="{{ site.data.photos[0].image | relative_url }}" alt="{{ site.data.photos[0].title }}" class="w-full h-auto object-cover group-hover:scale-105 transition-transform duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent flex items-end p-6">
                        <p class="text-xs text-slate-200 font-semibold">
                            <i class="fa-solid fa-camera mr-1 text-brand-pink"></i> Real Workshop Photo: Children engaged with the tabletop brain model.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Game Overview Section -->
<section id="game-details" class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-6">
        <div class="max-w-3xl mx-auto text-center mb-16">
            <span class="text-brand-pink font-extrabold text-xs uppercase tracking-widest block mb-2">Tabletop Game Experience</span>
            <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900">How The Maintaining Brains Game Works</h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-pink-50/60 border border-pink-100 rounded-3xl p-8 text-center flex flex-col items-center">
                <div class="w-16 h-16 rounded-2xl bg-brand-pink text-white flex items-center justify-center text-2xl font-bold mb-6 shadow-md shadow-pink-200">
                    <i class="fa-solid fa-user-doctor"></i>
                </div>
                <h3 class="text-xl font-bold text-slate-900 mb-3">Roleplay Healthcare Providers</h3>
                <p class="text-slate-600 text-sm leading-relaxed">
                    In small groups, players step into the shoes of healthcare providers directly caring for and making vital decisions for their patient's brain health.
                </p>
            </div>

            <div class="bg-pink-50/60 border border-pink-100 rounded-3xl p-8 text-center flex flex-col items-center">
                <div class="w-16 h-16 rounded-2xl bg-brand-pink text-white flex items-center justify-center text-2xl font-bold mb-6 shadow-md shadow-pink-200">
                    <i class="fa-solid fa-cubes-stacked"></i>
                </div>
                <h3 class="text-xl font-bold text-slate-900 mb-3">Build Brain Structures</h3>
                <p class="text-slate-600 text-sm leading-relaxed">
                    Players construct a physical brain model using plastic straws and pipe cleaners, symbolizing brain structural integrity and neural connections.
                </p>
            </div>

            <div class="bg-pink-50/60 border border-pink-100 rounded-3xl p-8 text-center flex flex-col items-center">
                <div class="w-16 h-16 rounded-2xl bg-brand-pink text-white flex items-center justify-center text-2xl font-bold mb-6 shadow-md shadow-pink-200">
                    <i class="fa-solid fa-shield-heart"></i>
                </div>
                <h3 class="text-xl font-bold text-slate-900 mb-3">Draw Resilience Cards</h3>
                <p class="text-slate-600 text-sm leading-relaxed">
                    Drawing lifestyle & event cards determines patient resilience. The game is memorable and encourages real-world healthy lifestyle decisions!
                </p>
            </div>
        </div>
    </div>
</section>

<!-- Dynamic Photo Gallery (Looping over _data/photos.yml) -->
<section id="gallery" class="py-24 bg-brand-bgLight border-y border-pink-100">
    <div class="max-w-7xl mx-auto px-6">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-12">
            <div>
                <span class="text-brand-pink font-extrabold text-xs uppercase tracking-widest block mb-2">Authentic Gallery</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-slate-900">Photos from maintainingbrains.ca</h2>
            </div>
            <p class="text-slate-600 max-w-md mt-4 md:mt-0 text-sm font-medium">
                Managed easily via Decap CMS or editing <code>_data/photos.yml</code>.
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            {% for item in site.data.photos %}
            <div class="photo-card rounded-3xl overflow-hidden bg-white border border-pink-100 shadow-sm flex flex-col group">
                <div class="relative overflow-hidden aspect-[4/3]">
                    <img src="{{ item.image | relative_url }}" alt="{{ item.title }}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    <span class="absolute top-4 left-4 bg-brand-pink text-white text-xs font-bold px-3 py-1 rounded-full shadow-md">{{ item.category }}</span>
                </div>
                <div class="p-6">
                    <h3 class="font-bold text-lg text-slate-900 mb-2">{{ item.title }}</h3>
                    <p class="text-sm text-slate-600 leading-relaxed">
                        {{ item.description }}
                    </p>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</section>

<!-- Dynamic Institutional Partners (Looping over _data/partners.yml) -->
<section id="partners" class="py-20 bg-white">
    <div class="max-w-7xl mx-auto px-6 text-center">
        <span class="text-brand-pink font-extrabold text-xs uppercase tracking-widest block mb-2">Institutional Support</span>
        <h2 class="text-3xl font-extrabold text-slate-900 mb-12">Supported By Our Research Partners</h2>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 items-center justify-items-center opacity-90 hover:opacity-100 transition-opacity">
            {% for partner in site.data.partners %}
            <a href="{{ partner.link }}" target="_blank" class="p-6 bg-slate-50 border border-slate-100 rounded-2xl w-full flex items-center justify-center h-32 hover:border-pink-200 transition-colors">
                <img src="{{ partner.logo | relative_url }}" alt="{{ partner.name }}" class="max-h-20 object-contain">
            </a>
            {% endfor %}
        </div>
    </div>
</section>
