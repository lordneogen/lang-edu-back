from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vocs(models.Model):  
    
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    voc_1=models.TextField(null=False)
    
    voc_2=models.TextField(null=False)
    
    voc_1_lang=models.TextField(null=False)
    
    voc_2_lang=models.TextField(null=False)
        

    def __str__(self):
        return str(self.pk)+' '+ self.voc_1 + '-' + self.voc_2 

    class Meta:

        managed = True
        db_table = 'vocs'
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'
