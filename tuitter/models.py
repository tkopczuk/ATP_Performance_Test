from django.contrib.auth.models import User
from django.db import models

class Tuit(models.Model):
    class Meta:
        get_latest_by = "added"
    user    = models.ForeignKey(User, null=False)
    status  = models.CharField(max_length=160, blank=False, null=False)
    added   = models.DateTimeField(auto_now_add=True, null=False)