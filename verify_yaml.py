import os
import re

def check_yaml_file(fp):
    if not os.path.exists(fp):
        return
    with open(fp, "r") as f:
        lines = f.readlines()
    
    issues = []
    for i, line in enumerate(lines):
        # Ignore comments
        if line.strip().startswith('#'):
            continue
            
        # Check if line has a key-value pair
        if ":" in line:
            parts = line.split(":", 1)
            val = parts[1].strip()
            
            # If value is not empty and not quoted
            if val and not (val.startswith('"') or val.startswith("'") or val.startswith('|') or val.startswith('>')):
                # If there's a colon followed by space in the value, it's illegal
                if ": " in val:
                    issues.append(f"Line {i+1}: {line.strip()}")
    
    if issues:
        print(f"--- Issues found in {fp} ---")
        for issue in issues:
            print(issue)
        print()

for file in os.listdir('_data'):
    if file.endswith('.yml'):
        check_yaml_file(os.path.join('_data', file))

print("Verification complete.")
