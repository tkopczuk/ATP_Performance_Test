from django.contrib.auth.models import User
from django.db import models
from ATP_Performance_Test.ext.django_registration.registration.signals import user_registered
from ATP_Performance_Test.ext.django_registration.registration.models import RegistrationProfile

class TuitterUserProfile(models.Model):
    """
        Augumented user profile
    """
    picture = models.CharField(max_length=1024)
    user    = models.ForeignKey(User, null=False, unique=True)

# Connected signals
def createUserProfileAndActivate(sender, user, request, **kwargs):
    TuitterUserProfile.objects.get_or_create(user=user)
    User.objects.filter(id=user.id).update(is_active=True)
    RegistrationProfile.objects.filter(user=user).update(activation_key="ALREADY_ACTIVATED")
user_registered.connect(createUserProfileAndActivate)