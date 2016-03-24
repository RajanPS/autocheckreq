# autocheckreq
This script automatically checks for missing requirements to be installed based on the requirements file specified in the python virtual environment

1) add req.yml file to the project root (refer the sample file)
2) mention the requirement files to be considered and path of it in the req.yml
3) save the script some where inside your project directory
4) auto call the script using autoenv in the project root
5) missing requirements will be listed and you can either install them or ignore
