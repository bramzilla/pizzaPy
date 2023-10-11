# FlyPy

Just an experimentation to try and setup a python template project.
First project file: gen_test01.py = test data generator.

## Installation

Instructions on how to install and set up the project.

## Usage

How to use the project.

### Pip
#### requirements.txt

* Make list of installed packages (+ update list)
`pip freeze > requirements.txt`

* Alternative:
You can use the following code to generate a requirements.txt file:
`pip install pipreqs`
`pipreqs /path/to/project`

The benefits of using pipreqs from its GitHub.
Why not pip freeze?

pip freeze only saves the packages that are installed with pip install in your environment.
pip freeze saves all packages in the environment including those that you don't use in your current project (if you don't have virtualenv).
and sometimes you just need to create requirements.txt for a new project without installing modules.

[link to source](https://stackoverflow.com/questions/31684375/automatically-create-file-requirements-txt)

* Check for missing packages 
`python -m pip check`

* Check outdated packages in list:
`pip list --outdated`

[link to source](https://learnpython.com/blog/python-requirements-file/#:~:text=You%20can%20do%20it%20as,with%20pip%20list%20%2D%2Doutdated%20.&text=Step%202%3A%20Upgrade%20the%20required,with%20pip%20install%20%2DU%20PackageName%20.&text=It%20is%20also%20possible%20to,U%20%2Dr%20requirements.txt%20.)

* Check unused, missing or transitive packages

You can find obsolete dependencies by using deptry, 
a command line utility that checks for various issues with a project's dependencies, 
such as unused, missing or transitive dependencies.

Add it to your project with:
`pip install deptry`

and then run
`deptry .`

Example output:
Scanning 2 files...

requirements.txt: DEP002 'pandas' defined as a dependency but not used in the codebase
Found 1 dependency issue.

Note that for the best results, 
you should be using a virtual environment for your project, see e.g. [here](https://stackoverflow.com/a/41799834/8037249).

[link to source](https://stackoverflow.com/questions/25376213/delete-unused-packages-from-requirements-file)

(Warning: When using pip to install deptry, make sure you install it within the virtual environment of your project. Installing deptry globally will not work, since it needs to have access to the metadata of the packages in the virtual environment.) [github source](https://github.com/fpgmaas/deptry)

## Contributing

Guidelines for contributing to the project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.