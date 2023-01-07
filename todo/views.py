from django.shortcuts import render, redirect
from .models import Items
from .forms import ItemsForm
# Create your views here.


def get_todo_list(request):
    items = Items.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo/todo_list.html", context)


def add_item(request):
    if request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_todo_list")

    form = ItemsForm
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
