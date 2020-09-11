import setuptools

setuptools.setup(
    name='mobile_client',
    version='1.0.0',
    packages=setuptools.find_packages(),
    url='https://github.com/GlueHome/mobile-client-python',
    license='MIT',
    author='Glue Tech',
    author_email='tech@gluehome.com',
    description='Glue Mobile API client package',
    python_requires='>=3.4',
    install_requires=[
        'requests',
        'dataclasses-json',
        'beautifulsoup4',
        'warrant'
    ],
    extras_require={
        'dev': [
            'pytest'
        ]
    }
)
