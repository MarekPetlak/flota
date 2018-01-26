from datetime import timezone

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import View

from django.shortcuts import redirect
from .models import Cars, Capacities
from .forms import UserForm, CapacityForm


# from django.http import Http404

def capacity_add(request):
    form = CapacityForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('capacities-index')

    return render(request, "cars/capacities-edit.html", {'form': form})


def capacity_index(request):
    return render(request, 'cars/capacities-index.html', {'items': Capacities.objects.all()})


class IndexView(generic.ListView):
    template_name = 'cars/index.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Cars.objects.all()


class DetailView(generic.DetailView):
    model = Cars
    template_name = 'cars/detail.html'


class CreateView(generic.CreateView):
    model = Cars
    fields = []


class UpdateView(generic.UpdateView):
    model = Cars
    fields = []


class DeleteView(generic.DeleteView):
    model = Cars
    success_url = reverse_lazy('cars:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'cars/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.user

                    return request('cars:index')

        return render(request, self.template_name, {'form': form})
