# -*- coding: utf-8 -*-
import os
import subprocess

with open('preview.html', 'r', encoding='utf-8') as f:
    s = f.read()

# Correctly replace the class attribute so there is only ONE class attribute
s = s.replace(
    '<div class="modal-overlay" id="smartToolModal"',
    '<div class="modal-overlay active" id="smartToolModal" style="display:flex !important;"'
)
s = s.replace('id="pane-sources" style="display:none;"', 'id="pane-sources" style="display:block;"')

with open('test_verify_modal.html', 'w', encoding='utf-8') as f:
    f.write(s)

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out = os.path.join(os.getcwd(), "verified_modal_visual.png")
subprocess.run([
    chrome, "--headless=new", "--disable-gpu",
    "--window-size=1200,950", f"--screenshot={out}",
    "http://localhost:8000/test_verify_modal.html"
], check=True)
print("Saved verified_modal_visual.png:", os.path.exists(out))
