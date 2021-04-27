import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        long_description = f.read()
else:
    long_description = 'kw3pan'

setuptools.setup(
    name='kw3pan',
    version='0.0.6',
    author='Kristóf-Attila Kovács',
    description='kw3pan',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kkristof200/py_web3_pancakeswap',
    packages=setuptools.find_packages(),
    install_requires=[
        'jsoncodable>=0.1.2',
        'kw3>=0.0.6'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
)