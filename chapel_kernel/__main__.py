from ipykernel.kernelapp import IPKernelApp
from .kernel import ChapelKernel
IPKernelApp.launch_instance(kernel_class=ChapelKernel)