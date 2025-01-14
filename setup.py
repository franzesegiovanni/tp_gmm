from setuptools import setup, find_packages

setup(
    name='tp_gmm',
    version='0.1.0',
    description='Task Parameterized Gaussian Mixture Models',
    author='Giovanni Franzese, BatyaGG',
    author_email='g.franzese@tudelft.nl',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
],
    # Add other dependencies here
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
