# encoding: utf8

from setuptools import setup, find_packages


setup(
    author='Eitan Joseph, Chami Lamelas',
    author_email="eitanjoseph@brandeis.edu",
    description='A data structures and algorithms library based on Introduction to Algorithms Third Edition by Thomas H. Cormen.',
    install_requires=['dalpy'],
    long_description='''Use `DALPy <https://pypi.org/project/dalpy/>`_ instead.''',
    name='cormen-lib',
    platforms=['all'],
    url='https://pypi.org/project/dalpy/',
    version="1.1.3",
    zip_safe=False,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
