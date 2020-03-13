from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length = 254) # max length required
    password = models.CharField(max_length = 200)
    securityQuestion = models.CharField(max_length = 200)
    securityQuesAnswer = models.CharField(max_length = 200)

    def __str__(self):
        return self.email

class ChatTable(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'sender' )
    reciever = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'reciever')
    message = models.CharField(max_length = 365)
