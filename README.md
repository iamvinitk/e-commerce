1) Install python 3.6.3
2) Install mysql community server
3) ```pip install -r requirements.txt```


# Commands to setup the project
1) Set up database configuration in Online_Retail>settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        //Name of the database
        'NAME': 'kompany',
        //Database password
        'PASSWORD': 'Admin@123',
        //Database user name
        'USER': 'root',
    }
}
```

2)Commands to set up project and run the development server
```
  python manage.py makemigrations
  python manage.py migrate
  //Create superuser
  python manage.py createsuperuser
  //run server
  python manage.py runserver
 ```
3)Populate the database using the excel files from db folder
  - open 127.0.0.1:8000/admin
    ![Alt text](Online_Retail/screenshots/Screenshot (2).png "Optional title")
  - add the product categories
  - add products from excel sheet using import
  

# MEMBERS
- Vinit Kanani ( [https://github.com/vinit-kanani](https://github.com/vinit-kanani) )
- Vaisakh M
