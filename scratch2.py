import re

with open('_data/hero.yml', 'a') as f:
    f.write('button1_text: "Download Game Materials"\n')
    f.write('button1_url: "#download"\n')
    f.write('button2_text: "For Teachers & Curriculum"\n')
    f.write('button2_url: "#teachers"\n')

with open('_data/content.yml', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if line.startswith('  focal_point:'):
        new_lines.append('  badges:\n')
        new_lines.append('    - title: "CIHR"\n')
        new_lines.append('      subtitle: "Workshop Grant"\n')
        new_lines.append('    - title: "Actua"\n')
        new_lines.append('      subtitle: "STEM Outreach"\n')
        new_lines.append('    - title: "Trauma"\n')
        new_lines.append('      subtitle: "Informed Design"\n')
        new_lines.append('  image_title: "Co-Creators at Toronto Workshop"\n')
        new_lines.append('  image_caption: "Collaborative development with educators, clinicians, and individuals with lived experience."\n')
    
    if line.startswith('  feedback_body:'):
        new_lines.append('  feedback_button_text: "Contact Us with Feedback"\n')
        new_lines.append('  image: "assets/images/real/X-Chem-1-2xl.jpeg"\n')
        new_lines.append('  image_caption: "X-Chem STEM Outreach Session at Dr. John Hugh Gillis High School"\n')

new_lines.append('\n# Section 7: Collaborators\n')
new_lines.append('collaborators:\n')
new_lines.append('  title: "Our Partners"\n')
new_lines.append('  body: "We love working with partners to co-create and evaluate customized versions of the Maintaining Brains Game for their audiences!"\n')
new_lines.append('  items:\n')
new_lines.append('    - icon: "groups"\n')
new_lines.append('      name: "Actua"\n')
new_lines.append('      description: "Canada\'s leading STEM outreach organization, collaborating to bring youth-focused brain health literacy to nationwide camps."\n')
new_lines.append('    - icon: "biotech"\n')
new_lines.append('      name: "X-Chem STEM Outreach"\n')
new_lines.append('      description: "Based at StFX, bringing hands-on neuroscience workshops and game trials directly into local elementary and high schools."\n')
new_lines.append('    - icon: "school"\n')
new_lines.append('      name: "Dr. John Hugh Gillis Regional High School"\n')
new_lines.append('      description: "Located in Antigonish, NS, collaborating on IB Psychology classroom testing and student discussion frameworks."\n')
new_lines.append('  feedback_title: "Have you made a custom version of the game?"\n')
new_lines.append('  feedback_body: "We\'d love to hear how your students or community group used the game!"\n')
new_lines.append('  feedback_button_text: "Let Us Know"\n')

with open('_data/content.yml', 'w') as f:
    f.writelines(new_lines)

print("done")
