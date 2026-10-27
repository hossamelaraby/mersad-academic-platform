# -*- coding: utf-8 -*-
import os
import subprocess

with open('preview.html', 'r', encoding='utf-8') as f:
    s = f.read()

s = s.replace('id="smartToolModal"', 'id="smartToolModal" class="modal-overlay active"')
s = s.replace('id="pane-sources" style="display:none;"', 'id="pane-sources" style="display:block;"')
with open('test_force_modal.html', 'w', encoding='utf-8') as f:
    f.write(s)

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out = os.path.join(os.getcwd(), "forced_modal_shot.png")
subprocess.run([
    chrome, "--headless=new", "--disable-gpu",
    "--window-size=1200,900", f"--screenshot={out}",
    "http://localhost:8000/test_force_modal.html"
], check=True)
print("Forced modal screenshot saved:", os.path.exists(out))
