# Florida Men IP Tool
This IP Tool (developed by the *Florida Men* team) is a web application that shows public IPv4/IPv6 information from the information fetched from [IP API](https://ipapi.co). 

<br>
For easy access, a version of this project is deployed on *Heroku* and can be accessed from this [link](https://floridamen-iptool.herokuapp.com/). 

###  Developers
- **Cabral, Jose Paulo C.** -  Frontend, Operations
- **Licas, Janrey T.** -  Backend, QA
- **Lopez, Joshua Albert T.** -  Backend, QA

### Dependencies
Host Machine running Linux with the following packages installed: 
- Docker
- Python 3 with Pip

### Notes
To ensure that all functionalities are working before deployment, unit tests were provided. These are present in the `tests` directory and can be executed using the command below, preferably, inside a virtual environment (substitute `python` with `python3` and `pip` with `pip3` if the default Python installed is still Python 2).

```bash
$ pip install -r requirements.txt
$ cd tests/
$ python -m unittest
```
<br>
To deploy, simply execute the command below from the root project directory.

```bash
$ bash deploy.sh
```

*Note: Make sure that the `Dockerfile` is present in the root project directory.*

### Directory Structure
This project consists the following files and follows the directory structure below.

```bash
florida-men-iptool/
├── api.py
├── app.py
├── deploy.sh
├── Dockerfile
├── LICENSE
├── __pycache__
│   └── api.cpython-38.pyc
├── README.md
├── requirements.txt
├── templates
│   ├── 404.html
│   └── index.html
└── tests
    ├── README.md
    ├── test_api.py
    └── tests_backend.py
```
