"""Validate the built public artifact without network calls or model inference."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'

class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.duplicates = []
        self.refs = []
        self.h1 = 0
        self.main = 0
        self.lang = None
        self.scripts = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'h1': self.h1 += 1
        if tag == 'main': self.main += 1
        if tag == 'script': self.scripts += 1
        if 'id' in a:
            if a['id'] in self.ids: self.duplicates.append(a['id'])
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if key in a: self.refs.append(a[key])

docs = {}
errors = []
for p in SITE.rglob('*.html'):
    d = Document()
    d.feed(p.read_text())
    docs[p.resolve()] = d
    if d.h1 != 1 or d.main != 1 or d.lang != 'en':
        errors.append(f'{p.name}: expected one h1, one main, and lang=en')
    if d.duplicates: errors.append(f'{p.name}: duplicate IDs')
    if d.scripts: errors.append(f'{p.name}: unexpected browser script')

links = 0
for p, d in docs.items():
    for ref in d.refs:
        u = urlsplit(ref)
        if u.scheme or u.netloc: continue
        target = (SITE / unquote(u.path).lstrip('/')) if u.path.startswith('/') else p.parent / unquote(u.path)
        if not u.path: target = p
        if target.is_dir(): target = target / 'index.html'
        target = target.resolve()
        links += 1
        if not target.is_relative_to(SITE):
            errors.append(f'{p.name}: link escapes site: {ref}')
        elif not target.exists():
            errors.append(f'{p.name}: missing local destination: {ref}')
        elif u.fragment and target in docs and unquote(u.fragment) not in docs[target].ids:
            errors.append(f'{p.name}: missing anchor: {ref}')

manifest = json.loads((ROOT/'evidence/source-manifest.json').read_text())
for r in manifest['files']:
    data = (ROOT/r['local_path']).read_bytes()
    git_sha = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if git_sha != r['upstream_git_blob_sha']:
        errors.append(f'Archive differs from upstream: {r["local_path"]}')
    if hashlib.sha256(data).hexdigest() != r['local_sha256']:
        errors.append(f'Manifest hash differs: {r["local_path"]}')

home = (SITE/'index.html').read_text()
findings = (SITE/'findings.html').read_text()
for required in ['https://gofund.me/95781ab95','mailto:RESelfProject@outlook.com','No established model-level RES finding']:
    if required not in home: errors.append(f'Home missing required content: {required}')
for required in ['0.507812','35/64','38/64','did <strong>not</strong> replicate','ASSAY_INADEQUATE']:
    if required not in findings: errors.append(f'Findings missing frozen conclusion: {required}')

# Detect obvious accidental credential formats without printing any matched value.
import re
secret_patterns=[r'gh[pousr]_[A-Za-z0-9]{30,}', r'sk-[A-Za-z0-9_-]{35,}',r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----']
for p in ROOT.rglob('*'):
    if p.is_file() and '.git' not in p.parts and p.suffix in {'.md','.json','.html','.mjs','.css','.txt'}:
        text=p.read_text(errors='replace')
        if any(re.search(pattern,text) for pattern in secret_patterns): errors.append(f'Possible credential in {p.relative_to(ROOT)}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(json.dumps({'html_pages':len(docs),'local_links_checked':links,'upstream_files_byte_verified':len(manifest['files']),'client_scripts':0,'result':'PASS'},indent=2))
