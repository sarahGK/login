This is a Django login app connet to a PostgreSQL instance on AWS

1.login: let user to register and login 
2.reservation: save reservation information into database
3.streetparking/settings:all the settings for apps and connecting to database on AWS

#----Useful command---#
1.connect to DB instance on AWS locally:
psql --host=xpostgres.c1nvk5oppivu.us-west-1.rds.amazonaws.com --port=5432 --username=xin —password --dbname=ridecell    'PASSWORD': 'tMrWDk3N'
2.starts the development server on the internal IP at port 8000:
python manage.py runserver 0.0.0.0:8000
3.create the tables in the database before we can use them. To do that, run the following command:
$ python manage.py migrate
4.Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.

#---Good Web development practice---#
1.If you want to change the way the page looks, you’ll need templated. Django’s template system separates the design from Python by creating a template that the view can use.The project’s TEMPLATES setting describes how Django will load and render templates. 
2.Whenever you create a form that alters data server-side, use method="post" and always return an HttpResponseRedirect after successfully dealing with POST data.
3.Dealing with url request:getting data from the database according to a parameter passed in the URL, loading a template and returning the rendered template.
4.Extending User Model Using a One-To-One Link: creating a new Django Model to store the extra information that relates to the User Model.This strategy results in additional queries or joins to retrieve the related data. Basically all the time you access an related data, Django will fire an additional query. But this can be avoided for the most cases. 
5.Form and field validation:Form validation happens when the data is cleaned.Three types of cleaning methods are run during form processing. These are normally executed when you call the is_valid() method on a form. 
