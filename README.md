# LMRC-Boards
A Notice Board in development for Lucknow Metro Railway Corporation. 
Developed for uploading and deleting documents. 

## Running the Project Locally

First,clone the repository to your local machine:

```bash
git clone https://github.com/mritunjaysharma394/LMRC-Boards.git
```
Change the directory to LMRC-Boards

``` bash
cd LMRC-Boards
```

Install the requirements:

```bash
pip install -r requirements.txt
```


Create the database:

```bash
python manage.py migrate
```
Create the Super User:

```bash
python manage.py createsuperuser
```
Write your username and password that shall be used for admin page.

Migrate again

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

Go to admin Page **127.0.0.1:8000/admin**.

Sign in using the username and password you created.

Add a new Board (name it 'Notice Board') under Boards in the admin page.

Reload **127.0.0.1:8000**.

Note use ```python3``` if ```python``` is not working.
