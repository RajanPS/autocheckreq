# autocheckreq
This script automatically checks for missing requirements to be installed based on the requirements file specified in the python virtual environment.

This script basically get's your pip freeze and checks whether all the packages mentioned in the requirements file are installed or not. List all the requirements file to be considered in the yaml file along with the path of where it is. If any missed requirements are indentified, it is listed for you to install or ignore.

you can manually try it out by running the script from the path where you have the req.yml file. Usually from the root of the project.(virtualenv should be active while running the script)

To automate missing requirements check, you can use [autoenv] (https://github.com/kennethreitz/autoenv) module.
add the below lines to the .env file. Change the script path relative to the root directory

<pre><code>
if [ -e "scripts/checkreq.py" ]
then
    python scripts/checkreq.py
fi
</code></pre>

# Steps
1. add req.yml file to the project root
2. mention the requirement files to be considered and path of it in the req.yml
3. save the checkreq.py script some where inside your project directory
4. auto call the script when you cd into project root using [autoenv] (https://github.com/kennethreitz/autoenv) .env file
5. script will be called each time when you cd into the root folder
5. missing requirements will be listed if any and you can either install them or ignore
