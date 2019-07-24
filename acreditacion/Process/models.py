from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    id_user = models.CharField(max_length=10, blank=True,null=True)
    status = models.CharField(max_length=1, default="1",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True) 

class Process(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    id_user = models.CharField(max_length=50,blank=True, null=True)
    user_list = models.CharField(max_length=200,blank=True, null=True)
    documents_list = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    status_process = models.CharField(max_length=10,blank=True, null=True,default='0')
    status = models.CharField(max_length=1, default="1",blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True) 

# Fases
class Phase(models.Model):
    id_process = models.CharField(max_length=10,blank=True, null=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True) 
    status_phase = models.CharField(max_length=15, blank=True, null=True,default='0')
    tasks_list = models.CharField(max_length=200, blank=True, null=True)
    documents_list = models.CharField(max_length=200,blank=True, null=True)
    final_report_doc = models.CharField(max_length=200, blank=True, null=True)
    continues_doc = models.CharField(max_length=200, blank=True, null=True)
    finished = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, default="1",blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True) 

# Critterios

class Criteria(models.Model):
    id_process = models.CharField(max_length=10,blank=True, null=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    documents_list = models.CharField(max_length=200,blank=True, null=True)
    status = models.CharField(max_length=1, default="1",blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True) 

# Indicador
class Indicator(models.Model):
    id_criteria = models.CharField(max_length=10,blank=True, null=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, default="1",blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True) 

class Task(models.Model):
    id_indicator = models.CharField(max_length=10,blank=True, null=True)
    id_phase = models.CharField(max_length=10,blank=True, null=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.CharField(max_length=25, blank=True, null=True)
    end_date = models.CharField(max_length=25, blank=True, null=True)
    user_list = models.CharField(max_length=200,blank=True, null=True)
    close_date = models.CharField(max_length=25, blank=True, null=True)
    documents_list = models.CharField(max_length=200,blank=True, null=True)
    status_task = models.CharField(max_length=10, blank=True, null=True,default='0')
    status = models.CharField(max_length=1, default="1",blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True) 
    
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name