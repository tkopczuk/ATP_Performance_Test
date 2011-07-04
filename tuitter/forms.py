from django.forms import models

from tuitter.models import Tuit

class AddTuitForm(models.ModelForm):
    class Meta:
        model = Tuit
        exclude = ('user', )