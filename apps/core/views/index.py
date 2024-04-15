from django.shortcuts import render


def index(request):
    context = {'a': 'aaa'}
    return render(request=request, template_name='index.html', context=context)
