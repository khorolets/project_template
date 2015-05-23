Start new project like this
`django-admin.py startproject --template=https://github.com/regqueryvalueex/project_template/zipball/master`

Rename project to YOUR real projectname.
Create your local settings in settings directrory.
Provide readme for your project.
Your ready to go.
If you wish to make random string for your SECRET_KEY setting, you just need to type the following in interactive mode:

````
import string
from django.utils.crypto import get_random_string

print "SECRET_KEY = '%s'" % get_random_string(length=75, allowed_chars=string.digits + string.letters + string.punctuation)
Just copy/paste this in your settings file.
```