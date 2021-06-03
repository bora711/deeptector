from django.db import models


class D1(models.Model):
    TIME = models.IntegerField(db_column='TIME', blank=True, null=True)  # Field name made lowercase.
    LOSS = models.FloatField(db_column='LOSS', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'D1'
    


class D2(models.Model):
    age_group = models.IntegerField(db_column='age_group', primary_key=True)
    EX_HIGH = models.FloatField(db_column='EX_HIGH', blank=True, null=True)  # Field name made lowercase.
    EX_MID = models.FloatField(db_column='EX_MID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'D2'


class Member(models.Model):
    id = models.CharField(db_column='id', primary_key=True, max_length=50)
    mask = models.TextField(db_column='mask', )
    name = models.CharField(db_column='name', max_length=50)
    in_enter = models.TimeField(db_column='in_enter')
    bodyTemp = models.CharField(db_column='bodyTemp', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='state', max_length=50)
    
    class Meta:
        managed = False
        db_table = 'member'