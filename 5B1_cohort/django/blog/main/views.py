from django.shortcuts import redirect, render


# Create your views here.

def home_page(request):
    if request.method == "POST":
        print(request.POST)
        return redirect("aboutpage")
    return render(request,"home.html")

def about_page(request):

    return render(request,"about.html")