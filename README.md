# SB Admin

- Create .env file according to .env.example file to set environment variables.

- Need Tensorflow 2.2.0 to work properly.

- Then run following commands in given order to start project.

```
conda create --name ml python=3.7
```

```
conda activate ml
```

```
pip install -r requirements.txt
```

```
python manage.py createsuperuser
```

```
python manage.py collectstatic
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py runscript generate_data -v3
```

```
python manage.py runserver_plus
```

## Extra Commands

### Dump database table to a file.

```
python manage.py dumpdata --indent 2 <app> > <filename.json>
```

### Load data to database from given files. Files should be in 'fixtures' folder

```
python manage.py loaddata <filename.json>
```

### Makes the current database have the same data as the fixture(s).

```
python manage.py syncdata data.json
```

## To dump the data from all the models in a given Django app

```
python manage.py dumpscript reservoirs > scripts/reservoirs_data.py
```

## To reset a given app, and reload with the saved data

```
python manage.py reset appname
```

```
python manage.py runscript testdata
```

### To create new module within given project.

```
python manage.py startapp <app>
```

## Run this to auto generate water_level data

```
python manage.py runscript generate_water_level_data
```

## Create new user

````
python manage.py createsuperuser
```
````
