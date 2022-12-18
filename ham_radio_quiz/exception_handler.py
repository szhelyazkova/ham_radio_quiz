from django.shortcuts import render


def custom_handler404(request, exception):
    return render(request, '404.html')


def custom_handler500(request, *args, **kwargs):
    return render(request, '500.html')
