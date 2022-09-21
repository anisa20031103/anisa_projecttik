from django.shortcuts import render

# Create your views here.
def feb(rrequest):
    return render(request, 'feb.html')
