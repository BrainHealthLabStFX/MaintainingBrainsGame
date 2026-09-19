import re

# 1. Update config.yml
config_yml = """backend:
  name: git-gateway
  branch: main

media_folder: "assets/images/uploads"
public_folder: "assets/images/uploads"

collections:
  # 1. Navigation Links
  - name: "navigation"
    label: "Header Navigation"
    files:
      - file: "_data/content.yml"
        label: "Menu Links"
        name: "menu"
        fields:
          - { label: "Menu Links", name: "menu_links", widget: "list", fields: [
              { label: "Label", name: "label", widget: "string" },
              { label: "URL Anchor", name: "url", widget: "string" }
            ]}

  # 2. Hero Banner
  - name: "hero_section"
    label: "Section 1: Hero Banner"
    files:
      - file: "_data/hero.yml"
        label: "Hero Content"
        name: "hero"
        fields:
          - { label: "Main Headline", name: "headline", widget: "string" }
          - { label: "Body Paragraph", name: "body", widget: "text" }
          - { label: "Hero Image", name: "image", widget: "image" }
          - { 
              label: "Photo Focus", 
              name: "focal_point", 
              widget: "select", 
              options: ["object-center", "object-top", "object-bottom", "object-left", "object-right"],
              default: "object-center"
            }
          - { label: "Highlights", name: "highlights", widget: "list", fields: [
              { label: "Icon", name: "icon", widget: "string" },
              { label: "Text", name: "text", widget: "string" }
            ]}
          - { label: "Download Button Text", name: "button1_text", widget: "string" }
          - { label: "Download Button URL", name: "button1_url", widget: "string" }
          - { label: "Teachers Button Text", name: "button2_text", widget: "string" }
          - { label: "Teachers Button URL", name: "button2_url", widget: "string" }

  # 3. Creators & Origin
  - name: "creators_section"
    label: "Section 2: Creators & Origin"
    files:
      - file: "_data/content.yml"
        label: "Creators Content"
        name: "creators"
        fields:
          - { label: "Title", name: "creators.title", widget: "string" }
          - { label: "Paragraph 1", name: "creators.p1", widget: "text" }
          - { label: "Paragraph 2", name: "creators.p2", widget: "text" }
          - { label: "Badges", name: "creators.badges", widget: "list", fields: [
              { label: "Title", name: "title", widget: "string" },
              { label: "Subtitle", name: "subtitle", widget: "string" }
            ]}
          - { label: "Workshop Image", name: "creators.image", widget: "image" }
          - { 
              label: "Photo Focus", 
              name: "creators.focal_point", 
              widget: "select", 
              options: ["object-center", "object-top", "object-bottom", "object-left", "object-right"],
              default: "object-center"
            }
          - { label: "Image Title", name: "creators.image_title", widget: "string" }
          - { label: "Image Caption", name: "creators.image_caption", widget: "text" }

  # 4. For Teachers
  - name: "teachers_section"
    label: "Section 3: For Teachers"
    files:
      - file: "_data/content.yml"
        label: "Teachers Content"
        name: "teachers"
        fields:
          - { label: "Title", name: "teachers.title", widget: "string" }
          - { label: "Intro Body", name: "teachers.body", widget: "text" }
          - { label: "Curriculum Title", name: "teachers.curriculum_title", widget: "string" }
          - { label: "Curriculum Body", name: "teachers.curriculum_body", widget: "text" }
          - { label: "Discussion Questions Title", name: "teachers.discussion_questions_title", widget: "string" }
          - { label: "Discussion Questions", name: "teachers.questions", widget: "list", fields: [
              { label: "Question", name: "question", widget: "string" }
            ]}
          - { label: "Feedback Card Title", name: "teachers.feedback_title", widget: "string" }
          - { label: "Feedback Card Body", name: "teachers.feedback_body", widget: "text" }
          - { label: "Feedback Button Text", name: "teachers.feedback_button_text", widget: "string" }
          - { label: "Teacher Image", name: "teachers.image", widget: "image" }
          - { label: "Teacher Image Caption", name: "teachers.image_caption", widget: "string" }

  # 5. Download Materials
  - name: "download_section"
    label: "Section 4: Download Game"
    files:
      - file: "_data/content.yml"
        label: "Download Content"
        name: "download"
        fields:
          - { label: "Title", name: "download.title", widget: "string" }
          - { label: "Body", name: "download.body", widget: "text" }
          - { label: "Button Label", name: "download.button_label", widget: "string" }
          - { label: "Button URL", name: "download.button_url", widget: "string" }
          - { label: "Printing Tips", name: "download.printing_tips", widget: "list", fields: [
              { label: "Tip", name: "tip", widget: "string" }
            ]}
          - { label: "Materials Needed", name: "download.materials_needed", widget: "list", fields: [
              { label: "Icon", name: "icon", widget: "string" },
              { label: "Material Name", name: "name", widget: "string" }
            ]}

  # 6. Research & Publications
  - name: "research_section"
    label: "Section 5: Research"
    files:
      - file: "_data/content.yml"
        label: "Research Publications"
        name: "research"
        fields:
          - { label: "Title", name: "research.title", widget: "string" }
          - { label: "Publication Cards", name: "research.items", widget: "list", fields: [
              { label: "Category", name: "category", widget: "string" },
              { label: "Title", name: "title", widget: "string" },
              { label: "Authors / Citation", name: "authors", widget: "text" },
              { label: "Link Text", name: "link_text", widget: "string" },
              { label: "Link URL", name: "link_url", widget: "string" }
            ]}

  # 7. Card Generator Tools
  - name: "tools_section"
    label: "Section 6: Card Generator"
    files:
      - file: "_data/content.yml"
        label: "Tool Content"
        name: "tools"
        fields:
          - { label: "Title", name: "tools.title", widget: "string" }
          - { label: "Body", name: "tools.body", widget: "text" }
          - { label: "Button Label", name: "tools.button_label", widget: "string" }
          - { label: "Tool URL", name: "tools.button_url", widget: "string" }

  # 8. Partners (Collaborators)
  - name: "collaborators_section"
    label: "Section 7: Collaborators"
    files:
      - file: "_data/content.yml"
        label: "Collaborators Content"
        name: "collaborators"
        fields:
          - { label: "Title", name: "collaborators.title", widget: "string" }
          - { label: "Body", name: "collaborators.body", widget: "text" }
          - { label: "Partners", name: "collaborators.items", widget: "list", fields: [
              { label: "Icon", name: "icon", widget: "string" },
              { label: "Name", name: "name", widget: "string" },
              { label: "Description", name: "description", widget: "text" }
            ]}
          - { label: "Feedback Title", name: "collaborators.feedback_title", widget: "string" }
          - { label: "Feedback Body", name: "collaborators.feedback_body", widget: "string" }
          - { label: "Feedback Button Text", name: "collaborators.feedback_button_text", widget: "string" }

  # 9. Supporters (Logos)
  - name: "supporters_section"
    label: "Section 8: Supporter Logos"
    files:
      - file: "_data/partners.yml"
        label: "Supporter Logos"
        name: "partners"
        fields:
          - { label: "Supporters", name: "partners", widget: "list", fields: [
              { label: "Name", name: "name", widget: "string" },
              { label: "Logo Image", name: "logo", widget: "image" },
              { label: "Website Link", name: "link", widget: "string" }
            ]}

  # 10. Site Settings & Footer Contact
  - name: "settings_section"
    label: "Site Contact Info"
    files:
      - file: "_data/settings.yml"
        label: "Contact & Location"
        name: "contact"
        fields:
          - { label: "Project Title", name: "title", widget: "string" }
          - { label: "Contact Email", name: "email", widget: "string" }
          - { label: "Department", name: "department", widget: "string" }
          - { label: "Institution", name: "institution", widget: "string" }
          - { label: "Location", name: "location", widget: "string" }
"""

with open('admin/config.yml', 'w') as f:
    f.write(config_yml)

print("config.yml written")
