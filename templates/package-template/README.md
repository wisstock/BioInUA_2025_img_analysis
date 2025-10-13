package-template
================
*_Bioinformatics for Ukraine course, 6-24 October 2025, Kyiv, Ukraine._*

Based on official [Python Packaging User Guide](https://packaging.python.org/en/latest/)

### Package structure:
```
package-template/
└── src/
│   └── package_template/
│       ├── __init__.py
│       └── module.py
├─── pyproject.toml
├─── README.md
├─── LICENSE
└─── .gitignore
```

### Dependency
- python >= 3.10
- numpy

### Local installation in editable mode with `pip`:
```
python -m pip install -e .
```