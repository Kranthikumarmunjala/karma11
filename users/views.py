from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import CustomUser
# Create your views here.


@api_view(['GET'])
def all_users(request):
    all_users=CustomUser.objects.all()
    output=[

    ]
    for temp_user in all_users:
        temp_dict={
            'user_id':temp_user.id,
            'user_user':temp_user.user,
            'user_email':temp_user.email,
            'user_mobile_number':temp_user.mobile_number,
            'user_age':temp_user.age,
            'user_dob':temp_user.dob
        }
        output.append(temp_dict)
    return Response(output)

@api_view(['GET'])
def user(request):
    user_id=request.GET.get('user_id',None)
    if user_id is None:
        return Response({'message':'invalid user id'})
    else:
        try:
            user_info=CustomUser.objects.get(id=user_id)
            user_dict={
                'user_id':user_info.id,
                'user_user':user_info.user,
                'user_email':user_info.email,
                'user_mobile_number':user_info.mobile_number,
                'user_age':user_info.age,
                'user_dob':user_info.dob
            }
            return Response(user_dict)
        except CustomUser.DoesNotExist:
            return Response({'message':'invalid user_id'})