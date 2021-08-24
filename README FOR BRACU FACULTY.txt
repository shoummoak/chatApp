MVT pattern used, not MVC

Django Projects can not be transformed into calssical MVC projects. This is 
because of how the Django framework functions. Instead, Django projects follow
the MVT (Model View Template) pattern. The actual code follows the MVT pattern, 
however I have still created a DUMMY MVC Structure folder that contains relevant 
files.

MVT Pattern

The MVT structure separates different parts of the software into modules called 'apps'. 
For example, this projcet currently has two different apps with separate objectives. The 'accounts' 
app for handling user accounts, registration, login. There is also the 'chat' app which
is for chatting with other users. It involves messages and socket programming.

Each app has its own set of important files relevant to the MVT structure. Some these 
important files are 'models.py', 'views.py', and a template subdiretory containing html files. 
We can not centralize these files as done in the in the MVC pattern. For example, we can not 
store different 'models.py' files in the same directory since they have to be present in their 
own app directory.

In MVT, the models.py is for creating the necessary database tables and creating relations
between different tables. view.py acts as the middle man between models.py and the template 
html files. views.py provides the logic needed for the respective app, it decides what page
to display to the user, and it communicates witht he databse as well. The template html files 
are simply the html files of the respective app that we want to display to the user.