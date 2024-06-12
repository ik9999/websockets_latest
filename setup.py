import os
import pathlib
import re

import setuptools


root_dir = pathlib.Path(__file__).parent

exec((root_dir / "src_latest" / "websockets_latest" / "version.py").read_text(encoding="utf-8"))

# PyPI disables the "raw" directive. Remove this section of the README.
long_description = re.sub(
    r"^\.\. raw:: html.*?^(?=\w)",
    "",
    (root_dir / "README.rst").read_text(encoding="utf-8"),
    flags=re.DOTALL | re.MULTILINE,
)

# Set BUILD_EXTENSION to yes or no to force building or not building the
# speedups extension. If unset, the extension is built only if possible.
if os.environ.get("BUILD_EXTENSION") == "no":
    ext_modules = []
else:
    ext_modules = [
        setuptools.Extension(
            "websockets_latest.speedups",
            sources=["src_latest/websockets_latest/speedups.c"],
            optional=os.environ.get("BUILD_EXTENSION") != "yes",
        )
    ]

# Static values are declared in pyproject.toml.
setuptools.setup(
    package_dir = {"": "src_latest"}
    version=version,
    long_description=long_description,
    ext_modules=ext_modules,
)
