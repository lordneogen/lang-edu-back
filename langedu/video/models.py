from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Videos(models.Model):  
    
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        
    title = models.TextField()

    video  = models.FileField(upload_to="videos/",null= True)
    
    str  = models.FileField(upload_to="subs/",null= True)
    

    def __str__(self):
        return str(self.pk)+' '+ self.title

    class Meta:

        managed = True
        db_table = 'videos'
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
