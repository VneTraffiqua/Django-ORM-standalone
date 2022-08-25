# Пульт охраны банка

Repository with a website for the lesson "Writing a bank guard console" course [dvmn.org](https://dvmn.org/modules/).

This is an internal repository for an employee of the Shining Bank. If you got into this repository by accident, then you will not be able to run it, because. you do not have access to the database, but you can freely use the layout code or see how the database queries are implemented.

The control panel can be connected to a remote database. The site displays a list of bank employees with active access cards and a list of those who are currently in the vault, indicating the time of stay.

The site also allows you to view the history of storage visits for any selected employee. For each visit, the date, time, and length of stay in the vault are displayed.

If an employee is in storage for more than an hour, the system marks this visit as suspicious.

## Установка и запуск сайта
Download code:
```
git clone https://github.com/vitaliy-pavlenko/django-orm-watching-storage.git
```
Change to the project directory:
```
cd django-orm-watching-storage
```
Install the dependencies in the virtual environment:
```
pip install -r requirements.txt
```
Create .env file with configuration:

```
DB_SETTINGS=postgres://USER:PASSWORD@HOST:PORT/NAME
```
Launch site:
```
python manage.py runserver 8000
```
Open the site in a browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Additional settings in .env
```
SECRET_KEY=YOUR_KEY
DEBUG=true
ALLOWED_HOSTS=host1,host2
```
