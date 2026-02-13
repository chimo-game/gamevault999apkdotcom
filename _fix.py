import os, re

dl_dir = 'downloads'
count = 0

for fname in os.listdir(dl_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(dl_dir, fname)
    with open(fpath, 'r') as f:
        html = f.read()

    # 1. Remove verify button HTML block
    html = re.sub(
        r'\s*<button class="df-verify-btn" id="dfVerifyBtn"[^>]*>.*?</button>',
        '',
        html,
        flags=re.DOTALL
    )

    # 2. Replace locker emoji with giphy.gif
    html = html.replace(
        '<div class="df-locker-emoji">&#x1F50D;</div>',
        '<img src="/assets/images/giphy.gif" alt="" class="df-locker-gif">'
    )

    # 3. Change locker header text
    html = html.replace(
        '<h2>One last step to unlock your download</h2>',
        '<h2>Are you human?</h2>'
    )

    # 4. Change locker description
    html = html.replace(
        '<p>Complete <b>1 quick action</b> below to verify &amp; unlock your APK file</p>',
        "<p>Please complete <b>1 quick action</b> below to verify you're not a robot.</p>"
    )

    with open(fpath, 'w') as f:
        f.write(html)
    count += 1
    print(f'  Updated: {fname}')

print(f'\nDone. Updated {count} pages.')
