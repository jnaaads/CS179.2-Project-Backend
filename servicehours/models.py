from django.db import models

# Create your models here.

class Student(models.Model):
	id_number = models.IntegerField(max_digits=6)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	year = models.IntegerField(max_digits=1)
	course = models.CharField(max_length=20)
	service_hours_todo = models.DecimalField(max_digits=5, decimal_places=2)
	service_hours_done = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)

class Task(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=400)
	duration_in_hours = models.DecimalField(max_digits=5, decimal_places=2)
	isDone = models.BooleanField()

	def __str__(self):
		return self.name

class Office(models.Model):
	name = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	tasks = models.ForeignKey(Task, on_delete=models.CASCADE)

	def __str__(self):
		return self.name