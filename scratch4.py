config_yml = """backend:
  name: git-gateway
  branch: main

media_folder: "assets/images/uploads"
public_folder: "assets/images/uploads"

collections:
  - name: "site_content"
    label: "Site Content"
    files:
      # 1. Hero Banner
      - file: "_data/hero.yml"
        label: "Section 1: Hero Banner"
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

      # 2-7. Main Content Body
      - file: "_data/content.yml"
        label: "Sections 2-7: Main Content"
        name: "content"
        fields:
          - name: "menu_links"
            label: "Menu Links"
            widget: "list"
            fields: [
              { label: "Label", name: "label", widget: "string" },
              { label: "URL Anchor", name: "url", widget: "string" }
            ]
          
          - name: "creators"
            label: "Section 2: Creators & Origin"
            widget: "object"
            fields:
              - { label: "Title", name: "title", widget: "string" }
              - { label: "Paragraph 1", name: "p1", widget: "text" }
              - { label: "Paragraph 2", name: "p2", widget: "text" }
              - { label: "Badges", name: "badges", widget: "list", fields: [
                  { label: "Title", name: "title", widget: "string" },
                  { label: "Subtitle", name: "subtitle", widget: "string" }
                ]}
              - { label: "Workshop Image", name: "image", widget: "image" }
              - { 
                  label: "Photo Focus", 
                  name: "focal_point", 
                  widget: "select", 
                  options: ["object-center", "object-top", "object-bottom", "object-left", "object-right"],
                  default: "object-center"
                }
              - { label: "Image Title", name: "image_title", widget: "string" }
              - { label: "Image Caption", name: "image_caption", widget: "text" }

          - name: "teachers"
            label: "Section 3: For Teachers"
            widget: "object"
            fields:
              - { label: "Title", name: "title", widget: "string" }
              - { label: "Intro Body", name: "body", widget: "text" }
              - { label: "Curriculum Title", name: "curriculum_title", widget: "string" }
              - { label: "Curriculum Body", name: "curriculum_body", widget: "text" }
              - { label: "Discussion Questions Title", name: "discussion_questions_title", widget: "string" }
              - { label: "Discussion Questions", name: "questions", widget: "list", fields: [
                  { label: "Question", name: "question", widget: "string" }
                ]}
              - { label: "Feedback Card Title", name: "feedback_title", widget: "string" }
              - { label: "Feedback Card Body", name: "feedback_body", widget: "text" }
              - { label: "Feedback Button Text", name: "feedback_button_text", widget: "string" }
              - { label: "Teacher Image", name: "image", widget: "image" }
              - { label: "Teacher Image Caption", name: "image_caption", widget: "string" }

          - name: "download"
            label: "Section 4: Download Game"
            widget: "object"
            fields:
              - { label: "Title", name: "title", widget: "string" }
              - { label: "Body", name: "body", widget: "text" }
              - { label: "Button Label", name: "button_label", widget: "string" }
              - { label: "Button URL", name: "button_url", widget: "string" }
              - { label: "Printing Tips", name: "printing_tips", widget: "list", fields: [
                  { label: "Tip", name: "tip", widget: "string" }
                ]}
              - { label: "Materials Needed", name: "materials_needed", widget: "list", fields: [
                  { label: "Icon", name: "icon", widget: "string" },
                  { label: "Material Name", name: "name", widget: "string" }
                ]}

          - name: "research"
            label: "Section 5: Research"
            widget: "object"
            fields:
              - { label: "Title", name: "title", widget: "string" }
              - { label: "Publication Cards", name: "items", widget: "list", fields: [
                  { label: "Category", name: "category", widget: "string" },
                  { label: "Title", name: "title", widget: "string" },
                  { label: "Authors / Citation", name: "authors", widget: "text" },
                  { label: "Link Text", name: "link_text", widget: "string" },
                  { label: "Link URL", name: "link_url", widget: "string" }
                ]}

          - name: "tools"
            label: "Section 6: Card Generator"
            widget: "object"
            fields:
              - { label: "Title", name: "title", widget: "string" }
              - { label: "Body", name: "body", widget: "text" }
              - { label: "Button Label", name: "button_label", widget: "string" }
              - { label: "Tool URL", name: "button_url", widget: "string" }

          - name: "collaborators"
            label: "Section 7: Collaborators"
            widget: "object"
            fields:
              - { label: "Title", name: "title", widget: "string" }
              - { label: "Body", name: "body", widget: "text" }
              - { label: "Partners", name: "items", widget: "list", fields: [
                  { label: "Icon", name: "icon", widget: "string" },
                  { label: "Name", name: "name", widget: "string" },
                  { label: "Description", name: "description", widget: "text" }
                ]}
              - { label: "Feedback Title", name: "feedback_title", widget: "string" }
              - { label: "Feedback Body", name: "feedback_body", widget: "string" }
              - { label: "Feedback Button Text", name: "feedback_button_text", widget: "string" }

      # 8. Supporter Logos
      - file: "_data/partners.yml"
        label: "Section 8: Supporter Logos"
        name: "partners"
        fields:
          - { label: "Supporters", name: "partners", widget: "list", fields: [
              { label: "Name", name: "name", widget: "string" },
              { label: "Logo Image", name: "logo", widget: "image" },
              { label: "Website Link", name: "link", widget: "string" }
            ]}

      # 9. Contact Settings
      - file: "_data/settings.yml"
        label: "Site Contact Info"
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

print("config.yml rewritten successfully")
