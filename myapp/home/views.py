from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from myapp.user.models import Event
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@csrf_exempt
def save(request):

    # 삭제
    Event.objects.all().delete()

    # 저장
    data = json.loads(request.body)
    events = data['events']

    for event in events :

        Event.objects.create(
            title = event['title']
            , discription = event['discription']
            , start = event['start']
            , end = event['end']
        )
    
    return HttpResponse(json.dumps({'msg': 'OK'}), content_type="application/json")

@csrf_exempt
def getList(request) :
    data = list(Event.objects.values())
    return JsonResponse(data, safe=False)


