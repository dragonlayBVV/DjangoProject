from django.shortcuts import render
from django.views.generic import TemplateView
#from django.http import HTTPResponse
# Create your views here.
def index(request):
    name = request.GET.get('name','Guest')
    title = 'First site!'
    name = 'Vital123'
    text = 'Hello'
    list = [1.45673, 2.45768, 4.5780]
    len_list = len(list)
    context = {
        'title': title,
        'text': text,
        'list': list,
        'len_list': len_list,
        'name': name,
    }
    return HTTPResponse(f"Hello, {name}")
    return render(request, 'index.html', context)

def base(request):
    return render(request, 'index2.html')

class index2(TemplateView):
    template_name = 'index2.html'
