from django.db import models
import uuid
import secrets
# Create your models here.

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.UUIDField(
        default=uuid.uuid4 , 
        editable=False,
        unique=True
    )
    name = models.CharField(max_length=100)
    secret_token = models.CharField(
        max_length=100,
        unique=True,
        default=secrets.token_hex(16)
    )
    
    
class Destination(models.Model):
    account = models.ForeignKey(
        Account , 
        on_delete=models.CASCADE,
        related_name="destinations"
    )
    url = models.URLField()
    method = models.CharField(max_length=10)
    headers = models.JSONField()

    def __str__(self):
        return f"{self.account.email} on destination url : {self.url}"
    
    