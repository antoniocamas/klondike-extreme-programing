'''
setup.py                                                                                                                                                                 
'''
import multiprocessing
from setuptools import setup, find_packages

setup(name='TestDrivenDevelopment',
      version='0.1',
      packages=find_packages(),
      tests_require=['nose'],
      test_suite='nose.collector'
)
