from setuptools import setup, find_packages

setup(
    name='tesouroapi',
    version='0.1.0',
    description='API para consulta de dados dos leilões do Tesouro Nacional',
    author='Cleber Gabriel Nicolussi Zanin',
    author_email='clebergnz@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
