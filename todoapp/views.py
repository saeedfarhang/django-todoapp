from django.shortcuts import render, redirect
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from .forms import TodoItemForm

def home_view(request):
    return render(request, 'todoapp/home.html')


@login_required(login_url='/accounts/login')
def todo_list_view(request):
    user = request.user
    query = TodoItem.objects.filter(owner = user)

    if request.method == 'POST':
        checked_list = request.POST.getlist('checked')
        checked_list = [int(i) for i in checked_list]
        for todo_item in query:
            if todo_item.id in checked_list:
                TodoItem.objects.filter(id = todo_item.id).update(checked=True)
            else:
                TodoItem.objects.filter(id = todo_item.id).update(checked=False)
        return redirect('/list')

    todo_list_len = len(query)
    return render(request, 'todoapp/todo_list.html', {'todolist':query,'todo_list_len':todo_list_len})

@login_required(login_url='/accounts/login')
def todo_item_create(request):
    user = request.user
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit= False)
            instance.owner = user
            instance.save()
            return redirect('todoapp:todo_list')
    form = TodoItemForm()
    return render(request, 'todoapp/create_todo_item.html', {'form':form})
    
def delete_todo_item(request, id):
    try:
        item = TodoItem.objects.get(id = id)
    except:
        return redirect('todoapp:todo_list')
    if item.owner == request.user:
        item.delete()
        return redirect('todoapp:todo_list')
    else:
        return redirect('todoapp:todo_list')