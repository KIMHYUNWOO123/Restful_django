from django.http import JsonResponse
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

    print(id, pw)

    return JsonResponse({'code': 1004, 'msg':'good'})