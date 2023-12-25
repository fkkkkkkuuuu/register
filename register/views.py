from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from register.forms import UserCreationForm, UserRoleForm
from django.views import View
from django.contrib.auth import get_user_model







class Register(View):
    template_name = 'registration.html'


    def get(self, request):
        context = {
            'form': UserCreationForm(), 'form1': UserRoleForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        form1 = UserRoleForm(request.POST)

        if form.is_valid():
            form.save()
            form1.save()
            role = form1.cleaned_data.get('role')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password, role=role)
            login(request, user)
            print(role)
            if role == 'seller':
                return redirect('home_other')
            if role == 'customer':
                return redirect('user_main')
        context = {
            'form': form,
            'form1': form1
        }
        return render(request, self.template_name, context)
