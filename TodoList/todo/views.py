from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Work


def todo_create(request):
    form = TodoForm()
    if request.method=="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()#for clearing form
            return redirect('/')
    context = {
        'form':form
    }
    return render(request,"todo/todocreate.html",context)

def home(request):
    context={
        'objects':Work.objects.all()
    }
    return render(request,'todo/home.html',context)

def update_todo(request,pk):
    todo = Work.objects.get(id=pk)
    up_todo = TodoForm(instance=todo)
    if request.method == "POST":
        up_todo = TodoForm(request.POST, instance = todo)
        if up_todo.is_valid():
            up_todo.save()
            return redirect('/');
    context={
        'up_todo':up_todo
    }
    return render(request,'todo/update_todo.html',context)

def detail_todo(request,pk):
    detail= Work.objects.get(id=pk)
    context={
        'de_form':detail
    }
    return render(request,'todo/detail_todo.html',context)
def delete_todo(request,pk):
    dele_todo=Work.objects.get(id=pk)
    if request.method=='POST':
        dele_todo.delete()
        return redirect('/')
    context = {
        'dele_todo': dele_todo
    }
    return render(request, 'todo/delete_todo.html', context)
