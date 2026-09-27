#!/usr/bin/env python3
import json

with open('stem_entry.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total forms: {len(data["forms"])}')
print('\nForm types:')
for form in data['forms']:
    print(f'  - {form["type"]}: {form["label"]}')

# Check for the three perfect forms
perfect_types = ['present_perfect', 'past_perfect', 'present_perfect_progressive']
found_perfect = [t for t in perfect_types if any(f['type'] == t for f in data['forms'])]

print(f'\nPerfect forms found: {len(found_perfect)}/3')
for ft in found_perfect:
    print(f'  ✓ {ft}')

for ft in perfect_types:
    if ft not in found_perfect:
        print(f'  ✗ {ft}')
