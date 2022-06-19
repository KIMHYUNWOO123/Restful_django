from django.db import models

class User(models.Model):
    num = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50)  # Field name made lowercase.
    userpassword = models.CharField(max_length=50)  # Field name made lowercase.
    username = models.CharField(max_length=50)  # Field name made lowercase.
    userbirth = models.CharField( max_length=50)