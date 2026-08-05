import os, re, glob
files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    original = content
    
    # 1. Top Nav and Footer Nav (regular)
    content = re.sub(r'<li>\s*<a[^>]*href=\"booking\.html\"[^>]*>Booking</a>\s*</li>\n?', '', content, flags=re.IGNORECASE)
    
    # 1b. Top Nav (with newlines like in booking.html/home2.html/index.html)
    content = re.sub(r'<li>\s*<a[^>]*href=\"booking\.html\"[^>]*>Booking</a>\s*</li>\n?', '', content, flags=re.IGNORECASE)
    
    # 2. Mobile Drawer
    content = re.sub(r'<a[^>]*href=\"booking\.html\"[^>]*>\s*<span[^>]*>calendar_month</span>\s*Booking\s*</a>\n?', '', content, flags=re.IGNORECASE)
    
    # 3. Footer Nav (with span)
    content = re.sub(r'<li>\s*<a[^>]*href=\"booking\.html\"[^>]*>\s*<span[^>]*></span>\s*Booking\s*</a>\s*</li>\n?', '', content, flags=re.IGNORECASE)
    
    # 4. Mobile Bottom Nav
    content = re.sub(r'<a[^>]*href=\"booking\.html\"[^>]*>\s*<span[^>]*>calendar_month</span>\s*<span[^>]*>Book(?:ing)?</span>\s*</a>\n?', '', content, flags=re.IGNORECASE)

    # 5. Top Nav (where it is just an <a> without <li>)
    # Looking at the output, there are "Other Link:" items which are actually the top nav links on some pages.
    # E.g. <a class="border-b-2 border-transparent pb-1 font-button text-button uppercase tracking-wider text-on-surface hover:text-secondary transition-colors duration-300" href="booking.html">Booking</a>
    content = re.sub(r'<li>\s*<a[^>]*href=\"booking\.html\"[^>]*>Booking</a>\s*</li>\n?', '', content, flags=re.IGNORECASE)
    
    # Top nav without <li> wrapper:
    content = re.sub(r'<a[^>]*href=\"booking\.html\"[^>]*>Booking</a>\n?', '', content, flags=re.IGNORECASE)
    # Note: This could match buttons like "Book Now" if they just say "Booking", but none of them do. They say "Book Now" or "Book Appointment".
    # Wait! In booking.html line 312 it's inside <li>:
    # <li>
    # <a class="..." href="booking.html">Booking</a>
    # </li>
    
    if content != original:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
