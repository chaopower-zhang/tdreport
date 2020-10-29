from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.generic.base import View
from .form import RegForm
from users.models import UserProfile


class RegisterView(View):
    '''用户注册'''

    def get(self, request):

        form_obj = RegForm()
        return render(request, 'register.html', {'form_obj': form_obj})

    def post(self, request):
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            form_obj.cleaned_data.pop('re_password')
            UserProfile.objects.create_user(**form_obj.cleaned_data)
            return HttpResponse('注册成功！')
        else:
            print(form_obj.errors)
            return HttpResponse('注册失败！')
