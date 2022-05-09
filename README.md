# Learning Flask framework
![GitHub last commit](https://img.shields.io/github/last-commit/ahmad-buhari/flask-project)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ahmad-buhari/flask-project) 



| Topic | Description |
| :---: | :---: |
| [Setup](https://github.com/ahmad-buhari/flask-project#setup) | Project setup details |
| [Project Background](https://github.com/ahmad-buhari/flask-project#background) | Purpose of the project |
| [Notes](https://github.com/ahmad-buhari/flask-project#notes) | Things I've learn throughtout the project |
| [Flask command line notes](https://github.com/ahmad-buhari/flask-project#flask-web-server-commands) |  Quick reference for flask cli |


## Setup
- Codebase python
- Pip module - flask
- poetry for python virtual env
- Running virtual machine with CentOS Stream


## Background
A web server's purpose is to serve content. In the past, websites were written in HTML and CSS manually per page. Now, a framework is utilized to build web pages from a template enabling faster development and minimizing overhead. In this project, I'll be using the Flask framework to build a website.

### Notes
- New pages are serve with this constructor of @app.route("/"). The `(" ")` identifies a new page.
- Set the run operation for the web script.
- `control flow` is dicated by incoming HTTP request. 
- A view function is only called if its URL is requested.


### Flask web server commands
Run these command in the linux shell.
- Run `export FLASK_APP=code.py` to set where Flask will run the codebase.
- Run `export FLASK_ENV=development` to enable development tools for debugging. 
- Run `flask run` to start the web server.






