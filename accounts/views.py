from django.contrib.auth import authenticate, login
from django.contrib.auth import login
#from authentication import authenticate
from django.http import HttpResponse

def persona_login(request):
    user = authenticate(assertion=request.POST['assertion'])
    if user:
        login(request,user)
    return HttpResponse('OK')
