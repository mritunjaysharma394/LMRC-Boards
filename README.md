# LMRC-Boards
A Notice Board in development for Lucknow Metro Railway Corporation

## Running the Project Locally

First,clone the repository to your local machine:

```bash
git clone https://github.com/mritunjaysharma394/LMRC-Boards.git
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

Add a new Board under Boards in the admin page

Reload **127.0.0.1:8000**.

