# TaekOnline

This is a project for database course of MAC of University of Windsor.

Taekonline is a Python/Django Web Application that uses SQLite Database.

To run the application in dev mode, you must have Python 3.6.7 installed.

1 - Extract the source-code of the project
```
unzip taekonline-master.zip
```
2 - Create a virtual enviroment
```
mkdir env
python3 -m venv env/taekonline
source env/taekonline/bin/activate
```
3 - Install the required libs
```
cd taekonline-master/
pip install -r requirements.txt
```

4 - Collect static files
```
python manage.py collectstatic
```
5 - Run the system:
```
python manage.py runserver
```
6 - Open a browser at [http://localhost:8000](http://localhost:8000)
