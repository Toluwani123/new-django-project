from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Storage
import pyqrcode
import png
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class AccountLogin(LoginView):
    template_name = 'base/acclogin.html'
    fields = '__all__'
    redirect_authenticated_user: True

    def get_success_url(self):
        return reverse_lazy('banks')

class BankList(LoginRequiredMixin, ListView):
    model = Storage
    context_object_name = 'banks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banks'] = context['banks'].filter(user=self.request.user) 
        return context
class BankDetails(LoginRequiredMixin, DetailView):
    model = Storage
    context_object_name = 'bank'

class BankCreate(LoginRequiredMixin, CreateView):
    model = Storage
    fields = ['bank_name', 'account_number']
    success_url = reverse_lazy('banks')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BankCreate, self).form_valid(form)



class BankUpdate(LoginRequiredMixin, UpdateView):
    model = Storage
    fields = fields = ['bank_name', 'account_number']
    success_url = reverse_lazy('banks')

class BankDelete(LoginRequiredMixin, DeleteView):
    model = Storage
    context_object_name = 'task'
    success_url = reverse_lazy('banks')


class RegisterUser(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('banks')
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('banks')
        return super(RegisterUser, self).get(*args, **kwargs)

def qr_code(request):
   context = {}
   if request.method == 'POST':
       data = request.POST["data"]
       img = pyqrcode.create(data)
       file_name = "qr.png"
       context["qr_filename"] = file_name
       img.png(settings.MEDIA_ROOT +file_name,scale=6)           
   return render(request, 'base/qr_code.html', context)