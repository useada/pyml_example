"""
An example Ocaml library exposed to Python
"""

import os
import sys
from ctypes import PyDLL, RTLD_GLOBAL, c_char_p

curdir = dir_path = os.path.dirname(os.path.realpath(__file__))
# dll = PyDLL(f"{curdir}/pywrap.so", RTLD_GLOBAL)

# Load the shared library and initialize the OCaml runtime
if sys.platform == "darwin":
    # dll = PyDLL(f"{curdir}/pywrap.dylib", RTLD_GLOBAL)
    dll = PyDLL(f"{curdir}/pywrap.so", RTLD_GLOBAL)
elif sys.platform == "win32":
    dll = PyDLL(f"{curdir}/pywrap.dll", RTLD_GLOBAL)
else:
    dll = PyDLL(f"{curdir}/pywrap.so", RTLD_GLOBAL)

argv_t = c_char_p * 2
argv = argv_t("pywrap.so".encode('utf-8'), None)
dll.caml_startup(argv)

# We export the names explicitly otherwise mypy gets confused and
# generates spurious errors
from example_module import random_expr, evaluate, random_expr_, evaluate_, map_array, add
