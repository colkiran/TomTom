from django.db import models

# Create your models here.
class Books(models.Model):
    Bookname = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)

    def __unicode__(self):
        return self.Bookname

    class Meta:
        verbose_name_plural = 'Books'