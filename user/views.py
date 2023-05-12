from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_text(request):
    # return HttpResponse('Hello World \n congratulations from the team "Upply_JumIT \n Direct by Natali Usevich')
    return render(request, 'main_page.html', )
