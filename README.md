# Maintaining Brains Website Template & CMS Guide

Welcome to the **GitHub Pages + Decap CMS Template** for `maintainingbrains.ca`.

---

## 📂 Repository Structure

```
├── _config.yml               # Global site configuration (Lab email, StFX colors)
├── _data/
│   ├── photos.yml            # Manage gallery photos, titles, and descriptions
│   └── partners.yml          # Manage institutional logos and links
├── _layouts/
│   └── default.html          # Main HTML structure with Tailwind CSS & navigation
├── _posts/                   # News and research updates (Markdown files)
├── admin/
│   ├── index.html            # Decap CMS Admin dashboard entry point
│   └── config.yml            # CMS collections setup
├── assets/
│   ├── images/gallery/       # High-res workshop photos
│   └── images/logos/         # Institutional partner logos
└── index.md                  # Main homepage template
```

---

## 👩‍💻 How Humans Can Update Content

### Option A: Using the Decap CMS Admin Panel (No Coding Required)
1. Go to `https://maintainingbrains.ca/admin/` in your browser.
2. Sign in with your GitHub account.
3. Select **Photo Gallery** to upload new photos, update captions, or reorder gallery items.
4. Select **Institutional Partners** to add or replace sponsor logos.
5. Select **News & Research Updates** to publish new articles.
6. Click **Publish**. GitHub Pages will rebuild and update your site automatically!

---

### Option B: Editing Directly on GitHub.com
- To add a new photo: Upload the image to `assets/images/gallery/` and add an entry into `_data/photos.yml`.
- To update lab details: Edit `_config.yml`.
