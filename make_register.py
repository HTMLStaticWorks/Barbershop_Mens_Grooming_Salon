import re

with open('register.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Title
content = re.sub(
    r'<title>Login \| BladeKing Barbershop</title>',
    '<title>Create Account | BladeKing Barbershop</title>',
    content
)

# Remove Login View
content = re.sub(
    r'<!-- Login View -->\s*<div class="glass-card[^>]*id="login-view".*?<!-- Register View -->',
    '<!-- Register View -->',
    content,
    flags=re.DOTALL
)

# Make Register View visible
content = re.sub(
    r'<div class="glass-card ([^>]*?) hidden ([^>]*?)" id="register-view">',
    r'<div class="glass-card \1 \2" id="register-view">',
    content
)

# Update Login Link
content = re.sub(
    r'<button class="text-secondary hover:underline decoration-secondary transition-all" onclick="toggleView\(\'login\'\)" type="button">Login here</button>',
    r'<a class="text-secondary hover:underline decoration-secondary transition-all" href="login.html">Login here</a>',
    content
)

# Remove toggleView function
content = re.sub(
    r'function toggleView\(view\) \{.*?\}\s*(?=function togglePassword)',
    '',
    content,
    flags=re.DOTALL
)

with open('register.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("register.html updated successfully.")
