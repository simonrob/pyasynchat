[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

# Purpose
This package contains the [asynchat](https://docs.python.org/3.11/library/asynchat.html) module as found in Python versions prior to 3.12.
It is provided so that existing code relying on `import asynchat` is able to continue being used without significant refactoring.

The module's source code is taken directly from the [Python standard library](https://github.com/python/cpython/blob/3.9/Lib/asynchat.py)<sup id="a1">[[1]](#f1)</sup>.
The specific version of [`asynchat.py`](https://github.com/simonrob/pyasynchat/blob/master/asynchat/asynchat.py) that is provided is the last update before the addition of deprecation/removal warnings at import time, and is identical to [the version bundled with Python 3.9](https://github.com/python/cpython/blob/3.9/Lib/asynchat.py).

Please note that new projects should prefer [asyncio](https://docs.python.org/3/library/asyncio.html).


## Installation
This version of `asynchat` is intended for Python 3.12 or later. Install the module using `pip`:
```shell
python -m pip install pyasynchat
```

The module can be installed for earlier Python versions, but it will have no effect, and the standard library version of `asynchat` will be used in its place.

Note that installing `pyasynchat` will not remove deprecation warnings in Python versions 3.10 and 3.11.
Instead, use the `warnings` package:
```python
import warnings
with warnings.catch_warnings():
    warnings.simplefilter('ignore', DeprecationWarning)
    import asynchat
```


## Usage
The module is imported in exactly the same way as the standard library component it replaces:
```python
import asynchat
```

Note that the [PyPI module](https://pypi.org/project/pyasynchat/) is named `pyasynchat` because creating modules with the same name as those provided by the standard library is not permitted.

For guidance about using the `asynchat` module, see the [official documentation](https://docs.python.org/3.11/library/asynchat.html).


## Maintenance
Due to the fact that this previously built-in module is [no-longer supported](https://peps.python.org/pep-0594/) by the Python core development team, no further maintenance of the code in [`asynchat.py`](https://github.com/simonrob/pyasynchat/blob/master/asynchat/asynchat.py) is intended.
This project is only intended to be updated to make changes or improvements to the module packaging.


## License
[Python Software Foundation License Version 2](LICENSE)


### Footnotes
<sub id="f1">1. Verify this if needed via: `diff <(curl --location https://github.com/python/cpython/raw/3.9/Lib/asynchat.py) <(curl --location https://github.com/simonrob/pyasynchat/raw/master/asynchat/asynchat.py)` [⏎](#a1)</sub>
