from django.db import models
from  django.urls import reverse
# Create your models here.

class equipment(models.Model):
    asset_num = models.CharField(max_length=200,unique=True, blank=False)
    serial_num = models.CharField(max_length=200,unique=False,blank=True)
    description = models.CharField(max_length=800, null=True,blank=True)
    equ_type = models.CharField(max_length=200,null=True,blank=True)
    BU = models.CharField(max_length=4,null=True,blank=True)
    BL = models.CharField(max_length=4,null=True,blank=True)

    # def get_absolute_url(self):
    #     return reverse('far_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s'% (self.equ_type ,self.serial_num )
    class Meta:
        ordering = ['equ_type']
