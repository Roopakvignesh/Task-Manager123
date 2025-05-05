from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Task
# Create your views here.
@login_required(login_url='signin')
def home(request):
    context={}
    if request.method=='POST':
        title=request.POST.get('title','')
        desc=request.POST.get('desc','')
        if title and desc:
            Task.objects.create(
                title=title,
                desc=desc,
                owner=request.user
            )
            return redirect('home')
        else:
            context['message']='Both are required!!!'
    tasks=request.user.tasks.all()
    # tasks=Task.objects.filter(owner=request.user)
    context['tasks']=tasks
    # context['operation']='Add Task'
    return render(request,'task_files/tasks.html',context)
@login_required(login_url='signin')
def update_task_view(request,pk):
    context={}
    try:
        task=request.user.tasks.get(id=pk)
        context['task']=task
    except:
        context['message']='404!! Not found'
    if request.method=='POST':
        title=request.POST.get('title','')#fetched from clint side
        desc=request.POST.get('desc','')
        task.title=title#adding it to the same object model
        task.desc=desc
        task.save()
    
        return redirect('home')
    # context['operation']='Edit Task'
    return render(request,'task_files/update_task.html',context)
@login_required(login_url='signin')
def delete_task_view(request,pk):
    context={}
    try:
        task=Task.objects.get(id=pk,owner=request.user)
        context['task']=task
    except:
        context['message']='404!! Not found'
    if request.method=='POST':
        task.delete()
        return redirect('home')
    return render(request,'task_files/task_delete.html',context)