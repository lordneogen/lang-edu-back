from django.db import models
from django.contrib.auth.models import User
from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError
# Create your models here.
def validate_text_file_extension(value):
    if not value.name.endswith('.mp4'):
        raise ValidationError('Разрешены только файлы с расширением .mp4')
    
def validate_srt_file_extension(value):
    if not value.name.endswith('.srt'):
        raise ValidationError('Разрешены только файлы с расширением .srt')
class Videos(models.Model):  
    
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
        
    title = models.TextField()

    video  = models.FileField(upload_to="videos/",null= True,validators=[validate_text_file_extension])
    
    str  = models.FileField(upload_to="subs/",null= True,validators=[validate_srt_file_extension])
    

    def __str__(self):
        return str(self.pk)+' '+ self.title

    class Meta:

        managed = True
        db_table = 'videos'
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
