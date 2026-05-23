$htmlPath = "index.html"
$heroHtmlPath = "c:\Users\User\.gemini\antigravity\brain\d16496b8-2098-4119-8127-6023ec6db692\scratch\hero_replacement.html"
$heroJsPath = "c:\Users\User\.gemini\antigravity\brain\d16496b8-2098-4119-8127-6023ec6db692\scratch\hero_js.js"

$html = Get-Content -Path $htmlPath -Raw -Encoding UTF8
$heroHtml = Get-Content -Path $heroHtmlPath -Raw -Encoding UTF8
$heroJs = Get-Content -Path $heroJsPath -Raw -Encoding UTF8

$html = [regex]::Replace($html, '(?s)<div class="bg-white rounded-2xl p-6 md:p-8 shadow-\[0_20px_50px_rgba\(0,0,0,0\.06\)\] border subtle-border diagnosis-card">.*?</form>\s*</div>', $heroHtml)
$html = [regex]::Replace($html, '(?s)// AI Preliminary Diagnosis Logic.*?\}\);', $heroJs)

Set-Content -Path $htmlPath -Value $html -Encoding UTF8
Write-Host "Replacement done."
