## Mixing Rust into python

This repository is a simple example of how to mix Rust code into Python code.
The Rust code is compiled into a shared library and then loaded into Python
using the `maturin` library.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?skip_quickstart=true&machine=basicLinux32gb&repo=850242937&ref=main&devcontainer_path=.devcontainer%2Fdevcontainer.json&geo=SoutheastAsia)

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

## Build the project

To build development artifacts, you can run the following command:

```bash
maturin develop
```

## Using UV as a package manager

To use `uv` as a package manager, you should the virtual environment in the
project directory:

```bash
uv venv
```

At the first, you can build the pyo3 library by running the following command:

```bash
uv sync --refresh
```

After that, the shared object is not built properly, you can run the following
command:

```bash
maturin develop --uv
```

Don't forget the `--uv` flag. because maturin will use `pip` as a package
manager by default. `--uv` flag will use `uv` as a package manager.
