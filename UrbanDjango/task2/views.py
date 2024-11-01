from django.shortcuts import render

def class_template(request):
    return render(request, 'class_template.html')

def func_template(request):
    return render(request, 'func_template.html')

