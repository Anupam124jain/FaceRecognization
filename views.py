
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.hashers import make_password, check_password
from forms import  *
from django.http import HttpResponse

@csrf_protect
def register(request):
    global variables
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            password=make_password(request.POST['password1'])
            userobj = User(firstname=request.POST['firstname'],lastname=request.POST['lastname'],password=password,
                            email=request.POST['email'],mobileno=request.POST['mobileno'],gender =request.POST['gender'])
            userobj.save()

            return HttpResponseRedirect('/register/success/')
        else:
            variables = RequestContext(request, {'form': form})
            render_to_response('registration/register.html', variables)
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html',variables)

def register_success(request):
    return render_to_response(
        'registration/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render_to_response(
        'home.html',
        {'user': request.user}
    )



