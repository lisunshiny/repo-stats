from setuptools import setup


setup(name='repostats',
      version='0.2',
      description='Get stats on your repo',
      url='http://github.com/lisunshiny/repostats',
      author='Liann Sun',
      author_email='lisunshiny@gmail.com',
      license='MIT',
      packages=['repostats'],
      install_requires=[],
      scripts=['bin/repostats'],
      zip_safe=False)
