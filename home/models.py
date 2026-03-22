from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.TextField()
    email = models.EmailField(unique=True)
    admission_number = models.TextField(unique=True)
    branch = models.TextField()
    year = models.IntegerField()
    contact_number = models.BigIntegerField()
    component_name = models.TextField()
    componentissue_date = models.TextField()
    componentdue_date = models.TextField()
    faculty_referred = models.TextField()

    class Meta:
        db_table = 'students'  # This forces the table name to be 'students'
