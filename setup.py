from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of Requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='life_insurance_coverage',
    version='0.0.1',
    author='Valli Raja Sekar',
    author_email='sekarvalliraja@gmail',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
