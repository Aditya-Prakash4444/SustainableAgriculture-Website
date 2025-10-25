import requests

urls = [
    'http://127.0.0.1:8000/',
    'http://127.0.0.1:8000/contact/',
    'http://127.0.0.1:8000/help/',
    'http://127.0.0.1:8000/login/',
    'http://127.0.0.1:8000/dashboard/',
]

for u in urls:
    try:
        r = requests.get(u, timeout=5)
        print(u, '->', r.status_code)
        if r.status_code == 200:
            html = r.text
            print(' links present ->',
                  'home', ('<a href="/"' in html),
                  'contact', ('/contact/' in html),
                  'help', ('/help/' in html),
                  'login', ('/login/' in html),
                  'dashboard', ('/dashboard/' in html)
                  )
    except Exception as e:
        print(u, '-> error', e)
