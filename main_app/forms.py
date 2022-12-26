from django.forms import ModelForm
from .models import Feeding
# import datepicker from bootstrap django date picker module on google
# https://pypi.org/project/django-bootstrap-datepicker-plus/
from bootstrap_datepicker_plus.widgets import DatePickerInput

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']
    widgets = {
        'date': DatePickerInput()
    }
    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['date'].widget = DateTimePickerInput()
    #     return form
    
