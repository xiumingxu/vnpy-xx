from distutils.core import setup

import numpy
from Cython.Build import cythonize

setup(
    name='binomial_tree_cython',
    ext_modules=cythonize("binomial_tree_cython.pyx"),
    include_dirs=[numpy.get_include()]
)
