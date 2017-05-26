# Boa

[![CircleCI](https://circleci.com/gh/astronomerio/boa.svg?style=svg)](https://circleci.com/gh/astronomerio/boa)

Boa is a Python package for constricting strings to a specific snakecase format.

We use it to translate user-defined event names into names we can use for database tables and in S3 file names. For example, "User Buys Item" becomes "user_buys_item".

## Installation

Install in your virtual environment:

```bash
$ pip install boa-str
```

## Quickstart

```python
>>> import boa
>>> my_str = 'Hello Boa'
>>> boa.constrict(my_str)
'hello_boa'
```

## Tests

We use [nose2][nose2-pypi] and [coverage][coverage-pypi] for unit tests.

First install test requirements:

```bash
$ pip install -r requirements-dev.txt
```

Then run:

```bash
$ invoke test
```

## Lint

```bash
$ invoke lint
```

🐍️🐍️🐍️

[coverage-pypi]: https://pypi.python.org/pypi/coverage
[nose2-pypi]: https://pypi.python.org/pypi/nose2
