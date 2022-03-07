from django.shortcuts import redirect, render

# Create your views here.

def home_page(request):
    if request.method == "POST":
        print(request.POST)
        return redirect("blogpage")
    return render(request,"home.html")

def blog_page(request):

    return render(request,"blog.html")
