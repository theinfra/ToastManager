from django.db import models

# Members of the club
class Member(models.Model):
	name = models.CharField(max_length=100)

	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	def __str__(self):
		return f"{self.name}"