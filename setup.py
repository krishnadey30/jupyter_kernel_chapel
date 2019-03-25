#!/usr/bin/env python
from setuptools import setup
setup( name="jupyter-kernel-chapel"
     , version="0.0.2"
     , description="A Jupyter kernel for chapel"
     , author="Krishna Kumar Dey"
     , author_email="krishnakumardey.dey@gmail.com"
     , url="https://github.com/krishnadey30/jupyter_kernel_chapel"
     , download_url='https://github.com/krishnadey30/jupyter_kernel_chapel/tarball/0.0.1'
     , packages=["jupyter-kernel-chapel"]
     , scripts=['jupyter-kernel-chapel/install_chapel_kernel']
     , keywords=['jupyter', 'notebook', 'kernel', 'chapel']
     , include_package_data=True
     )
