const fs = require('fs');

const heroYml = fs.readFileSync('_data/hero.yml', 'utf8');
const contentYml = fs.readFileSync('_data/content.yml', 'utf8');

// just append since yaml allows appending at the end for objects
fs.appendFileSync('_data/hero.yml', `button1_text: "Download Game Materials"
button1_url: "#download"
button2_text: "For Teachers & Curriculum"
button2_url: "#teachers"
`);

fs.appendFileSync('_data/content.yml', `  badges:
    - title: "CIHR"
      subtitle: "Workshop Grant"
    - title: "Actua"
      subtitle: "STEM Outreach"
    - title: "Trauma"
      subtitle: "Informed Design"
  image_title: "Co-Creators at Toronto Workshop"
  image_caption: "Collaborative development with educators, clinicians, and individuals with lived experience."

# Let's use sed instead for specific sections, or just rewrite the whole file
`);
