from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import (
    RegistrationForm
)




def Registration(request):
    template_name = 'registration/register.html'

    if request.method == 'POST':

        post_request = request.POST
        username = post_request.get('username')
        email = post_request.get('email')
        passsword = post_request.get('password1')
        passsword2 = post_request.get('password2')

        form_errors = []

        context = {'form_errors': form_errors, 'form': RegistrationForm()}

        if (username or email or passsword or passsword2) is None:
            form_errors.append('Incomplete form submitted')
            return render(request, template_name, context)

        if passsword != passsword2:
            form_errors.append('Passwords do not match')
            return render(request, template_name, context)

        # Create User and automatically login user
        try:
            user = User.objects.create_user(username, email, passsword)
            user.save()
        
        except IntegrityError:
            form_errors.append('User with this username already exists')
            return render(request, template_name, context)

        return redirect('authentication:login')

    context = {'form': RegistrationForm()}
    return render(request, template_name, context)
