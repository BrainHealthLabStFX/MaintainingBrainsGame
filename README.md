# Maintaining Brains Website — Project Documentation & Maintenance Guide

Welcome to the official repository for **Maintaining Brains** (`maintainingbrains.ca`), an interactive, evidence-based learning tool created by the Mazerolle Lab at St. Francis Xavier University (StFX).

---

## 💡 1. Site Architecture & Conceptualization

The site is built as a lightweight, ultra-fast **Single-Page Application (SPA)** with a decoupled content architecture powered by **Sveltia CMS** and **GitHub Pages**.

### Core Technical Pillars:
* **Single-Page Responsive Layout (`index.html`):** Built with **Tailwind CSS**, **Google Material Symbols**, and **FontAwesome**.
* **Decoupled Data Store (`_data/*.yml`):** All site content (copy, headlines, lists, images, navigation links, and settings) is stored cleanly in 12 structured YAML data files.
* **Dual-Layer Rendering System:**
  1. **Static HTML Fallback:** Hardcoded HTML in `index.html` guarantees instant rendering and SEO indexing before JavaScript executes.
  2. **Dynamic Client-Side Hydration (`fetchYaml` + `js-yaml`):** On page load, client-side JavaScript fetches `_data/*.yml` with cache-busting timestamps (`?t=timestamp`) to dynamically update DOM text and image elements live.
* **Subpath & Custom Domain Resiliency:** All asset fetching and image helper functions (`fixImg`, `cleanUrl`) use subfolder-resilient relative paths (`./_data/`, `./assets/`), enabling seamless deployment on GitHub Pages (`/MaintainingBrainsGame/`), custom root domains (`maintainingbrains.ca`), or local offline previews.

---

## 📂 2. Repository Structure

```
├── .github/
│   └── workflows/
│       └── sync-fallbacks.yml    # GitHub Action to auto-sync index.html fallbacks when _data/ updates
├── _data/                        # Structured CMS content files
│   ├── attribution.yml           # Footer Creative Commons license text & icons
│   ├── collaborators.yml         # Section 6: Partners cards (Actua, X-Chem, High School)
│   ├── configuration.yml         # Site protection & favicon settings
│   ├── creators.yml              # Section 1: How the Game Was Created (CIHR, Actua)
│   ├── customize.yml            # Section 4: Easy to Customize card generator section
│   ├── download.yml             # Section 3: Play The Game, printing tips & required materials
│   ├── educators.yml            # Section 2: For Educators & curriculum alignment
│   ├── hero.yml                 # Main Banner headline, body, buttons & highlights strip
│   ├── menu.yml                 # Header navigation menu links
│   ├── partners.yml             # Section 7: Supporter organization logos & website links
│   ├── research.yml             # Section 5: Research publications & honours thesis cards
│   └── settings.yml             # Footer contact details (Email, Department, Institution, Location)
├── admin/
│   ├── config.yml               # Sveltia CMS collection schemas & field definitions
│   └── index.html               # Sveltia CMS Single Page Admin Panel entry point
├── assets/
│   └── images/                  # All site visual assets
│       ├── gallery/             # Workshop event photos
│       ├── logos/               # Institutional partner logos (CIHR, StFX, ResearchNS, VAST)
│       ├── real/                # High-res activity photos
│       └── uploads/             # User-uploaded CMS media & favicons
├── scripts/
│   └── sync_fallbacks.py        # Python script that syncs index.html fallbacks with _data/*.yml
├── .gitignore                   # Excludes system files (.DS_Store)
├── .nojekyll                    # Instructs GitHub Pages to serve _data/ raw files without Jekyll
└── index.html                   # Main website HTML structure & hydration script
```

---

## 👩‍💻 3. How to Edit & Manage Content

### Option A: Using Sveltia CMS Admin Panel (No Coding Required)
1. Navigate to **`https://maintainingbrains.ca/admin/`** (or `https://brainhealthlabstfx.github.io/MaintainingBrainsGame/admin/`).
2. Log in using your **GitHub account**.
3. Select any collection from the left sidebar:
   * **Banner (Hero):** Update main headline, body text, action buttons, or highlights strip text.
   * **Creators / About:** Edit workshop origin story, CIHR/Actua badges, and photo captions.
   * **Educators:** Edit curriculum alignment text, IB Psychology student discussion questions, or contact info.
   * **Play The Game (Download):** Edit card deck download links, printing guidelines, and required materials.
   * **Customize:** Edit the card generator tool description and hyperlink text.
   * **Research:** Add, remove, or edit conference posters and honours thesis publications.
   * **Partners:** Manage partner organization cards.
   * **Supporters:** Upload or update sponsor logos (CIHR, StFX, ResearchNS, VAST) and website links.
   * **Header Navigation / Footer Contact / Attribution:** Customize nav menu order, lab email, or license info.
4. Click **Publish**. Sveltia will commit the change directly to GitHub `main` branch.

#### 🎨 Rich Text & Formatting Tips in CMS:
* **Gradient Text in Headline:** Wrapping text in `<span class="text-transparent bg-clip-text bg-gradient-to-r from-pink-200 via-amber-200 to-white">your text</span>` creates the signature pink-to-white gradient text.
* **Inline Hyperlinks:** Standard HTML links like `<a href="mailto:emazerol@stfx.ca" class="text-brand-pink hover:text-brand-darkPink hover:underline font-bold transition-colors">get in touch!</a>` are fully supported.
* **Multiple Paragraphs:** In multiline text fields, pressing `Enter` twice creates distinct, formatted paragraphs automatically.

---

### Option B: Editing Directly on GitHub
1. Navigate to the `_data/` folder on GitHub.
2. Edit any `.yml` file directly in the browser and click **Commit changes**.

---

## ⚙️ 4. Maintenance & Configuration Notables

### 🖼️ Sveltia Media Manager Integration
* In `admin/config.yml`, `media_folder: "assets/images"` is mapped to the root image directory.
* This allows the Sveltia Media Manager to scan and display all images across `/real`, `/logos`, `/gallery`, and `/uploads`.

### 🔄 Auto-Syncing Static HTML Fallbacks
* Whenever a file in `_data/*.yml` is modified, the GitHub Action (`.github/workflows/sync-fallbacks.yml`) automatically triggers `scripts/sync_fallbacks.py`.
* The script synchronizes the hardcoded static HTML elements in `index.html` with the new YAML content, ensuring visitors with slow connections or disabled JS still see up-to-date content.

### 🚫 `.nojekyll` File
* The `.nojekyll` file in the root folder is **critical**. It prevents GitHub Pages from running Jekyll builds, ensuring that raw `_data/*.yml` files are served over HTTP with `200 OK` status for client-side JS hydration.

### 🎨 Visual Rhythm & Section Zebra Striping
The page maintains a clean visual rhythm alternating background colors:
* **Hero Section:** Deep Fuschia Gradient (`hero-gradient`)
* **Highlights Strip:** Playful Light Pink Gradient
* **About:** White (`bg-white`)
* **Educators:** Soft Pink Light (`bg-brand-bgLight`)
* **Download:** White (`bg-white`)
* **Customize:** Soft Pink Light (`bg-brand-bgLight`)
* **Research:** White (`bg-white`)
* **Partners:** Soft Pink Light (`bg-brand-bgLight`)
* **Supporters:** White (`bg-white`)
* **Footer:** Deep Fuschia Gradient (`footer-gradient`)
