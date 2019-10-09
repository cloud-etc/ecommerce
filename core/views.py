from django.shortcuts import render
from .forms import ContactForm

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'core/contact.html', context)

