#!/usr/bin/env python
import subprocess
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext
from distutils.command.clean import clean

class CustomBuilder(build_ext):
    def run(self):
        p = subprocess.Popen('nvcc --compiler-options="-fPIC" -m64 -arch=sm_20 -o cufft_core.o -c cufft_core.cu', stdout=subprocess.PIPE, shell=True)
        stdout, stderr = p.communicate()
        if p.returncode != 0:
            raise RuntimeError
        build_ext.run(self)

class CustomCleaner(clean):
    def run(self):
        os.remove('cufft_core.o')
        clean.run(self)

_cufft = Extension('_cufft',
  ['cufft.i','cufft_cxxwrap.cpp'],
  swig_opts=['-c++'],
  include_dirs = ['/usr/local/cuda-7.5/targets/x86_64-linux/include'],
  library_dirs = ['/usr/local/cuda-7.5/targets/x86_64-linux/lib'],
  libraries = ['cuda', 'cudart', 'cufft'],
  extra_objects = ['cufft_core.o']
)

setup(name = 'cuFFT',
  description = 'A very simple Python wrapper for cuFFT',
  author      = 'Yohai Meiron (based the NVIDIA CUDA Fast Fourier Transform library)',
  version     = '1.0',
  ext_modules = [_cufft],
  cmdclass = {'build_ext': CustomBuilder, 'clean': CustomCleaner}
)
