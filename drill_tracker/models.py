from django.db import models
from django.contrib.auth.models import User

class Drills(models.Model):

    name = models.CharField(
        max_length=100, 
        null=False,
        db_column='name', 
        verbose_name='Name')
    
    link = models.CharField(
        max_length=200, 
        null=True,
        db_column='link', 
        verbose_name='URL link')
        
    sdate = models.DateTimeField(
        db_column='sdate', 
        verbose_name='Start Date')
    
    edate = models.DateTimeField(
        db_column='edate', 
        verbose_name='End Date')

    total = models.IntegerField(
        db_column='total', 
        null=False,
        verbose_name='Total Reps')
    
    user = models.ForeignKey(
        User,
        db_column = 'user_id',
        null = False,
        db_index = True,
        verbose_name = 'User',
        related_name = 'drills')


class Daily_Reps(models.Model):
    drill_date = models.DateTimeField(
        db_column='ddate', 
        verbose_name='Drill Date')
    
    reps = models.IntegerField(
        db_column='reps', 
        null=False,
        verbose_name='Total Daily Reps')
    
    drill = models.ForeignKey(
        Drills, 
        db_column='drill_id', 
        db_index=True, 
        null=False,
        blank=False, 
        verbose_name='Drill', 
        related_name='reps')
