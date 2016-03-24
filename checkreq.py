#!/usr/bin/env python 

# req.yml file should be added to the directory from where this script needs to be called
# *** sample content of req.yml file ***
# path: '.'
# requirements: ['requirements_dev.txt', 'requirements_prod.txt']

# To automate the process. call this script from autoenv's .env file.
# check out more about autoenv - https://github.com/kennethreitz/autoenv


# Python 2 and 3:
from __future__ import print_function
import os
import subprocess
import yaml
import re


def main():
    if os.path.isfile('req.yml'):
        data = yaml.load(open('req.yml', 'rb').read())
        path = data.get('path')
        requirements = data.get('requirements')
        p = subprocess.Popen(['pip', 'freeze'], stdout=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = p.communicate()
        if stdout:
            installed_req = set(stdout.split('\n'))  # installed requirements
            listed_req = set()
            for req_file in requirements:
                req_list = open(os.path.join(path, req_file), 'r').read().split('\n')
                for item in req_list:
                    sr = re.search('^-r.*.txt', item)
                    if sr:
                        req_list.remove(item)
                req_list = filter(None, req_list)
                listed_req = listed_req | set(req_list)
            missed_list = listed_req - installed_req
            if missed_list:
                print('Below modules are not installed')
                for item in missed_list:
                    print('{0} {1}'.format('-->', item))
                if eval(input("press 1 to proceed 0 to exit?")):
                    for req_file in requirements:
                        subprocess.call(["pip", "install", "-r", os.path.join(path, req_file)])
        else:
            print(stderr)

if __name__ == '__main__':
    main()
