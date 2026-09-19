import re

with open('index.html', 'r') as f:
    html = f.read()

# I will systematically replace the known text blocks with empty strings.
# This ensures the HTML structure, classes, and layout remain perfectly intact.

replacements = [
    # Hero
    ("Learning how to maintain your brain through play!", ""),
    ("Lifestyle changes could delay or prevent 45% of cognitive impairment, but the general public is typically not aware of this potential. We co-created the Maintaining Brains Game to share research on strategies to maintain and improve brain health!", ""),
    ("Hands-on Straw & Pipe Cleaner Brain Models", ""),
    ("Cognitive Resilience & Strategy Cards", ""),
    ("Co-Created with Lived Experience & Educators", ""),
    ("Trauma-Informed & Strengths-Based Care", ""),
    (">Download Game Materials<", "><"),
    (">For Teachers & Curriculum<", "><"),
    
    # Creators
    ("How The Game Was Created", ""),
    ("We co-created our initial draft, the Maintain Your Brain Game, at a workshop funded by the Canadian Institutes of Health Research (CIHR). The workshop brought together people with lived experience of cognitive impairment, Indigenous educators, South Asian educators, healthcare providers, and academic researchers.", ""),
    ("Since then, we co-created Maintaining Brains with high school teachers and the national youth-serving organization, Actua. This youth-focused version incorporates trauma-informed principles of agency, strengths-based approaches, and safe environments.", ""),
    (">Workshop Grant<", "><"),
    (">STEM Outreach<", "><"),
    (">Informed Design<", "><"),
    (">CIHR<", "><"),
    (">Actua<", "><"),
    (">Trauma<", "><"),
    ("Co-Creators at Toronto Workshop", ""),
    ("Collaborative development with educators, clinicians, and individuals with lived experience.", ""),

    # Teachers
    ("For Educators & Teachers", ""),
    ("The Maintaining Brains Game provides educators with an engaging way to introduce students to concepts related to brain health, cognition, and lifelong wellness.", ""),
    ("Curriculum Outcomes Alignment", ""),
    ("We reviewed English program Nova Scotia curriculum outcomes and guidelines to identify specific outcomes that the Maintaining Brains Game helps achieve in high school science, health, and psychology classes.", ""),
    ("Student Discussion Questions (Created by IB Psychology Students)", ""),
    ("Why is it important to think about brain health throughout life?", ""),
    ("How do everyday lifestyle choices influence cognitive wellness and reserve?", ""),
    ("What is one thing you learned that you can apply in your own daily life?", ""),
    ("How can communities support healthy aging and brain resilience?", ""),
    ("Are you a teacher using the game?", ""),
    ("If you use Maintaining Brains in your classroom outside Nova Scotia, we'd love to hear how it went!", ""),
    (">Contact Us with Feedback<", "><"),
    ("X-Chem STEM Outreach Session at Dr. John Hugh Gillis High School", ""),

    # Download
    ("Everything you need to facilitate and play the Maintaining Brains Game in your classroom or community group. Download complete PDF card packages and instruction sheets.", ""),
    (">Download Game Package<", "><"),
    ("Print on white, blue, or yellow paper matching the filename color code.", ""),
    ("Files include full crop marks and bleeds for professional laser cutters.", ""),
    ("Recommended paper weight: 65 - 90 lb cardstock.", ""),
    ("Laminating increases durability, though cards become thicker to handle.", ""),
    (">Plastic Straws<", "><"),
    (">Pipe Cleaners<", "><"),
    (">Glass Marbles<", "><"),
    (">Face Masks<", "><"),

    # Research
    ("Research & Publications", ""),
    ("Conference Poster • Canadian Association for Neuroscience", ""),
    ("Improving brain health literacy among adolescents: The Maintain Your Brain Game", ""),
    ("Shaw-Peters L, MacLellan M, Monaghan J, Gilroy-Dreher S, Harrison L, MacGillivray M, Berrigan LI, Gawryluk JR, Phelps J, Fitzgibbon-Collins LK, Mazerolle EL (2026). Montreal, Canada.", ""),
    (">Download Conference Poster →<", "><"),
    ("Honours Thesis • StFX Psychology", ""),
    ("Maintain your Brain: Co-creating and evaluating a game to teach adolescent audiences about cognitive reserve", ""),
    ("Lydia Shaw-Peters (2026). Honours Thesis, Department of Psychology, St. Francis Xavier University.", ""),
    (">Download Honours Thesis →<", "><"),

    # Tools
    ("Tool To Create Custom Game Cards", ""),
    ("Want to make your own custom version of the Maintaining Brains Game or populate card templates directly from a spreadsheet? Use our open-source generator tool!", ""),
    (">Open Card Generator Tool<", "><"),

    # Partners
    ("Our Partners", ""),
    ("We love working with partners to co-create and evaluate customized versions of the Maintaining Brains Game for their audiences!", ""),
    (">Canada's leading STEM outreach organization, collaborating to bring youth-focused brain health literacy to nationwide camps.<", "><"),
    (">Based at StFX, bringing hands-on neuroscience workshops and game trials directly into local elementary and high schools.<", "><"),
    (">Located in Antigonish, NS, collaborating on IB Psychology classroom testing and student discussion frameworks.<", "><"),
    ("Dr. John Hugh Gillis Regional High School", ""),
    ("X-Chem STEM Outreach", ""),
    ("Have you made a custom version of the game?", ""),
    ("We'd love to hear how your students or community group used the game!", ""),
    (">Let Us Know<", "><")
]

# We must be careful because "Download Game Materials" appears multiple times (like the ID, or other places).
# We'll use a specific replacement for the header.
html = html.replace('<h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-3">Download Game Materials</h2>', '<h2 class="text-3xl md:text-4xl font-extrabold text-slate-900 mb-3"></h2>')

for old, new in replacements:
    html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
print("Placeholders removed.")
