#!/usr/bin/env python
import json
import os
from setuptools import setup, find_packages
from setuptools.command.install import install
from glob import glob

kernelpath = os.path.join("share", "jupyter", "kernels", "chapel")
nbextpath = os.path.join("share", "jupyter", "nbextensions", "chapel-mode")
nbconfpath = os.path.join("etc", "jupyter", "nbconfig", "notebook.d")

with open('README.md', 'r') as f:
    long_description = f.read()

setup( name="jupyter-kernel-chapel"
     , version="0.0.4"
     , description="A Jupyter kernel for chapel"
     , long_description=long_description
     , author="Krishna Kumar Dey"
     , author_email="krishnakumardey.dey@gmail.com"
     , url="https://github.com/krishnadey30/jupyter_kernel_chapel"
     , download_url='https://github.com/krishnadey30/jupyter_kernel_chapel/tarball/0.0.1'
     , packages=find_packages()
     , keywords=['jupyter', 'notebook', 'kernel', 'chapel']
     , include_package_data=True
     , data_files=[(kernelpath, glob("jupyter-kernel-chapel/resources/*")),
                   (kernelpath, glob("jupyter-kernel-chapel/kernel.json")),
                   (nbextpath, glob("jupyter-kernel-chapel/chapel-mode/*")),
                   (nbconfpath, glob("jupyter-kernel-chapel/chapel-mode.json"))]
     )
