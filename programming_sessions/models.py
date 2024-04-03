from django.db import models

# Create your models here.
class Meeting(models.Model):
    host_name=models.CharField(max_length=100)
    title=models.TextField()
    description=models.TextField()
    technology=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    duration=models.FloatField()
    skill_level=models.CharField(max_length=100)
    session_link=models.CharField(max_length=100)
    # participants=
    status=models.CharField(max_length=100)


