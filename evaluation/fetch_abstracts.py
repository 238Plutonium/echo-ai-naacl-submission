#!/usr/bin/env python3
"""Fetch local PubMed title/abstract cache from a list of PMIDs; do not redistribute automatically."""
import argparse
import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--pmids', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
p.add_argument('--email', default='')
a = p.parse_args()
ids = list(dict.fromkeys(x.strip() for x in a.pmids.read_text().splitlines() if x.strip()))
if not all(x.isdigit() for x in ids):
    raise ValueError('Expected one numeric PMID per line')
if a.output.exists():
    raise FileExistsError(f'Refusing to overwrite {a.output}')
cache = {}
for i in range(0, len(ids), 15):
    query = {'db':'pubmed','id':','.join(ids[i:i+15]),'retmode':'xml','tool':'echoai_reproduction'}
    if a.email:
        query['email'] = a.email
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?' + urllib.parse.urlencode(query)
    with urllib.request.urlopen(url, timeout=45) as r:
        root = ET.fromstring(r.read())
    for art in root.findall('.//PubmedArticle'):
        pmid = (art.findtext('./MedlineCitation/PMID') or '').strip()
        title = art.find('.//ArticleTitle')
        lines = [''.join(title.itertext()).strip() if title is not None else '']
        for ab in art.findall('.//Abstract/AbstractText'):
            text = ''.join(ab.itertext()).strip()
            label = ab.get('Label')
            lines.append(f'{label}: {text}' if label else text)
        if pmid:
            cache[pmid] = '\n'.join(lines).strip()
    time.sleep(0.4)
a.output.parent.mkdir(parents=True, exist_ok=True)
with a.output.open('x') as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)
print(f'Fetched {len(cache)}/{len(ids)} records. Records are current, not a historical cache reconstruction.')
