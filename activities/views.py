# activities/views.py

from django.views.generic import ListView
from django.shortcuts import redirect
from activities.models import Activity
from activities.forms import ActivityForm

class ActivityListView(ListView):
    model = Activity
    template_name = 'home.html'
    context_object_name = 'activities'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ActivityForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)