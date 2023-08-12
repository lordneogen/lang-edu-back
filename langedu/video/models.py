from django.db import models

# Create your models here.

class Videos(models.Model):  
        
    title = models.TextField()

    video  = models.FileField(upload_to="videos/",null= True)
    
    str  = models.FileField(upload_to="subs/",null= True)

    user = models

    def __str__(self):
        return str(self.pk)+' '+ self.title

    class Meta:

        managed = True
        db_table = 'videos'
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
