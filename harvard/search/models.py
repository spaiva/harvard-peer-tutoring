from django.db import models
from django.core.urlresolvers import reverse

class Department(models.Model):    
	department_name = models.CharField(max_length=255)
	department_code = models.IntegerField()
	department_logo = models.FileField(null=True, blank=True)

	def get_absolute_url(self):
		return reverse('search:detail', kwargs={'pk' : self.pk})

	def __str__(self):
		return self.department_name


class School(models.Model):
	school_name = models.CharField(max_length=255)
	school_code = models.IntegerField(default=0)

	def __str__(self):
		return self.school_name


class Course(models.Model):
    
	course_code = models.CharField(max_length=50)
	course_name = models.CharField(max_length=255)
	num_tutors = models.IntegerField()
	department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
	school = models.ForeignKey(School, on_delete=models.CASCADE, default=None)
	has_tutor_request = models.BooleanField(default=False)

	def __str__(self):
		return self.course_code + ' - ' + self.course_name

