from django.http import HttpResponse

from django.shortcuts import render, redirect

from .forms import Movieform
from p1app.models import movies


# Create your views here.


def demo(request):
    movie=movies.objects.all()
    return render(request,'index.html',{'movie_list':movie})

def detail(request,movie_id):
    movie=movies.objects.get(id=movie_id)
    # return HttpResponse("this is movie no %s" % movie_id)
    return render(request,'detail.html',{"movie":movie})


def data(request):
    if request.method=="POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img  =  request.FILES['img']

        Movie=movies(name=name,desc=desc,year=year,img=img)
        Movie.save()
        return redirect('/')
    return render(request,'add.html')


def update(request,id):
    movie=movies.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):

    if request.method=='POST':
        mov=movies.objects.get(id=id)
        mov.delete()
        return redirect('/')

    return render(request,'delete.html')






