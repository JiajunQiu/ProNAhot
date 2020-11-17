from setuptools import setup
from setuptools import find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as file:
        return file.read()


setup(
    name='pronahot',
    version='0.1.0',
    description='ProNAhot: Predicting protein-DNA, protein-RNA and protein-protein binding hot-spots from sequence',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3.4',
    ],
    url='https://github.com/JiajunQiu/ProNAHot',
    author='Jiajun Qiu',
    author_email='jiajunqiu@hotmail.com',
    license="MIT License",
    packages=find_packages(exclude=['tests']),
    install_requires=[
        # ML
        'numpy == 1.14.*',
        'scipy == 0.14.0',
        'scikit-learn == 0.19.1',
        'PyWavelets >= 0.5.2',

    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
)
