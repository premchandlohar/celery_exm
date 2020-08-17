from django.http import JsonResponse
import json
from .models import Userprofile
from django.contrib.auth import get_user_model
from django.db import transaction

# Create your views here.

def create_user(request):
    try:
        params = json.loads(request.body)

        username = params.get('username')
        password = params.get('password')
        first_name = params.get('first_name')
        last_name = params.get('last_name')
        age = params.get('age')
        mobile_number = params.get('mobile_number')
        email = params.get('email')

        with transaction.atomic():
            user_obj =get_user_model().objects.create(
                username = username,
                # is_staff = True
            )
            user_obj.set_password(password)
            user_obj.save()

            user_profile_obj = Userprofile.objects.create(
                user = user_obj,
                first_name = first_name,
                last_name = last_name,
                age = age,
                mobile_number = mobile_number,
                email = email
            )

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})