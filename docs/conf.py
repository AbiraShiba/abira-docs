# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "abira-docs"
copyright = "2026, abira"
author = "abira"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}


extensions = [
    "myst_parser",
    "sphinx.ext.mathjax",
]

# Markdownで多少のHTMLを許可
myst_enable_extensions = [
    "html_admonition",
    "html_image",
    "dollarmath",
    "amsmath",
]
myst_dmath_double_inline = True

# MathJax v3 を明示（安全策）
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# physics をロード + 有効化
mathjax3_config = {
    "loader": {"load": ["[tex]/physics"]},
    "tex": {"packages": {"[+]": ["physics"]}},
}
root_doc = "index"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
# html_theme = "alabaster"
html_static_path = ["_static"]
