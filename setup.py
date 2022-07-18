from setuptools import setup, find_packages  
  
setup(  
    name = "EasyGitTool",  
    version = "V0.2-dev",
    long_description = "EasyGitTool for python",  
    license = "Mozilla Public License Version 2.0",
    url = "https://easygittool.github.io",  
    author = "Mryan2005",  
    author_email = "A2564011261@163.com",  
    packages = find_packages(),  
    include_package_data = True,  
    platforms = "any",  
    install_requires = [],  
    keywords=["EasyGitTool"],
    scripts = [],  
    entry_points = {  
        'console_scripts': [  
            'gt = EasyGitTool.main:main'  
        ]  
    }  
)
