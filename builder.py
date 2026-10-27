# -*- coding: utf-8 -*-
"""
Smart Platform Builder for Mersad (مدونة مرصاد)
Generates preview.html and theme.xml with 9 dedicated smart tools,
live Blogger post rendering, and responsive design.
"""
import os
import xml.etree.ElementTree as ET

def read_b64(name):
    with open(name + '.b64.txt', 'r', encoding='utf-8') as f:
        return f.read().strip()

print("1. Loading base64 assets...")
hero_cover_b64 = read_b64('hero_cover_hd.jpg')
laptop_art_b64 = read_b64('laptop_clean_opt.jpg')
logo_clean_b64 = read_b64('logo_clean_512.png')
logo_footer_b64 = read_b64('logo_footer_light.png')

print("Assets loaded successfully.")
