import re

with open('build_all.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any data:image/...;base64,{var} with {var}
replacements = [
    ('data:image/png;base64,{logo_clean_b64}', '{logo_clean_b64}'),
    ('data:image/png;base64,{logo_footer_b64}', '{logo_footer_b64}'),
    ('data:image/jpeg;base64,{laptop_art_b64}', '{laptop_art_b64}'),
    ('data:image/jpeg;base64,{hero_cover_b64}', '{hero_cover_b64}')
]

for old, new in replacements:
    count = text.count(old)
    text = text.replace(old, new)
    print(f"Replaced {count} occurrences of {old}")

with open('build_all.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated build_all.py successfully.")
