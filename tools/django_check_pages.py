import os
import sys
from pathlib import Path
import django

# Ensure project root is on sys.path so 'agriconnect' settings module can be imported
proj_root = str(Path(__file__).resolve().parents[1])
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agriconnect.settings')
django.setup()

from django.test import Client

client = Client()
paths = ['/', '/contact/', '/help/', '/login/', '/dashboard/']
for p in paths:
    res = client.get(p)
    html = res.content.decode('utf-8')
    print(p, '->', res.status_code)
    if res.status_code == 200:
        print('  links ->',
              'home', ('href="/"' in html),
              'contact', ('/contact/' in html),
              'help', ('/help/' in html),
              'login', ('/login/' in html),
              'dashboard', ('/dashboard/' in html)
              )
    else:
        print('  content preview:', html[:200])
