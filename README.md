## Mixing Rust into python

This repository is a simple example of how to mix Rust code into Python code.
The Rust code is compiled into a shared library and then loaded into Python
using the `maturin` library.

## Development

To build the Rust code, you need to have Rust installed. You can install Rust
using `rustup` by following the instructions on the
[Rust website](https://www.rust-lang.org/tools/install).

To install maturin, you can use `pip` or `pipx`:

```bash
pip install -U maturin
```

## Initialize the project

To initialize the project, you need to run the following command:

```bash
maturin new [path]
```

This will create a new project in the specified path. You can then navigate to
the [path] and start developing your Rust code.
