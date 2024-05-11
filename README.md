# Writing a Python Library in OCaml

This is an example of how to write a python library in OCaml, using
[pyml](https://github.com/thierry-martinez/pyml) and
[pythonlib](https://github.com/janestreet/pythonlib).

## gen python bindings
>$ cd ocaml
>$ pyml_bindgen val_specs.txt adder Adder --caml-module Adder > lib.ml

this operation with generate lib.ml in ocaml

## Build
>$ make


## test
>$ cd test
>$ python test.py

