import os, re, glob
files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    print(f'--- {f} ---')
    # Top Nav and Footer Nav (regular)
    for m in re.finditer(r'<li>\s*<a[^>]*href=\"booking\.html\"[^>]*>Booking</a>\s*</li>', content, re.IGNORECASE):
        print('Top Nav:', m.group(0).strip())
    # Mobile Drawer
    for m in re.finditer(r'<a[^>]*href=\"booking\.html\"[^>]*>\s*<span[^>]*>calendar_month</span>\s*Booking\s*</a>', content, re.IGNORECASE):
        print('Mobile Drawer:', m.group(0).strip())
    # Footer Nav (with span)
    for m in re.finditer(r'<li>\s*<a[^>]*href=\"booking\.html\"[^>]*>\s*<span[^>]*></span>\s*Booking\s*</a>\s*</li>', content, re.IGNORECASE):
        print('Footer Nav Span:', m.group(0).strip())
    # Mobile Bottom Nav
    for m in re.finditer(r'<a[^>]*href=\"booking\.html\"[^>]*>\s*<span[^>]*>calendar_month</span>\s*<span[^>]*>Book(?:ing)?</span>\s*</a>', content, re.IGNORECASE):
        print('Mobile Bottom Nav:', m.group(0).strip())
    
    # Let's also check for any other nav links without <li> wrapper, just in case
    for m in re.finditer(r'<a[^>]*href=\"booking\.html\"[^>]*>Booking</a>', content, re.IGNORECASE):
        if not re.search(r'<li>\s*<a', content[max(0, m.start()-10):m.end()]):
            print('Other Link:', m.group(0).strip())
