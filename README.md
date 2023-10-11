# FlyPy

Just an experimentation to try and setup a python template project.
First project file: gen_test01.py = test data generator.

## Structure

my_project/
│
├── README.md        # Documentation about your project
├── .gitignore       # Specifies files/directories to be ignored by Git
├── requirements.txt # List of project dependencies
├── src/             # Source code directory
│   ├── main.py      # Main Python script
│   └── ...
│
├── tests/           # Unit tests directory (optional)
│   ├── test_main.py # Unit tests for main.py (example)
│   └── ...
│
├── data/            # Data files (if applicable)
│   ├── input/
│   ├── output/
│   └── ...
│
└── venv/            # Virtual environment (if used)

## Installation

Instructions on how to install and set up the project.

### setup new project

...Using VScode & Git

**Step 1: Install VSCode and Git**
If you haven't already, download and install Visual Studio Code from the official website (https://code.visualstudio.com/) and Git from the Git website (https://git-scm.com/downloads). Make sure both are properly installed and accessible from your command line or terminal.

**Step 2: Create a Project Directory**
Choose or create a directory on your computer where you want to store your project. This will be your project's root directory.

**Step 3: Open VSCode**
Open VSCode by clicking on its icon or running code from your terminal/command prompt.

**Step 4: Open the Project Directory**
In VSCode, go to "File" -> "Open Folder" and select the project directory you created in Step 2. This will open your project in VSCode.

**Step 5: Initialize a Git Repository**
To start tracking your project with Git, you need to initialize a Git repository in your project directory:

a. Open the integrated terminal in VSCode by clicking "View" -> "Terminal" or by pressing Ctrl+Backtick (`) on your keyboard.

b. Navigate to your project directory using the terminal. For example:
cd path/to/your/project

c. Run the following command to initialize a Git repository:
git init

**Step 6: Create a .gitignore File**
Create a .gitignore file in your project directory to specify which files or directories Git should ignore. These are typically files that don't need to be tracked, such as temporary files, build artifacts, or sensitive information. You can create this file manually or use a template from https://www.gitignore.io/ based on your project's language and tools.

For example, to create a basic .gitignore file for Python projects, you can run:<br>
`echo "__pycache__/" > .gitignore`<br>
`echo ".DS_Store" >> .gitignore`

**Step 7: Add and Commit Files**
a. Create or copy your Python test data generator script into your project directory.

b. Back in the integrated terminal, use the following Git commands to add and commit your files:<br>
`git add .`<br>
`git commit -m "initial commit"`

**Step 8: Create a Remote Repository (e.g., GitHub)**
If you want to host your project on a remote Git repository, like GitHub, GitLab, or Bitbucket, follow these steps:

a. Create an account on the chosen platform if you don't have one.

b. Create a new repository on the platform (e.g., on GitHub, click the "+ New" button).

c. Follow the platform's instructions to add a remote repository URL to your local repository. For example, GitHub provides a URL like https://github.com/username/repository-name.git.

d. Use the following Git command to add the remote repository:<br>
`git remote add origin <remote-repo-url>`

e. Push your code to the remote repository:<br>
`git push -u origin master`

**Step 9: Verify on the Remote Repository**
Visit your remote repository on the platform (e.g., GitHub) to ensure your code has been successfully pushed and is now hosted online.

That's it! You've now set up a project in VSCode, initialized a Git repository, and pushed your code to a remote repository. You can continue to develop your Python test data generator, make changes, commit them, and push updates to your Git repository as needed.



## Usage

How to use the project.

### pip
#### requirements.txt

* Make list of installed packages (+ update list)<br>
`pip freeze > requirements.txt`

* Alternative:
You can use the following code to generate a requirements.txt file:<br>
`pip install pipreqs`<br>
`pipreqs /path/to/project`

The benefits of using pipreqs from its GitHub.<br>
Why not pip freeze?

pip freeze only saves the packages that are installed with pip install in your environment.
pip freeze saves all packages in the environment including those that you don't use in your current project (if you don't have virtualenv).
and sometimes you just need to create requirements.txt for a new project without installing modules.

[link to source](https://stackoverflow.com/questions/31684375/automatically-create-file-requirements-txt)

* Check for missing packages<br> 
`python -m pip check`

* Check outdated packages in list:<br>
`pip list --outdated`

[link to source](https://learnpython.com/blog/python-requirements-file/#:~:text=You%20can%20do%20it%20as,with%20pip%20list%20%2D%2Doutdated%20.&text=Step%202%3A%20Upgrade%20the%20required,with%20pip%20install%20%2DU%20PackageName%20.&text=It%20is%20also%20possible%20to,U%20%2Dr%20requirements.txt%20.)

* Check unused, missing or transitive packages

You can find obsolete dependencies by using deptry, 
a command line utility that checks for various issues with a project's dependencies, 
such as unused, missing or transitive dependencies.

Add it to your project with:<br>
`pip install deptry`

and then run<br>
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