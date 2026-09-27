import json
import os
from pathlib import Path

# Read Target 1400 words
with open(r"C:\Users\hmicr\AppData\Local\Temp\claude\C--Users-hmicr-ngsl-samples\d5370acc-4a0a-4b4e-9fb8-56da335224fd\scratchpad\target_1400_words.txt") as f:
    target_1400_words = set(word.strip() for word in f.readlines() if word.strip())

# Process existing entry files
modified_count = 0
error_count = 0
project_dir = r"C:\Users\hmicr\ngsl-samples"
os.chdir(project_dir)

for word in sorted(target_1400_words):
    entry_file = f"{word}_entry.json"
    if os.path.exists(entry_file):
        try:
            with open(entry_file, 'r', encoding='utf-8') as f:
                entry = json.load(f)
            
            # Add tags field if it doesn't exist
            if "tags" not in entry:
                entry["tags"] = ["Target 1400"]
                with open(entry_file, 'w', encoding='utf-8') as f:
                    json.dump(entry, f, ensure_ascii=False, indent=2)
                modified_count += 1
        except json.JSONDecodeError as e:
            error_count += 1
            if error_count <= 5:  # Print first 5 errors
                print(f"Error in {entry_file}: {e}")

print(f"Modified {modified_count} entries to add Target 1400 tag")
if error_count > 0:
    print(f"Encountered {error_count} JSON errors")
