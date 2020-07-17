import bootstrap_datepicker_plus as datetimepicker
import django_filters

from app.models import MyModel


class MyModelFilter(django_filters.FilterSet):
    date_field = django_filters.DateFilter(
        widget=datetimepicker.DatePickerInput(
            format='%Y-%m-%d',
            options={
                'locale': 'ja',
                'dayViewHeaderFormat': 'YYYY年 MMMM',
            }
        ),
    )
    datetime_field = django_filters.DateTimeFilter(
        widget=datetimepicker.DateTimePickerInput(
            format='%Y-%m-%d %H:%M:%S',
            options={
                'locale': 'ja',
                'dayViewHeaderFormat': 'YYYY年 MMMM',
            }
        ),
    )
    class Meta:
        model = MyModel
        fields = ['date_field', 'datetime_field']
