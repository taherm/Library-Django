from django.db import models
from members.models import Members

class Author(models.Model):
	name = models.CharField(max_length=50)


	def __str__(self):
		return self.name

class Publication(models.Model):
	name = models.CharField(max_length=50)
	address = models.TextField()

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=100)
	isbn = models.CharField(max_length=50)
	pages = models.IntegerField(max_length=5)
	pub_n = models.ManyToManyField(Publication)
	author = models.ManyToManyField(Author)
	price = models.IntegerField(max_length=5)
	num_copy = models.IntegerField(max_length=5,default=1)

	def __str__(self):
		return self.title

class BookIssue(models.Model):
	IssueId = models.CharField(max_length=7,primary_key=True)
	MemId = models.ForeignKey(Members)
	Book = models.ForeignKey(Book)
	IssueDate = models.DateField()
	ReturnDate = models.DateField()

	def __str__(self):
		return self.IssueId
		


# Create your models here.
