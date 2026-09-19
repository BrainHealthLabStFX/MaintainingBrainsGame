with open('_data/download.yml', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip().startswith("- tip:"):
        # Split on the FIRST colon only
        key, val = line.split(":", 1)
        val = val.strip()
        new_lines.append(f"{key}: \"{val}\"\n")
    elif line.strip().startswith("- icon:"):
        key, val = line.split(":", 1)
        new_lines.append(f"{key}: \"{val.strip()}\"\n")
    elif line.strip().startswith("name:"):
        # already quoted from previous script
        new_lines.append(line)
    else:
        new_lines.append(line)

with open('_data/download.yml', 'w') as f:
    f.writelines(new_lines)

# Also fix any other lists in other files just to be 100% safe
def quote_list_items(fp, prefix):
    if not __import__('os').path.exists(fp): return
    with open(fp, 'r') as f:
        lines = f.readlines()
    nl = []
    for line in lines:
        if line.strip().startswith(prefix):
            k, v = line.split(":", 1)
            v = v.strip()
            if not v.startswith('"') and not v.startswith("'"):
                v = v.replace('"', '\\"')
                nl.append(f"{k}: \"{v}\"\n")
            else:
                nl.append(line)
        else:
            nl.append(line)
    with open(fp, 'w') as f:
        f.writelines(nl)

quote_list_items('_data/teachers.yml', '- question:')
quote_list_items('_data/research.yml', '- category:')
quote_list_items('_data/collaborators.yml', '- icon:')
quote_list_items('_data/partners.yml', '- name:')
