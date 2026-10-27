import os
import subprocess

with open('preview.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add script at end to open the modal
html_modal_open = html.replace('</body>', '<script>openSmartTool("sources");</script></body>')
with open('test_modal.html', 'w', encoding='utf-8') as f:
    f.write(html_modal_open)

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out = os.path.join(os.getcwd(), "modal_screenshot.png")
cmd = [chrome, "--headless=new", "--disable-gpu", "--window-size=1200,900", f"--screenshot={out}", "http://localhost:8000/test_modal.html"]
subprocess.run(cmd, check=True)
print("Saved modal_screenshot.png:", os.path.exists(out))
