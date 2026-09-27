#!/usr/bin/env python3
import json
import sys

with open('elbow_entry.json', 'r') as f:
    data = json.load(f)
    
# Verify the perfect forms exist
forms = data.get('forms', [])
perfect_forms = [f for f in forms if f.get('type') in ['present_perfect', 'past_perfect', 'present_perfect_progressive']]

print(f"Total forms: {len(forms)}")
print(f"Perfect forms found: {len(perfect_forms)}")
for pf in perfect_forms:
    print(f"  - {pf['type']}: {pf['text']}")
