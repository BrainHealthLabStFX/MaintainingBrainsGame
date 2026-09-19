config = """backend:
  name: git-gateway
  branch: main

media_folder: "assets/images/uploads"
public_folder: "assets/images/uploads"

collections:
  - name: "navigation"
    label: "Header Navigation"
    files:
      - file: "_data/menu.yml"
        label: "Menu Links"
        name: "menu"
        fields:
          - { label: "Menu Links", name: "menu_links", widget: "list", required: false, fields: [
              { label: "Label", name: "label", widget: "string", required: false },
              { label: "URL Anchor", name: "url", widget: "string", required: false }
            ]}

  - name: "hero_section"
    label: "Section 1: Hero Banner"
    files:
      - file: "_data/hero.yml"
        label: "Hero Content"
        name: "hero"
        fields:
          - { label: "Section Anchor ID", name: "section_id", widget: "string", required: false, default: "about" }
          - { label: "Main Headline", name: "headline", widget: "string", required: false }
          - { label: "Body Paragraph", name: "body", widget: "text", required: false }
          - { label: "Hero Image", name: "image", widget: "image", required: false }
          - { 
              label: "Photo Focus", 
              name: "focal_point", 
              widget: "select", 
              required: false,
              options: ["object-center", "object-top", "object-bottom", "object-left", "object-right"],
              default: "object-center"
            }
          - { label: "Highlights", name: "highlights", widget: "list", required: false, fields: [
              { label: "Icon", name: "icon", widget: "string", required: false },
              { label: "Text", name: "text", widget: "string", required: false }
            ]}
          - { label: "Download Button Text", name: "button1_text", widget: "string", required: false }
          - { label: "Download Button URL", name: "button1_url", widget: "string", required: false }
          - { label: "Teachers Button Text", name: "button2_text", widget: "string", required: false }
          - { label: "Teachers Button URL", name: "button2_url", widget: "string", required: false }

  - name: "creators_section"
    label: "Section 2: Creators & Origin"
    files:
      - file: "_data/creators.yml"
        label: "Creators Content"
        name: "creators"
        fields:
          - { label: "Section Anchor ID", name: "section_id", widget: "string", required: false, default: "creators" }
          - { label: "Title", name: "title", widget: "string", required: false }
          - { label: "Paragraph 1", name: "p1", widget: "text", required: false }
          - { label: "Paragraph 2", name: "p2", widget: "text", required: false }
          - { label: "Badges", name: "badges", widget: "list", required: false, fields: [
              { label: "Title", name: "title", widget: "string", required: false },
              { label: "Subtitle", name: "subtitle", widget: "string", required: false }
            ]}
          - { label: "Workshop Image", name: "image", widget: "image", required: false }
          - { 
              label: "Photo Focus", 
              name: "focal_point", 
              widget: "select", 
              required: false,
              options: ["object-center", "object-top", "object-bottom", "object-left", "object-right"],
              default: "object-center"
            }
          - { label: "Image Title", name: "image_title", widget: "string", required: false }
          - { label: "Image Caption", name: "image_caption", widget: "text", required: false }

  - name: "teachers_section"
    label: "Section 3: For Teachers"
    files:
      - file: "_data/teachers.yml"
        label: "Teachers Content"
        name: "teachers"
        fields:
          - { label: "Section Anchor ID", name: "section_id", widget: "string", required: false, default: "teachers" }
          - { label: "Title", name: "title", widget: "string", required: false }
          - { label: "Intro Body", name: "body", widget: "text", required: false }
          - { label: "Curriculum Title", name: "curriculum_title", widget: "string", required: false }
          - { label: "Curriculum Body", name: "curriculum_body", widget: "text", required: false }
          - { label: "Discussion Questions Title", name: "discussion_questions_title", widget: "string", required: false }
          - { label: "Discussion Questions", name: "questions", widget: "list", required: false, fields: [
              { label: "Question", name: "question", widget: "string", required: false }
            ]}
          - { label: "Feedback Card Title", name: "feedback_title", widget: "string", required: false }
          - { label: "Feedback Card Body", name: "feedback_body", widget: "text", required: false }
          - { label: "Feedback Button Text", name: "feedback_button_text", widget: "string", required: false }
          - { label: "Teacher Image", name: "image", widget: "image", required: false }
          - { label: "Teacher Image Caption", name: "image_caption", widget: "string", required: false }

  - name: "download_section"
    label: "Section 4: Download Game"
    files:
      - file: "_data/download.yml"
        label: "Download Content"
        name: "download"
        fields:
          - { label: "Section Anchor ID", name: "section_id", widget: "string", required: false, default: "download" }
          - { label: "Title", name: "title", widget: "string", required: false }
          - { label: "Body", name: "body", widget: "text", required: false }
          - { label: "Button Label", name: "button_label", widget: "string", required: false }
          - { label: "Button URL", name: "button_url", widget: "string", required: false }
          - { label: "Printing Tips", name: "printing_tips", widget: "list", required: false, fields: [
              { label: "Tip", name: "tip", widget: "string", required: false }
            ]}
          - { label: "Materials Needed", name: "materials_needed", widget: "list", required: false, fields: [
              { label: "Icon", name: "icon", widget: "string", required: false },
              { label: "Material Name", name: "name", widget: "string", required: false }
            ]}

  - name: "research_section"
    label: "Section 5: Research"
    files:
      - file: "_data/research.yml"
        label: "Research Publications"
        name: "research"
        fields:
          - { label: "Section Anchor ID", name: "section_id", widget: "string", required: false, default: "research" }
          - { label: "Title", name: "title", widget: "string", required: false }
          - { label: "Publication Cards", name: "items", widget: "list", required: false, fields: [
              { label: "Category", name: "category", widget: "string", required: false },
              { label: "Title", name: "title", widget: "string", required: false },
              { label: "Authors / Citation", name: "authors", widget: "text", required: false },
              { label: "Link Text", name: "link_text", widget: "string", required: false },
              { label: "Link URL", name: "link_url", widget: "string", required: false }
            ]}

  - name: "tools_section"
    label: "Section 6: Card Generator"
    files:
      - file: "_data/tools.yml"
        label: "Tool Content"
        name: "tools"
        fields:
          - { label: "Section Anchor ID", name: "section_id", widget: "string", required: false, default: "tools" }
          - { label: "Title", name: "title", widget: "string", required: false }
          - { label: "Body", name: "body", widget: "text", required: false }
          - { label: "Button Label", name: "button_label", widget: "string", required: false }
          - { label: "Tool URL", name: "button_url", widget: "string", required: false }

  - name: "collaborators_section"
    label: "Section 7: Collaborators"
    files:
      - file: "_data/collaborators.yml"
        label: "Collaborators Content"
        name: "collaborators"
        fields:
          - { label: "Section Anchor ID", name: "section_id", widget: "string", required: false, default: "partners" }
          - { label: "Title", name: "title", widget: "string", required: false }
          - { label: "Body", name: "body", widget: "text", required: false }
          - { label: "Partners", name: "items", widget: "list", required: false, fields: [
              { label: "Icon", name: "icon", widget: "string", required: false },
              { label: "Name", name: "name", widget: "string", required: false },
              { label: "Description", name: "description", widget: "text", required: false }
            ]}
          - { label: "Feedback Title", name: "feedback_title", widget: "string", required: false }
          - { label: "Feedback Body", name: "feedback_body", widget: "string", required: false }
          - { label: "Feedback Button Text", name: "feedback_button_text", widget: "string", required: false }

  - name: "supporters_section"
    label: "Section 8: Supporter Logos"
    files:
      - file: "_data/partners.yml"
        label: "Supporter Logos"
        name: "partners"
        fields:
          - { label: "Section Anchor ID", name: "section_id", widget: "string", required: false, default: "supporters" }
          - { label: "Supporters", name: "partners", widget: "list", required: false, fields: [
              { label: "Name", name: "name", widget: "string", required: false },
              { label: "Logo Image", name: "logo", widget: "image", required: false },
              { label: "Website Link", name: "link", widget: "string", required: false }
            ]}

  - name: "settings_section"
    label: "Site Contact Info"
    files:
      - file: "_data/settings.yml"
        label: "Contact & Location"
        name: "contact"
        fields:
          - { label: "Project Title", name: "title", widget: "string", required: false }
          - { label: "Contact Email", name: "email", widget: "string", required: false }
          - { label: "Department", name: "department", widget: "string", required: false }
          - { label: "Institution", name: "institution", widget: "string", required: false }
          - { label: "Location", name: "location", widget: "string", required: false }
"""
with open('admin/config.yml', 'w') as f:
    f.write(config)

print("Config rewritten")
