from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Team
# Create your views here.

@api_view(['GET'])
def all_teams(request):
    all_teams=Team.objects.all()
    output=[

    ]
    for temp_team in all_teams:
        temp_dict={
            'team_id':temp_team.id,
            'team_country':temp_team.country,
            'team_name':temp_team.name,
            'temp_discription':temp_team.discription,
            'temp_logo':temp_team.logo
        }
        output.append(temp_dict)
    return Response(output)

@api_view(['GET'])
def team(request):
    team_id=request.GET.get('team_id',None)
    if team_id is None:
        return Response({'message':'invalid team id'})
    else:
        try:
            team_info=Team.objects.get(id=team_id)
            team_dict={
                'team_id':team_info.id,
                'team_name':team_info.name,
                'team_country':team_info.country,
                'team_discription':team_info.discription,
                'team_logo':team_info.logo
            }
            return Response(team_dict)
        except Team.DoesNotExist:
            return Response({'message':'invalid team_id'})
