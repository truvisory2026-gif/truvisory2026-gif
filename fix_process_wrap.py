# -*- coding: utf-8 -*-
import re

css_path = 'assets/css/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .process-timeline in media queries to allow wrapping
css = css.replace(
    'flex-direction: row;\n    max-width: 100%;\n    align-items: center;\n    justify-content: space-between;',
    'flex-direction: row;\n    flex-wrap: wrap;\n    max-width: 100%;\n    align-items: center;\n    justify-content: center;\n    gap: 1.5rem;'
)

# Hide connectors if wrapping occurs? Actually, connectors might look weird if wrapping.
# Let's just allow wrapping and center it.
# We also want to make sure the base .process-timeline has wrap just in case
if 'display: flex;\n  flex-direction: column;\n  gap: 1rem;\n  max-width: 600px;\n  margin: 0 auto;' in css:
    css = css.replace(
        'display: flex;\n  flex-direction: column;\n  gap: 1rem;\n  max-width: 600px;\n  margin: 0 auto;',
        'display: flex;\n  flex-direction: column;\n  gap: 1rem;\n  max-width: 800px;\n  margin: 0 auto;'
    )

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated .process-timeline css to flex-wrap.")
