Boa
===

.. image:: https://img.shields.io/pypi/v/boa-str.svg
    :target: https://pypi.python.org/pypi/boa-str
    :alt: PyPI

.. image:: https://img.shields.io/circleci/project/github/astronomerio/boa.svg
    :target: https://circleci.com/gh/astronomerio/boa
    :alt: CircleCI

.. image:: https://codecov.io/gh/astronomerio/boa/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/astronomerio/boa
    :alt: Codecov

Boa is a Python package for normalizing and converting strings to snakecase.

For example, it translates the user-defined event ``'User Buys Item'`` to ``'user_buys_item'`` which can then be used in a file path in S3, or as the name of a schema or table in Redshift.

It also handles the more complex cases such as stripping punctuation and converting words from camelCase or PascalCase to snake_case (see examples below).

Installation
------------

Install in your virtual environment:

.. code-block:: console

    $ pip install boa-str

Quickstart
----------

.. code-block:: python

    >>> import boa
    >>> my_str = 'Hello Boa'
    >>> boa.constrict(my_str)
    'hello_boa'

Examples
--------

.. code-block:: python

    >>> import boa
    >>> boa.constrict('toInfinityAndBeyond')
    'to_infinity_and_beyond'
    >>> boa.constrict('Welcome-to-planet-Earth!')
    'welcome_to_planet_earth'

Tests
-----

We use `nose2 <https://pypi.python.org/pypi/nose2>`_ and `coverage <https://pypi.python.org/pypi/coverage>`_ for unit tests.

Install with test requirements:

.. code-block:: console

    $ pip install boa-str[test]

Then run:

.. code-block:: console

    $ invoke test

Lint
----

.. code-block:: console

    $ invoke lint

Dev
---

Install with dev requirements (includes test requirements):

.. code-block:: console

    $ pip install boa-str[dev]

🐍️🐍️🐍️
