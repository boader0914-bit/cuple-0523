import re
import sys

html_path = 'index.html'
hero_html_path = 'c:/Users/User/.gemini/antigravity/brain/d16496b8-2098-4119-8127-6023ec6db692/scratch/hero_replacement.html'
hero_js_path = 'c:/Users/User/.gemini/antigravity/brain/d16496b8-2098-4119-8127-6023ec6db692/scratch/hero_js.js'

try:
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    with open(hero_html_path, 'r', encoding='utf-8') as f:
        hero_html = f.read()
    with open(hero_js_path, 'r', encoding='utf-8') as f:
        hero_js = f.read()

    # Replace HTML section
    pattern_html = re.compile(r'<div class="bg-white rounded-2xl p-6 md:p-8 shadow-\[0_20px_50px_rgba\(0,0,0,0\.06\)\] border subtle-border diagnosis-card">.*?</form>\s*</div>', re.DOTALL)
    html = pattern_html.sub(hero_html, html, count=1)

    # Replace JS section
    pattern_js = re.compile(r'// AI Preliminary Diagnosis Logic.*?\}\);', re.DOTALL)
    html = pattern_js.sub(hero_js, html, count=1)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Replacement success.")
except Exception as e:
    print(f"Error: {e}")
