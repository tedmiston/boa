from invoke import task

@task
def clean(ctx):
    """Clear bytecode and cache files."""
    ctx.run('find . -name \*.pyc -delete')
    ctx.run('find . -name __pycache__ -delete')

@task
def lint(ctx):
    """Check style."""
    ctx.run('pycodestyle .')

@task
def release(ctx, upload=False, cleanup=True):
    """Generate a distribution release and upload to PyPI."""
    ctx.run('python setup.py check')
    ctx.run('python setup.py sdist')
    ctx.run('python setup.py bdist_wheel --universal')

    if upload:
        ctx.run('twine upload dist/*')

    if cleanup:
        ctx.run('python setup.py clean --all')
        ctx.run('rm -fR boa_str.egg-info/')
        ctx.run('rm -fR dist/')

@task
def test(ctx):
    """Run unit tests and coverage."""
    ctx.run('nose2')
    ctx.run('python -m doctest -v README.md')
