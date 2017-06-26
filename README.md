# Boa

[![PyPI](https://img.shields.io/pypi/v/boa-str.svg)](https://pypi.python.org/pypi/boa-str) [![CircleCI](https://img.shields.io/circleci/project/github/astronomerio/boa.svg)](https://circleci.com/gh/astronomerio/boa) [![codecov](https://codecov.io/gh/astronomerio/boa/branch/master/graph/badge.svg)](https://codecov.io/gh/astronomerio/boa)

Boa is a Python package for normalizing and converting strings to snakecase.

For example, it translates the user-defined event `'User Buys Item'` to `'user_buys_item'` which can then be used in a file path in S3, or as the name of a schema or table in Redshift.

It also handles the more complex cases such as stripping punctuation and converting words from camelCase or PascalCase to snake_case (see examples below).

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

## Examples

```python
>>> import boa

>>> boa.constrict('toInfinityAndBeyond')
'to_infinity_and_beyond'

>>> boa.constrict('Welcome-to-planet-Earth!')
'welcome_to_planet_earth'

```

## Tests

We use [nose2][nose2-pypi] and [coverage][coverage-pypi] for unit tests.

Install with test requirements:

```bash
$ pip install boa-str[test]
```

Then run:

```bash
$ invoke test
```

## Lint

```bash
$ invoke lint
```

## Dev

Install with dev requirements (includes test requirements):

```bash
$ pip install boa-str[dev]
```

🐍️🐍️🐍️

[coverage-pypi]: https://pypi.python.org/pypi/coverage
[nose2-pypi]: https://pypi.python.org/pypi/nose2
