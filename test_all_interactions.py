# -*- coding: utf-8 -*-
import os
import subprocess

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()

# 1. Main Page Screenshot (1312x1200)
main_shot = os.path.join(cwd, "test_main_view.png")
subprocess.run([
    chrome, "--headless=new", "--disable-gpu",
    "--window-size=1312,1200", f"--screenshot={main_shot}",
    "http://localhost:8000/preview.html"
], check=True)
print("Main page screenshot saved:", os.path.exists(main_shot))

# 2. Open each tool and take screenshots to verify all 9 tools work
tools_to_test = [
    ("sources", "shot_tool_sources.png"),
    ("literature", "shot_tool_literature.png"),
    ("citations", "shot_tool_citations.png"),
    ("data", "shot_tool_data.png")
]

with open('preview.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

for tool_id, shot_name in tools_to_test:
    test_file = f"test_{tool_id}.html"
    modified_html = base_html.replace('</body>', f'<script>openSmartTool("{tool_id}");</script></body>')
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(modified_html)
    
    shot_path = os.path.join(cwd, shot_name)
    subprocess.run([
        chrome, "--headless=new", "--disable-gpu",
        "--window-size=1200,900", f"--screenshot={shot_path}",
        f"http://localhost:8000/{test_file}"
    ], check=True)
    print(f"Tool {tool_id} screenshot saved:", os.path.exists(shot_path))

# 3. Mobile screenshot
mobile_shot = os.path.join(cwd, "test_mobile_view.png")
subprocess.run([
    chrome, "--headless=new", "--disable-gpu",
    "--window-size=390,844", f"--screenshot={mobile_shot}",
    "http://localhost:8000/preview.html"
], check=True)
print("Mobile view screenshot saved:", os.path.exists(mobile_shot))
