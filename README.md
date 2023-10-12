# FlyPy

Just an experimentation to try and setup a python template project.
First project file: gen_test01.py = test data generator.

## Structure

my_project/<br>
│<br>
├── README.md        # Documentation about your project<br>
├── .gitignore       # Specifies files/directories to be ignored by Git<br>
├── requirements.txt # List of project dependencies<br>
├── src/             # Source code directory<br>
│   ├── main.py      # Main Python script<br>
│   └── ...<br>
│<br>
├── tests/           # Unit tests directory (optional)<br>
│   ├── test_main.py # Unit tests for main.py (example)<br>
│   └── ...<br>
│<br>
├── data/            # Data files<br>
│   ├── input/<br>
│   ├── output/<br>
│   └── ...<br>
│<br>
└── venv/            # Virtual environment<br>

## Installation

Instructions on how to install and set up the project.

### setup virtual environment

**Step 1: Open Your Terminal or Command Prompt:**
Open your terminal or command prompt and navigate to your project's root directory. You can use the cd command to change directories.<br>
`cd path\to\your\project`

**Step 2: Check Python Version (Optional):**
You can check the installed Python version by running:<br>
`python --version`

Ensure that you have the desired Python version installed. If not, you can install it from the Python website.

**Step 3: Install virtualenv (if not already installed):**
virtualenv is a Python package that allows you to create and manage virtual environments. If you don't have it installed, you can install it using pip:<br>
`pip install virtualenv`

**Step 4: Create a Virtual Environment:**
In your project's directory, you can create a virtual environment using the following command. Replace venv with the name you want for your virtual environment:<br>
`virtualenv venv`

This command will create a directory named venv in your project directory, containing the isolated environment.

**Step 5: Activate the Virtual Environment:**
To activate the virtual environment, you'll need to run a command specific to your operating system.

On Windows (PowerShell):<br>
`.\venv\Scripts\Activate`

On macOS and Linux (Bash):<br>
`source venv/bin/activate`

Once the virtual environment is activated, you'll notice that your command prompt or terminal prompt changes to show the name of the active environment (e.g., (venv)).

**Step 6: Install Dependencies:**
With the virtual environment active, you can now use pip to install the dependencies specific to your project without affecting the system-wide Python installation. For example, if you have a requirements.txt file listing your project's dependencies, you can install them with:<br>
`pip install -r requirements.txt`

**Step 7: Work in the Virtual Environment:**
You can now work on your project within the virtual environment. Any Python scripts you run, or packages you install, will be isolated to this environment.

**Step 8: Deactivate the Virtual Environment:**
When you're done working in the virtual environment, you can deactivate it. This will return you to the system-wide Python environment.
`deactivate`

The virtual environment's name in your terminal prompt will disappear, indicating that you've returned to the system Python.


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