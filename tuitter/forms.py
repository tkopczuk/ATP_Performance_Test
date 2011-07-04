from django.forms import models

from ATP_Performance_Test.tuitter.models import Tuit

class AddTuitForm(models.ModelForm):
    class Meta:
        model = Tuit
        exclude = ('user', )