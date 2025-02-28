import os, sysconfig
from pathlib import Path
from setuptools import setup, Extension
from Cython.Build import cythonize
extensions = [
    Extension("ctf", ["ctf.pyx"],
    library_dirs=[f"{Path(sysconfig.get_paths()['stdlib']).parent}{os.path.sep}libs"],
    libraries=["python311"],
    include_dirs=[sysconfig.get_paths()["include"]])
]

setup(
    name="ctf",
    ext_modules=cythonize(extensions),
)
