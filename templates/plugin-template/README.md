plugin-template
===============
_Bioinformatics for Ukraine course, 6-24 October 2025, Kyiv, Ukraine._

Based on official [napari Plugins Guide](https://napari.org/stable/plugins/first_plugin.html)

### Plugin structure:
```
plugin-template/
├── src/
│   └── plugin_template/
│       ├── __init__.py
│       ├── napari.yaml
│       └── _widget.py
├─── pyproject.toml
├─── README.md
├─── LICENSE
└─── .gitignore
```

### Dependency
- python >= 3.10
- matplotlib
- numpy
- scikit-image

### Local installation in editable mode with `pip`:
```
python -m pip install -e .
```

### Widgets
- Simple masking from meetintg 3
- Widget demo
- Plot demo