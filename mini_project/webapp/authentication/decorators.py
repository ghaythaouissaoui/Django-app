from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='directeur').exists():
                return redirect('base_user')
            elif request.user.groups.filter(name='admin').exists():
                return redirect('base') #routing error was do to this redirect call. the  value was base_admin instead of base
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_function(request,*args, **kwargs):
            group= None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('You are not authorized')
        return wrapper_function
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group= None 
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group=='directeur':
            redirect('user-page')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function