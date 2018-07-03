from django.db import models

class BookinfoManager(models.Manager):
    def get_queryset(self):
        return super(BookinfoManager,self).get_queryset().filter(pk=3)
    def create_book(self,t,d):
        b = self.create(btitle=1,bpubdate=d)
        return b


# Create your models here.
class Bookinfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpubdate = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    book = models.Manager()
    book2 = BookinfoManager()

class Heroinfo(models.Model):
    hname = models.CharField(max_length=20)
    hsex = models.BooleanField(default=True)
    hcontent = models.TextField(max_length=100)
    isDelete = models.BooleanField(default=False)
    hbook = models.ForeignKey('Bookinfo')


    class Meta():
        db_table = 'heroinfo'
