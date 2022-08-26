from django.db import models

# Create your models here.
class Recipient(models.Model):
    email = models.EmailField(max_length=256,unique=True)
    name = models.CharField(max_length=256,blank = True,null=True)
    company = models.CharField(max_length=256,blank=True,null = True)
    status = models.BooleanField(default=False,blank = True)
    phone = models.CharField(max_length=15,blank=True)
    errors = models.JSONField(blank=True,null=True)

    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = "Recipients"