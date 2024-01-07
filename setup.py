from setuptools import find_packages , setup 
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements = [] 
    constant = '-e .'
    with open(file_path) as file_object:
        requirement = file_object.readlines()
        requirement = [i.replace('\n','') for i in requirement]
    if constant in requirement:
        requirement.remove('-e .')
    return requirement

setup(
    name = 'iserveu_mlp', 
    version='0.0.1',
    author='abhishek nayak',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)