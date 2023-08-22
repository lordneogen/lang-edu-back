from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Text(models.Model):  
    
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        
    title = models.TextField(null=False)

    text  = models.FileField(upload_to="text/",null=False)

    def __str__(self):
        return str(self.pk)+' '+ self.title

    class Meta:

        managed = True
        db_table = 'text'
        verbose_name = 'Текста'
        verbose_name_plural = 'Текст'