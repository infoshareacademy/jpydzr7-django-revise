from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.template import loader
from django.contrib.auth import login
from password_manager.models import PasswordData


# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def register_form(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    register_template = loader.get_template("register.html")
    context = {"form": form}
    return HttpResponse(register_template.render(context, request))


@login_required
def add_password_form(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        entry = PasswordData(user=request.user,
                             service_name=service_name,
                             username=username,
                             email=email,
                             password=password)
        entry.save()

        return redirect('passwords_list')

    add_password_form_template = loader.get_template("add_password_form.html")
    context = {}
    return HttpResponse(add_password_form_template.render(context, request))


@login_required
def passwords_list(request):
    entries = PasswordData.objects.filter(user=request.user)
    passwords_list_template = loader.get_template("passwords_list.html")
    context = {'entries': entries}
    return HttpResponse(passwords_list_template.render(context, request))


@login_required
def password_details(request, entry_id):
    entry = get_object_or_404(PasswordData, id=entry_id, user=request.user)
    password_details_template = loader.get_template("password_details.html")
    context = {'entry': entry}
    return HttpResponse(password_details_template.render(context, request))
