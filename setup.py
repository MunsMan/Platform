from setuptools import setup

setup(name='Platform',
      version='0.1',
      description='A Platform for different UseCases. For more Information, please read the README.md',
      url='https://github.com/MunsMan/Platform',
      author='MunsMan',
      author_email='hendrik.munske@me.com',
      license='MIT',
      # packages=['Extensions, Functions'],
      install_requires=[
            'hashlib',
            'typing',
            'paho-mqtt'
      ],
      zip_safe=False)
