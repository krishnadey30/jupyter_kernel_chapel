#!/usr/bin/env python

from glob import glob
from distutils.core import setup

import json
import os
import sys

from jupyter_client.kernelspec import install_kernel_spec
from IPython.utils.tempdir import TemporaryDirectory

from os.path import dirname,abspath

from shutil import copy as file_copy

kernelpath = os.path.join("share", "jupyter", "kernels", "chapel")
nbextpath = os.path.join("share", "jupyter", "nbextensions", "chapel-mode")
nbconfpath = os.path.join("etc", "jupyter", "nbconfig", "notebook.d")

setup( name="chapel_kernel"
     , version="0.0.1"
     , description="A Jupyter kernel for chapel"
     , author="Krishna Kumar Dey"
     , author_email="krishnakumardey.dey@gmail.com"
     , url="https://github.com/krishnadey30/jupyter-chapel"
     , packages=["chapel_kernel"]
     , package_dir={"chapel_kernel": "chapel_kernel"}
     , data_files=[(kernelpath, glob("jupyter_kernel_singular/kernel.json")),
                    (nbextpath, glob("chapel_kernel/chapel-mode/*")),
                   (nbconfpath, glob("chapel_kernel/chapel-mode.json"))]
     )
