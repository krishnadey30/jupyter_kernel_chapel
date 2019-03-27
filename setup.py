#!/usr/bin/env python
import json
import os
from setuptools import setup, find_packages
from setuptools.command.install import install


class Installer(install):
     def run(self):
          # Regular install
          install.run(self)

          # Post install
          print('Installing Ansible Kernel kernelspec')
          from jupyter_client.kernelspec import KernelSpecManager
          from IPython.utils.tempdir import TemporaryDirectory
          kernel_json = {
          "argv": [
               "python3",
               "-m",
               "jupyter-kernel-chapel",
               "-f",
               "{connection_file}"
          ],
          "display_name": "Chapel",
          "language": "chapel",
          "codemirror_mode": "chapel"
          }
          
          with TemporaryDirectory() as td:
               os.chmod(td, 0o755)  # Starts off as 700, not user readable
               with open(os.path.join(td, 'kernel.json'), 'w') as f:
                    json.dump(kernel_json, f, sort_keys=True)
               # TODO: Copy resources once they're specified

               print('Installing IPython kernel spec')
               KernelSpecManager().install_kernel_spec(td, 'chapel', user=self.user, replace=True, prefix=self.prefix)



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
     , cmdclass={'install': Installer}
     , keywords=['jupyter', 'notebook', 'kernel', 'chapel']
     , include_package_data=True
     )
