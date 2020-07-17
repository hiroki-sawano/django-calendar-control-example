from django_filters.views import FilterView
from django.urls import path, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from app.forms import MyModelForm
from app.filters import MyModelFilter
from app.models import MyModel

app_name = 'app'
urlpatterns = [
    path('my-model/new',
         CreateView.as_view(
             form_class=MyModelForm,
             template_name='app/create_update.html',
             success_url=reverse_lazy('app:search'),
         ),
         name='create'),
    path('my-model/<int:pk>',
         UpdateView.as_view(
             model=MyModel,
             form_class=MyModelForm,
             template_name='app/create_update.html',
             success_url=reverse_lazy('app:search'),
         ),
         name='update'),
    path('my-model/search',
         FilterView.as_view(
             filterset_class=MyModelFilter,
             template_name='app/search.html',
         ),
         name='search'),
]
