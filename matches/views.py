from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Match,MatchResult
# Create your views here.

@api_view(['request'])
def matches(request):
    all_matches=Match.objects.all()
    output=[

    ]
    for temp_matche in all_matches:
        temp_dict={
            'match_id':temp_dict.id,
            'match_country_one':temp_dict.country_one,
            'match_country_two':temp_dict.country_two,
            'match_datetime':temp_dict.datetime,
            'match_venue':temp_dict.venue
        }
        output.append(temp_dict)
    return Response(output)

@api_view(['GET'])
def match(request):
    match_id=request.GET.get('match_id',None)
    if match_id is None:
        return Response({'message':'invalid match id'})
    else:
        try:
            match_info=Match.objects.get(id=match_id)
            match_dict={
                'match_id':match_dict.id,
                'match_country_one': match_dict.country_one,
                'match_country_two': match_dict.country_two,
                'match_datetime': match_dict.datetime,
                'match_venue': match_dict.venue,
            }
            return Response(match_dict)
        except Match.DoesNotExist:
            return Response({'message':'invalid match_id'})