import subprocess
import os

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.getcwd()
out_desktop = os.path.join(cwd, "verify_desktop.png")
out_mobile = os.path.join(cwd, "verify_mobile.png")

print("Capturing desktop...")
cmd_d = [chrome, "--headless=new", "--disable-gpu", "--window-size=1312,1800", f"--screenshot={out_desktop}", "http://localhost:8000/preview.html"]
subprocess.run(cmd_d, check=True)
print("Desktop exists:", os.path.exists(out_desktop))

print("Capturing mobile...")
cmd_m = [chrome, "--headless=new", "--disable-gpu", "--window-size=390,1200", f"--screenshot={out_mobile}", "http://localhost:8000/preview.html"]
subprocess.run(cmd_m, check=True)
print("Mobile exists:", os.path.exists(out_mobile))
