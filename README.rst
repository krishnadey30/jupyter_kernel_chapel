=====================
Jupyter Kernel Chapel
=====================

Using Chapel in Jupyter
**************************


It is possible to use `Jupyter <http://www.jupyter.org>`_ as front-end for Chapel.

Installation
############

These installation instructions are for Ubuntu Linux 16.04 (Xenial).

Python and Jupyter
~~~~~~~~~~~~~~~~~~

If you want to run the Jupyter notebook locally on your computer, you need a recent version
of Python 2 or 3 and Jupyter installed. The use of Python 3 is recommended.

**To install Python3 run**

.. code-block:: bash

  apt-get install python3-pip


We recommend using Python3, but you can also use Python2.

**To install Jupyter using pip, run**

.. code-block:: bash

  pip3 install jupyter


Chapel
~~~~~~

Please install Chapel in shared mode

.. code-block:: bash

  export CHPL_LIB_PIC=shared


Jupyter Kernel Chapel
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

  pip3 install jupyter-kernel-chapel
