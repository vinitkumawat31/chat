from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChatMessage(models.Model):
	message = models.CharField(max_length=500)
	room = models.CharField(max_length=200)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	timestamp = models.DateTimeField(default = timezone.now())
	def __str__(self):
		return self.message
