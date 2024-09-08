# Configuration file for the Sphinx documentation builder.

project = 'tips-and-tricks'
copyright = '2024, See the AUTHORS.md file'
author = 'See the AUTHORS.md file'
release = '0.0.1'

extensions = ['sphinx_wagtail_theme']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']
html_title = "PSM tips and trics page"

html_show_copyright = False
html_show_sphinx = False