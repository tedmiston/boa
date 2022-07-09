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

You can also override the default behavior of stripping non-alphanumeric characters by providing a replacement character:

.. code-block:: python

    >>> import boa
    >>> my_str = 'no*separator'
    >>> boa.constrict(my_str)
    'noseparator'
    >>> my_str = 'with*a*separator'
    >>> boa.constrict(my_str, '_')
    'with_a_separator'
    >>> boa.constrict(my_str, repl='_')
    'with_a_separator'

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

You can either install boa in a virtual environment or alternatively run the dockerized CircleCI build locally (skip to the CircleCI section after you clone).

We use `nose2 <https://pypi.python.org/pypi/nose2>`_ and `coverage <https://pypi.python.org/pypi/coverage>`_ for unit tests.

Clone:

.. code-block:: console

    $ git clone https://github.com/tedmiston/boa/
    $ cd boa

Install with test requirements:

.. code-block:: console

    $ pip install .[test]

Then run:

.. code-block:: console

    $ invoke test

CircleCI
--------

CircleCI will automatically run on the server, and with the 2.0 API can now also be run locally (using Docker) to check config or run unit tests.

Setup
~~~~~

Install the `CircleCI CLI <https://circleci.com/docs/2.0/local-jobs/>`_ as described in their documentation.

*Note: While the CircleCI docs claim that working_directory cannot be a relative path for local builds, it works fine for me. If you experience an issue with this, try changing it to an absolute path instead.*

Validate
~~~~~~~~

To validate the config:

.. code-block:: console

    $ circleci config validate

Build
~~~~~

To run the build:

.. code-block:: console

    $ circleci build \
    -e CIRCLE_PROJECT_USERNAME=astronomerio \
    -e CIRCLE_PROJECT_REPONAME=boa

You need to provide these additional environment variables when running locally that get populated automatically on the server.

*Note: Due to a limitation in CircleCI, it's expected to see an error for skipping uploading test results when running locally. It's currently not possible to configure built-in commands to not run locally.*

Style
-----

.. code-block:: console

    $ invoke lint

Contribute
----------

Clone the repo, then install with dev requirements which also includes test requirements:

.. code-block:: console

    $ git clone https://github.com/tedmiston/boa/
    $ cd boa
    $ pip install .[dev]

🐍️🐍️🐍️
