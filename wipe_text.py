with open("index.html", "r") as f:
    html = f.read()

replacements = [
    ("Learning how to maintain your brain through play!", ""),
    ("Lifestyle changes could delay or prevent 45% of cognitive impairment, but the general public is typically not aware of this potential. We co-created the Maintaining Brains Game to share research on strategies to maintain and improve brain health!", ""),
    ("How The Game Was Created", ""),
    ("We co-created our initial draft, the Maintain Your Brain Game, at a workshop funded by the Canadian Institutes of Health Research (CIHR). The workshop brought together people with lived experience of cognitive impairment, Indigenous educators, South Asian educators, healthcare providers, and academic researchers.", ""),
    ("Since then, we co-created Maintaining Brains with high school teachers and the national youth-serving organization, Actua. This youth-focused version incorporates trauma-informed principles of agency, strengths-based approaches, and safe environments.", ""),
    ("For Educators & Teachers", ""),
    ("The Maintaining Brains Game provides educators with an engaging way to introduce students to concepts related to brain health, cognition, and lifelong wellness.", ""),
    ("Curriculum Outcomes Alignment", ""),
    ("We reviewed English program Nova Scotia curriculum outcomes and guidelines to identify specific outcomes that the Maintaining Brains Game helps achieve in high school science, health, and psychology classes.", ""),
    ("Student Discussion Questions (Created by IB Psychology Students)", ""),
    ("Download Game Materials", ""),
    ("Everything you need to facilitate and play the Maintaining Brains Game in your classroom or community group. Download complete PDF card packages and instruction sheets.", ""),
    ("Research & Publications", ""),
    ("Tool To Create Custom Game Cards", ""),
    ("Want to make your own custom version of the Maintaining Brains Game or populate card templates directly from a spreadsheet? Use our open-source generator tool!", ""),
    ("Our Partners", ""),
    ("We love working with partners to co-create and evaluate customized versions of the Maintaining Brains Game for their audiences!", ""),
    ("Have you made a custom version of the game?", ""),
    ("We'd love to hear how your students or community group used the game!", ""),
    (">Contact Us<", "><"),
    (">Download Game Package<", "><"),
    (">Open Card Generator Tool<", "><")
]

for old, new in replacements:
    html = html.replace(old, new)

with open("index.html", "w") as f:
    f.write(html)
