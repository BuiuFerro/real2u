# real2u
Repository for a job test

# User Interface (frontend):

## Technologies:

**[Yarn](https://www.npmjs.com/package/yarn)** 
It's as package management of the frontend. A personal option over npm.
```
$ npm install yarn
```

**[React](https://pt-br.reactjs.org/)** 
A JavaScript library for building the frontend.

### Installing dependencies:
```
$ yarn add create_react-app react-scripts
```
### Building the client:
```
yarn build
```

# Server (backend):

## Technologies:

**[Python](https://www.python.org/downloads/)** 
Using the 3.8.3v. Access the link and look for the download section that 
best fits your OS.

**[Flask](https://flask.palletsprojects.com/en/1.1.x/)** 
Using to build the backend server of the application.

### Creating a virtual enviroment:
```
$ pip install virtualenv
$ virtualenv nome_da_virtualenv
```
### Activating the virtualenv:
```
$ .\nome_da_virtualenv\Scripts\activate
```

### Installing dependencies with pip:
OBS: pip is alread install in this Python version.
```
$ pip install -r requirements
```

### Initializing the app:
```
$ cd backend
$ python main.py
```
