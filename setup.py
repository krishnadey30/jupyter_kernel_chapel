#!/usr/bin/env python
from setuptools import setup
setup( name="chapel_kernel"
     , version="0.0.1"
     , description="A Jupyter kernel for chapel"
     , author="Krishna Kumar Dey"
     , author_email="krishnakumardey.dey@gmail.com"
     , url="https://github.com/krishnadey30/jupyter_kernel_chapel"
     , packages=["chapel_kernel"]
     , scripts=['chapel_kernel/install_chapel_kernel']
     , include_package_data=True
     )
