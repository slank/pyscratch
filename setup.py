from subprocess import check_output
from setuptools import setup

def version_from_git():
    output = check_output(
        ('git', 'tag', '-l', '--points-at=HEAD')
    )
    if not output:
        return None
    return output.split('\n')[0]

setup(
    name='scratch',
    version=version_from_git(),
    description='Scratch project for testing packaging',
    url='https://github.com/slank/pyscratch',
    author='Matthew Wedgwood',
    author_email='pyscratch+maintainers@smacky.org',
    license='MIT',
    packages=['scratch'],
    zip_safe=True,
)
