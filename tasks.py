from invoke import task

@task
def clean(ctx):
    # TODO: implement clear **/*.pyc and __pycache__ files
    pass

@task
def lint(ctx):
    ctx.run('pycodestyle .')

@task
def release(ctx):
    """Generate a distribution release and upload to PyPI."""
    ctx.run('python setup.py check')
    ctx.run('python setup.py sdist')
    ctx.run('python setup.py bdist_wheel --universal')
    ctx.run('twine upload dist/*')
    # TODO: clean up build, dist, etc

@task
def test(ctx):
    """Run unit tests and coverage."""
    ctx.run('nose2')
