// Initialize HTM with React's createElement (which Sveltia aliases to 'h')
const html = htm.bind(h);

const HeroPreview = createClass({
    componentDidMount() {
        // Inject Tailwind into the preview iframe
        const iframeDocument = this.props.document;
        if (!iframeDocument.getElementById('tailwind-script')) {
            const script = iframeDocument.createElement('script');
            script.id = 'tailwind-script';
            script.src = 'https://cdn.tailwindcss.com';
            iframeDocument.head.appendChild(script);

            const configScript = iframeDocument.createElement('script');
            configScript.innerHTML = `
                tailwind.config = {
                    theme: {
                        extend: {
                            fontFamily: { sans: ['"Plus Jakarta Sans"', 'sans-serif'] },
                            colors: {
                                brand: { pink: '#D25299', darkPink: '#942663', lightPink: '#e18cbb', bgLight: '#FDF7FA' }
                            }
                        }
                    }
                }
            `;
            iframeDocument.head.appendChild(configScript);
            
            const fontLink = iframeDocument.createElement('link');
            fontLink.rel = 'stylesheet';
            fontLink.href = 'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap';
            iframeDocument.head.appendChild(fontLink);
            
            const iconsLink = iframeDocument.createElement('link');
            iconsLink.rel = 'stylesheet';
            iconsLink.href = 'https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0';
            iframeDocument.head.appendChild(iconsLink);

            const customCss = iframeDocument.createElement('style');
            customCss.innerHTML = `
                .hero-gradient { background: linear-gradient(135deg, #002A5C 0%, #4A154B 50%, #D25299 100%); }
                .material-symbols-outlined { vertical-align: middle; }
            `;
            iframeDocument.head.appendChild(customCss);
        }
    },

    render() {
        const { entry, getAsset } = this.props;
        const data = entry.get('data').toJS();
        
        const image = data.image ? getAsset(data.image) : null;
        const imageUrl = image ? image.url : '';
        
        const highlights = data.highlights || [];

        return html`
            <div class="bg-slate-50 text-slate-800 font-sans antialiased min-h-screen">
                <section class="relative pt-20 pb-20 hero-gradient text-white overflow-hidden">
                    <div class="max-w-7xl mx-auto px-6 relative z-10">
                        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                            <div class="lg:col-span-7 text-left">
                                <h1 class="text-4xl md:text-6xl font-black tracking-tight mb-6 leading-tight" dangerouslySetInnerHTML=${{__html: data.headline || ''}}></h1>
                                
                                <p class="text-lg md:text-xl text-pink-100 max-w-2xl mb-8 font-medium leading-relaxed" dangerouslySetInnerHTML=${{__html: data.body || ''}}></p>

                                <div class="flex flex-col sm:flex-row items-center justify-start gap-4">
                                    ${data.button1_text ? html`
                                        <a href="#" class="w-full sm:w-auto bg-white text-brand-darkPink font-black px-8 py-4 rounded-full shadow-xl flex items-center justify-center gap-2">
                                            <span class="material-symbols-outlined text-xl">download</span>
                                            ${data.button1_text}
                                        </a>
                                    ` : ''}
                                    ${data.button2_text ? html`
                                        <a href="#" class="w-full sm:w-auto border-2 border-white/80 text-white font-extrabold px-8 py-4 rounded-full flex items-center justify-center gap-2">
                                            <span class="material-symbols-outlined text-xl">school</span>
                                            ${data.button2_text}
                                        </a>
                                    ` : ''}
                                </div>
                            </div>

                            <div class="lg:col-span-5 relative">
                                ${imageUrl ? html`
                                    <div class="relative rounded-3xl overflow-hidden shadow-2xl border-4 border-white/20">
                                        <img src=${imageUrl} class="w-full h-auto object-cover ${data.focal_point || 'object-center'}" />
                                    </div>
                                ` : ''}
                            </div>
                        </div>
                    </div>
                </section>

                <section class="bg-gradient-to-r from-pink-100 via-pink-50 to-pink-100 border-y border-pink-200/70 py-6 text-left">
                    <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-6 text-pink-950 text-xs md:text-sm font-extrabold">
                        ${highlights.map(item => html`
                            <div class="flex items-center gap-3">
                                ${item.icon ? html`
                                    <span class="w-10 h-10 rounded-2xl bg-pink-200/80 text-brand-darkPink flex items-center justify-center shrink-0">
                                        <span class="material-symbols-outlined text-xl">${item.icon}</span>
                                    </span>
                                ` : ''}
                                <span>${item.text}</span>
                            </div>
                        `)}
                    </div>
                </section>
            </div>
        `;
    }
});

CMS.registerPreviewTemplate('hero_data', HeroPreview);
