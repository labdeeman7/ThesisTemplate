"""Render every page and record MuPDF warnings; this is not an Acrobat test."""
from pathlib import Path
import hashlib
import json
import re
import sys
import fitz

reports = []
for filename in sys.argv[1:]:
    path = Path(filename)
    document = fitz.open(path)
    opening_warnings = fitz.TOOLS.mupdf_warnings()
    issues = []
    for page in document:
        try:
            page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
            page.get_text()
            warnings = fitz.TOOLS.mupdf_warnings()
            if warnings:
                issues.append({'pdf_page': page.number + 1, 'warnings': warnings})
        except Exception as exc:
            issues.append({'pdf_page': page.number + 1, 'error': str(exc),
                           'warnings': fitz.TOOLS.mupdf_warnings()})
    references = set()
    for xref in range(1, document.xref_length()):
        references.update(re.findall(r'/ICCBased\s+(\d+)\s+0\s+R', document.xref_object(xref)))
    profiles = [{'xref': int(x), 'decoded_bytes': len(document.xref_stream(int(x)) or b'')}
                for x in sorted(references, key=int)]
    reports.append({'file': str(path), 'bytes': path.stat().st_size,
                    'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                    'pages': len(document), 'metadata': document.metadata,
                    'opening_warnings': opening_warnings, 'page_issues': issues,
                    'icc_profiles': profiles})
    document.close()
output = Path('.build/pdf-check-2026-10-12.json')
output.write_text(json.dumps(reports, indent=2, ensure_ascii=False), encoding='utf-8')
for report in reports:
    print(report['file'], report['pages'], 'pages;', len(report['page_issues']), 'pages with warnings/errors')
    print('Empty ICC profiles:', [p['xref'] for p in report['icc_profiles'] if p['decoded_bytes'] == 0])
print('Report:', output)
