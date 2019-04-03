#!/usr/bin/env python
import json
import os
import codecs
from setuptools import setup, find_packages
from setuptools.command.install import install
from glob import glob

kernelpath = os.path.join("share", "jupyter", "kernels", "chapel")
nbextpath = os.path.join("share", "jupyter", "nbextensions", "chapel-mode")
nbconfpath = os.path.join("etc", "jupyter", "nbconfig", "notebook.d")

def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)

def read(fname):
    return codecs.open(fpath(fname), encoding='utf-8').read()

setup( name="jupyter-kernel-chapel"
     , version="0.0.4"
     , description="A Jupyter kernel for chapel"
     , long_description=read(fpath('README.rst'))
     , author="Krishna Kumar Dey"
     , author_email="krishnakumardey.dey@gmail.com"
     , url="https://github.com/krishnadey30/jupyter_kernel_chapel"
     , download_url='https://github.com/krishnadey30/jupyter_kernel_chapel/tarball/0.0.1'
     , packages=find_packages()
     , keywords=['jupyter', 'notebook', 'kernel', 'chapel']
     , include_package_data=True
     , install_requires=[
        'jupyter-core',
        'jupyter_client',
        ]
     , data_files=[(kernelpath, glob("jupyter-kernel-chapel/resources/*")),
                   (kernelpath, glob("jupyter-kernel-chapel/kernel.json")),
                   (nbextpath, glob("jupyter-kernel-chapel/chapel-mode/*")),
                   (nbconfpath, glob("jupyter-kernel-chapel/chapel-mode.json"))]
     )
