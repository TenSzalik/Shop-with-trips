from django.shortcuts import render
from planet.models import Planet, Trip

# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def menu_view(request):
    queryset = Planet.objects.all()

    return render(request, "block_content/menu_list.html", {"queryset": queryset})


def trip_view(request):
    queryset = Trip.objects.all()

    return render(request, "block_content/trips.html", {"queryset": queryset})


def register_view(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}

    return render(request, "block_content/register.html", context)


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect("/")
            return response
        else:
            response = redirect("/")
            return response

    else:
        return render(request, "block_content/login.html", {})


def logout_view(request):
    logout(request)

    return redirect("/login")


def planet_data_view(request, pk):
    planet = Planet.objects.get(id=pk)
    context = {"planet": planet}
    return render(request, "block_content/planet_data.html", context)


def trip_offer_view(request, pk):
    trip = Trip.objects.get(id=pk)
    context = {"trip": trip}
    return render(request, "block_content/trip_offer.html", context)
