## Introduction

#### Hello Pyclub. Welcome to official Python Django club Github repository.
On every wednesday, this repository will be updated, you can check the code here.

## Installation guide

0. If you haven't downloaded the Git for your system, download it

    For Windows:
      Download from here: https://git-scm.com/download/win

    For Linux/Mac:
    Install the package by
    `
    $ sudo apt-get install git
    `

1. Clone repository 

    `
    git clone https://github.com/jai-singhal/pyclub
    `
    
2. cd to repository.

3. Create a virtualenv by following command
    For Linux/Mac: 
    ` virtualenv -p python3 .
    `
    
    For Windows: 
    `
    virtualenv .
    `

4. Activate virtualenv 

    For Linux/mac: 
    `
    source bin/activate
   `
   
    For Windows: 
    `
    .\scripts\activate
    `

5. Install required packages(pip for windows else pip3)

    `
    pip3 install -r requirements.txt
    `

6. cd to src and run the server (python for windows else python3)

    `
    python3 manage.py runserver
    `
