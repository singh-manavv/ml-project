from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    The function `get_requirements` takes a file path as input and returns a list of strings.
    
    :param file_path: A string representing the file path of the requirements file
    :type file_path: str
    """
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
    
    return requirements
    


setup(
    name='ML Project',
    version='0.0.1',
    author='Manvendra Singh',
    author_email='manvendras2608@gmail.com',
    packages=find_packages(),
    install_requires=['numpy','pandas']
    
)