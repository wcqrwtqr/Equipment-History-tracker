from django.db import models

# Create your models here.
class jobs(models.Model):
    jobid = models.CharField(max_length = 20 ,unique=True,blank=False)
    client = models.CharField(max_length=255,blank=False)
    field = models.CharField(max_length=255,blank=True, null=True)
    well = models.CharField(max_length=255,blank=False, null=True)
    country = models.CharField(max_length=255,blank=False,default='Iraq')
    bu = models.CharField(max_length= 3, default='KIU', null=True, blank=True)
    bl = models.CharField(max_length= 3, default='SWT', null=True, blank=True)
    description = models.CharField(max_length= 800, blank=True, null=True)
    iscontract = models.BooleanField(default=True, null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(blank=True,null=True)
    # image = models.ImageField(null=True, blank=True)
    # updated = models.DateTimeField(auto_now_add=True,blank=True)
    # created = models.DateTimeField(auto_now_add=True, blank=True)

    # def get_absolute_url(self):
    #     return reverse('jobs_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s %s'% (self.jobid, self.client, self.well)

    class Meta:
        ordering = ['client']
