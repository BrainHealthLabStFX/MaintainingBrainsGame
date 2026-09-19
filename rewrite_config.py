with open("admin/config.yml", "r") as f:
    text = f.read()

# Make the internal names unique to bust cache
text = text.replace('name: "menu"', 'name: "menu_data"')
text = text.replace('name: "hero"', 'name: "hero_data"')
text = text.replace('name: "creators"', 'name: "creators_data"')
text = text.replace('name: "teachers"', 'name: "teachers_data"')
text = text.replace('name: "download"', 'name: "download_data"')
text = text.replace('name: "research"', 'name: "research_data"')
text = text.replace('name: "tools"', 'name: "tools_data"')
text = text.replace('name: "collaborators"', 'name: "collaborators_data"')
text = text.replace('name: "partners"', 'name: "partners_data"')
text = text.replace('name: "contact"', 'name: "contact_data"')

with open("admin/config.yml", "w") as f:
    f.write(text)
print("Config names updated to bust cache.")
