from setuptools import find_packages, setup

setup(
    name='boa-str',
    version='1.0.1',
    description='Convert strings to snakecase',
    long_description=(
        'Boa is a Python package for constricting strings to a specific '
        'snakecase format.\n\nWe use it to translate user-defined event names '
        'into names we can use for database tables and in S3 file names. For '
        'example, "User Buys Item" becomes "user_buys_item".'
    ),
    url='https://github.com/astronomerio/boa',
    author='Taylor Edmiston',
    author_email='taylor@astronomer.io',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='boa snakecase snake_case snake case inflector astronomer astronomerio',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
)
