from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView  # new

from .models import Department


class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/home.html'


class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'departments/new.html'
    fields = '__all__'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'departments/details.html'
