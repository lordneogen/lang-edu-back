from django.db import models

# Create your models here.

class Text(models.Model):  
        
    title = models.TextField()

    text  = models.FileField(upload_to="text/",null= True)

    def __str__(self):
        return str(self.pk)+' '+ self.title

    class Meta:

        managed = True
        db_table = 'text'
        verbose_name = 'Текста'
        verbose_name_plural = 'Текст'