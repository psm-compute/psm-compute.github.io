# Configuration file for the Sphinx documentation builder.

project = 'tips-and-tricks'
copyright = '2024, See the AUTHORS.md file'
author = 'See the AUTHORS.md file'
release = '0.0.1'

extensions = ['sphinx_wagtail_theme']

templates_path = ['_templates']
exclude_patterns = []

# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = "PSM tips",
    github_url = "https://github.com/psm-compute/psm-compute.github.io/tree/main/docs/source/"
    # logo_alt = "Wagtail",
    # logo_height = 59,
    # logo_url = "/",
    # logo_width = 45,
)

html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']
html_title = "PSM tips and trics page"

html_show_copyright = False
html_show_sphinx = False
