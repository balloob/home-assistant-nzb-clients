from setuptools import setup

setup(name='python-sabnzbd',
      version='0.1',
      description='Python API for talking to SABnzbd',
      url='https://github.com/jamespcole/home-assistant-nzb-clients',
      author='James Cole',
      license='GPLv2',
      install_requires=['requests>=2.0'],
      packages=['pysabnzbd'],
      zip_safe=True)
