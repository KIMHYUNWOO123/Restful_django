from django.http import JsonResponse
from requests import request
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import User
from django.views.decorators.csrf import csrf_exempt


class PostViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PostSerializer
    
   
   
@csrf_exempt
def test(request):

    if request.method == 'POST':
        id = request.POST.get('userid','')
        pw = request.POST.get('userpassword','')
        name = request.POST.get('username', '')
        birth = request.POST.get('userbirth' '')

    print(id, pw, name, birth)

    return JsonResponse({'code': "ㅎㅇ", 'msg':'ㅋ'})