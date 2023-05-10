from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=50, unique=True)
    describe = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()