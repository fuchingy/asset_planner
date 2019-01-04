import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='asset_planner',
    version='1.0.0',
    license='MIT',
    maintainer='Fu-Ching Yang',
    maintainer_email='fcyangesl@gmail.com',
    description='An app to monior, evaluate and plan personal assets',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
