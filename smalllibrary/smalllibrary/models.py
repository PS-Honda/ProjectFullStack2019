from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Bindding(models.Model) : 
    #type of book hard copy or soft copy
    name = models.CharField(max_length=64)
    def __str__ (self):
        return self.name 

class Pubilsher(models.Model) : 
    name = models.CharField(max_length=64)
    def __str__ (self):
        return self.name 

class Book(models.Model) :
    title  = models.CharField(max_length=255)
    cover = models.ImageField(blank=True,null=True,upload_to='smalllibrary/static/images/')
    isbn_10 = models.CharField(max_length=15)
    author = models.CharField(max_length=255)
    bindding = models.ForeignKey(Bindding,on_delete=models.PROTECT)
    year = models.PositiveSmallIntegerField()
    pubilsher = models.ForeignKey(Pubilsher,on_delete=models.PROTECT)
    borrow_status = models.BooleanField()
    def __str__ (self):
        return self.title 

class Borrow(models.Model) :
    borrower = models.ForeignKey(User,on_delete=models.PROTECT)
    book = models.ForeignKey(Book,on_delete=models.PROTECT)
    def __str__ (self):
        return self.borrower 

class Transaction(models.Model) :
    book = models.ForeignKey(Book,on_delete=models.PROTECT)
    actor = models.ForeignKey(User,on_delete=models.PROTECT)
    action = models.CharField(max_length=32)
    credit = models.DateTimeField(auto_now=True)
    def __str__(self) :
        return self.book