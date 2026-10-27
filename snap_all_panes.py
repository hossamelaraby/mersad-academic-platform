# -*- coding: utf-8 -*-
import os
import subprocess

tools = ["literature", "citations", "data", "writing", "word"]
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()

with open('preview.html', 'r', encoding='utf-8') as f:
    base = f.read()

for tid in tools:
    s = base.replace(
        '<div class="modal-overlay" id="smartToolModal"',
        f'<div class="modal-overlay active" id="smartToolModal" style="display:flex !important;"'
    )
    s = s.replace(f'id="pane-{tid}" style="display:none;"', f'id="pane-{tid}" style="display:block;"')
    
    # Also set title
    meta_titles = {
        "literature": "مرصاد الدراسات السابقة",
        "citations": "مرصاد التوثيق",
        "data": "مرصاد البيانات",
        "writing": "مرصاد الكتابة",
        "word": "تصدير Word"
    }
    s = s.replace('id="toolHeaderTitle">مرصاد المصادر', f'id="toolHeaderTitle">{meta_titles[tid]}')
    
    tfile = f"test_pane_{tid}.html"
    with open(tfile, 'w', encoding='utf-8') as f:
        f.write(s)
    
    out = os.path.join(cwd, f"shot_pane_{tid}.png")
    subprocess.run([
        chrome, "--headless=new", "--disable-gpu",
        "--window-size=1200,950", f"--screenshot={out}",
        f"http://localhost:8000/{tfile}"
    ], check=True)
    print(f"Generated shot_pane_{tid}.png:", os.path.exists(out))
