from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Country
# Create your views here.


@api_view(['GET'])
def all_countries(request):
    all_countries=Country.objects.all()
    output=[

    ]
    for temp_countries in all_countries:
        temp_dict={
            'country_id':temp_countries.id,
            'country_name':temp_countries.name,
            'country_short_code':temp_countries.short_code,
            'country_color':temp_countries.color,
            'country_flag':temp_countries.flag
        }
        output.append(temp_dict)
    return Response(output)

@api_view(['GET'])
def country(request):
    country_id=request.GET.get('country_id',None)
    if country_id is None:
        return Response({'message':'invalid country id'})
    else:
        try:
            country_info=Country.objects.get(id=country_id)
            country_dict={
                'country_id':country_info.id,
                'country_name':country_info.name,
                'country_color':country_info.color,
                'country_flag':country_info.flag
            }
            return Response(country_dict)
        except Country.DoesNotExist:
            return Response({'message':'invalid country_id'})
