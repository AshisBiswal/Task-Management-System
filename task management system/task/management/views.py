from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
import requests
from .forms import loginform,registerform,taskform,commentform
from .models import taskmodel,Comment
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.db.models import Q




def register(request):
    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm_password']
            email = form.cleaned_data['email']
            user  = User.objects.filter(username = username)
            if(user.exists()):
                messages.info(request, "Username already taken!")
                return redirect('register')
            if(password == confirm):
                user = User.objects.create(username = username,email = email)
                user.set_password(password)
                user.save()
                subject = 'welcome to Task Manager'
                message = f'Hi {user.username}, thank you for registering in Task Manager.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )
               
                return redirect('login')
            else:
                messages.info(request, "password not matching")
                return redirect('register')

    form = registerform()
    return render(request,'register.html',{'form' : form})
def task(request):
    work = taskmodel.objects.all()

    if request.method == "POST":
        query = request.POST.get('answers123')  
        filtering = request.POST.get('filter12')  

        if query:
            work = work.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(assigned_to__username__icontains=query)
            )
            
        if filtering != None:
            work = work.filter(
                Q(priority__icontains=filtering) |
                Q(status__icontains=filtering) 
            )

    context = {'tasks': work}
    return render(request, 'task.html', context)
def user_login(request):
    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password= form.cleaned_data['password']

            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request,user)


                return redirect('task_page')
            else:
               
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password.'})

    else:
        context = {}
        context['form'] = loginform()
        return render(request,'login.html',context)

def addtask(request):
    if request.method == "POST":
        form = taskform(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            priority = form.cleaned_data['priority']
            status = form.cleaned_data['status']
            due_date = form.cleaned_data['due_date']
            assigned_to = form.cleaned_data['assigned_to']
            assigned_by = request.user
            
            try:
                user = User.objects.get(username=assigned_to)
            except User.DoesNotExist:
                user = None
            
            task = taskmodel.objects.create(title=title, description=description, priority=priority, status=status, due_date=due_date, assigned_to=user,assigned_by=request.user)
            if request.user.is_authenticated:
                assigned_by = request.user.username
            subject = 'welcome to Task Manager'
            login_url = reverse('login')  
            message = f"Hi, you have been assigned a task by {assigned_by}. Please login to {login_url}."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
               
            return redirect('task_page') 
        else:
           
            return render(request, 'addtask.html', {'form': form, 'error_message': 'Invalid inputs'})
    
  
    form = taskform()
    return render(request, 'addtask.html', {'form': form})



def update_task(request, task_id):
    task = get_object_or_404(taskmodel, pk=task_id)
    
    if request.method == "POST":
        if(request.user == task.assigned_by):
            form = taskform(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_page')
        else:
            messages.info(request,'you cant update this task')
            return redirect('task_page')  
    else:
        form = taskform(instance=task)
    
    return render(request, 'update.html', {'form': form})


def comments(request,task_id):
    task = taskmodel.objects.get(pk = task_id)
    if request.method == "POST":
        form = commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user  
            comment.save()
            return render(request, 'comment.html', {'task': task, 'comment': comment})
       
    form = commentform()
    return render(request, 'comment.html', {'task': task, 'form': form})


def deletecomment(request,comment_id):
    comment = get_object_or_404(Comment,pk = comment_id)
    task_id=comment.task.id
    if request.user == comment.user:
        comment.delete()

    return redirect("comment", task_id)

def deletetask(request,task_id):
    task = get_object_or_404(taskmodel, pk=task_id)
    
    print("Requesting user:", request.user)
    print("Task assigned to:", task.assigned_to)
    
    if request.user == task.assigned_to or request.user == task.assigned_by:
        task.delete()
        messages.success(request, "Task deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this task.")
    
    return redirect("task_page")


def home(request):
    return render(request,'home.html')