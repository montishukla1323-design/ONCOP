import subprocess
import os

def get_word_page_count(docx_filename):
    abs_path = os.path.abspath(docx_filename).replace('\\', '\\\\')
    ps_code = f"""
$ErrorActionPreference = 'Stop'
$w = New-Object -ComObject Word.Application
try {{
    $d = $w.Documents.Open('{abs_path}')
    $pages = $d.ComputeStatistics(2)
    Write-Output "PAGE_COUNT: $pages"
    $d.Close(0)
}} finally {{
    $w.Quit()
}}
"""
    with open("temp_count.ps1", "w", encoding="utf-8") as f:
        f.write(ps_code)
    try:
        res = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "temp_count.ps1"], capture_output=True, text=True)
        for line in res.stdout.splitlines():
            if "PAGE_COUNT:" in line:
                return int(line.split(":")[1].strip())
    finally:
        if os.path.exists("temp_count.ps1"):
            os.remove("temp_count.ps1")
    return None

if __name__ == "__main__":
    count = get_word_page_count("test_header.docx")
    print("Computed page count:", count)
