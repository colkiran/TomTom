from django.db import models

# Create your models here.
class Books(models.Model):
    bookname = models.CharField(max_length = 50)
    author = models.CharField(max_length=50)

    def __unicode__(self):
        return self.bookname

