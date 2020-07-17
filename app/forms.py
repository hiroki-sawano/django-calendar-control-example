import bootstrap_datepicker_plus as datetimepicker
from django import forms

from app.models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['date_field', 'datetime_field']
        widgets = {
            'date_field': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                     'locale': 'ja',
                     'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            'datetime_field': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }
