import json

# 1. Create individual YAML files manually
files = {
    "_data/menu.yml": """menu_links:
  - label: Home
    url: '#about'
  - label: Creators
    url: '#creators'
  - label: For Teachers
    url: '#teachers'
  - label: Download
    url: '#download'
  - label: Research
    url: '#research'
  - label: Tools
    url: '#tools'
  - label: Partners
    url: '#partners'
""",
    "_data/creators.yml": """section_id: creators
title: How The Game Was Created
p1: We co-created our initial draft, the Maintain Your Brain Game, at a workshop funded by the Canadian Institutes of Health Research (CIHR). The workshop brought together people with lived experience of cognitive impairment, Indigenous educators, South Asian educators, healthcare providers, and academic researchers.
p2: Since then, we co-created Maintaining Brains with high school teachers and the national youth-serving organization, Actua. This youth-focused version incorporates trauma-informed principles of agency, strengths-based approaches, and safe environments.
image: assets/images/real/Workshop-1-2.jpeg
focal_point: object-center
badges:
  - title: CIHR
    subtitle: Workshop Grant
  - title: Actua
    subtitle: STEM Outreach
  - title: Trauma
    subtitle: Informed Design
image_title: Co-Creators at Toronto Workshop
image_caption: Collaborative development with educators, clinicians, and individuals with lived experience.
""",
    "_data/teachers.yml": """section_id: teachers
title: For Educators & Teachers
body: The Maintaining Brains Game provides educators with an engaging way to introduce students to concepts related to brain health, cognition, and lifelong wellness.
curriculum_title: Curriculum Outcomes Alignment
curriculum_body: We reviewed English program Nova Scotia curriculum outcomes and guidelines to identify specific outcomes that the Maintaining Brains Game helps achieve in high school science, health, and psychology classes.
discussion_questions_title: Student Discussion Questions (Created by IB Psychology Students)
questions:
  - question: Why is it important to think about brain health throughout life?
  - question: How do everyday lifestyle choices influence cognitive wellness and reserve?
  - question: What is one thing you learned that you can apply in your own daily life?
  - question: How can communities support healthy aging and brain resilience?
feedback_title: Are you a teacher using the game?
feedback_body: If you use Maintaining Brains in your classroom outside Nova Scotia, we'd love to hear how it went!
feedback_button_text: Contact Us with Feedback
image: assets/images/real/X-Chem-1-2xl.jpeg
image_caption: X-Chem STEM Outreach Session at Dr. John Hugh Gillis High School
""",
    "_data/download.yml": """section_id: download
title: Download Game Materials
body: Everything you need to facilitate and play the Maintaining Brains Game in your classroom or community group. Download complete PDF card packages and instruction sheets.
button_label: Download Game Package
button_url: '#'
printing_tips:
  - tip: Print on white, blue, or yellow paper matching the filename color code.
  - tip: Files include full crop marks and bleeds for professional laser cutters.
  - tip: Recommended paper weight: 65 - 90 lb cardstock.
  - tip: Laminating increases durability, though cards become thicker to handle.
materials_needed:
  - icon: science
    name: Plastic Straws
  - icon: hub
    name: Pipe Cleaners
  - icon: circle
    name: Glass Marbles
  - icon: masks
    name: Face Masks
""",
    "_data/research.yml": """section_id: research
title: Research & Publications
items:
  - category: Conference Poster • Canadian Association for Neuroscience
    title: 'Improving brain health literacy among adolescents: The Maintain Your Brain Game'
    authors: Shaw-Peters L, MacLellan M, Monaghan J, Gilroy-Dreher S, Harrison L, MacGillivray M, Berrigan LI, Gawryluk JR, Phelps J, Fitzgibbon-Collins LK, Mazerolle EL (2026). Montreal, Canada.
    link_text: Download Conference Poster →
    link_url: https://www.maintainingbrains.ca/research.html
  - category: Honours Thesis • StFX Psychology
    title: 'Maintain your Brain: Co-creating and evaluating a game to teach adolescent audiences about cognitive reserve'
    authors: Lydia Shaw-Peters (2026). Honours Thesis, Department of Psychology, St. Francis Xavier University.
    link_text: Download Honours Thesis →
    link_url: https://www.maintainingbrains.ca/research.html
""",
    "_data/tools.yml": """section_id: tools
title: Tool To Create Custom Game Cards
body: Want to make your own custom version of the Maintaining Brains Game or populate card templates directly from a spreadsheet? Use our open-source generator tool!
button_label: Open Card Generator Tool
button_url: https://www.maintainingbrains.ca/tools.html
""",
    "_data/collaborators.yml": """section_id: partners
title: Our Partners
body: We love working with partners to co-create and evaluate customized versions of the Maintaining Brains Game for their audiences!
items:
  - icon: groups
    name: Actua
    description: Canada's leading STEM outreach organization, collaborating to bring youth-focused brain health literacy to nationwide camps.
  - icon: biotech
    name: X-Chem STEM Outreach
    description: Based at StFX, bringing hands-on neuroscience workshops and game trials directly into local elementary and high schools.
  - icon: school
    name: Dr. John Hugh Gillis Regional High School
    description: Located in Antigonish, NS, collaborating on IB Psychology classroom testing and student discussion frameworks.
feedback_title: Have you made a custom version of the game?
feedback_body: We'd love to hear how your students or community group used the game!
feedback_button_text: Let Us Know
"""
}

import os
for path, text in files.items():
    with open(path, "w") as f:
        f.write(text)

if os.path.exists('_data/content.yml'):
    os.remove('_data/content.yml')

# Fix hero.yml
with open('_data/hero.yml', 'r') as f:
    hero = f.read()
if 'section_id:' not in hero:
    hero = "section_id: about\n" + hero
with open('_data/hero.yml', 'w') as f:
    f.write(hero)

# Fix partners.yml
with open('_data/partners.yml', 'r') as f:
    partners = f.read()
if 'section_id:' not in partners:
    # it's just a list, make it a map
    partners = "section_id: supporters\npartners:\n" + partners.replace("- name:", "  - name:")
    partners = partners.replace("  logo:", "    logo:").replace("  link:", "    link:")
with open('_data/partners.yml', 'w') as f:
    f.write(partners)

print("Split complete")
