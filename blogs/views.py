from django.shortcuts import render,redirect
from blogs.models import Blog

# Create your views here.
def index(request):
    bl = Blog.objects.all()
    return render(request,"index.html",{"bl":bl})

def add(request):
    return render(request,"add.html")

def delete(request,id):
    bl = Blog.objects.filter(id=id)
    bl.delete()
    return redirect("/")

def insert(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        writer = request.POST["writer"]
        data = Blog.objects.create(title=title,content=content,writer=writer)
        data.save()
        return redirect("/")
    return redirect("/")