from django.shortcuts import render
from django.views.generic import View
# from .utils import main
from django.http import JsonResponse

from .models import UserAccount
import json

class TrackerView(View):
    def get(self, req):
        return render(req, 'tracker/trackers.html')

    def post(self,request):
        data = json.loads(request.body)
        is_exist = UserAccount.objects.filter(name=data['name'],phone=data['phone'])
        if not is_exist:
            UserAccount.objects.create(name=data['name'],phone=data['phone'],start_date=data['start'],end_date=data['end'])
            return JsonResponse({'success':'You have successfully signedUp'})
        
        return JsonResponse(data={'error':'User already exist'},status=403)