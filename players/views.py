from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Player,PlayerMatchPoints
# Create your views here.

@api_view(['GET'])
def all_players(request):
    all_players=Player.objects.all()
    output=[

    ]
    for temp_players in all_players:
        temp_dict={
            'player_id':temp_players.id,
            'player_name': temp_players.name,
            'player_number': temp_players.number,
            'player_image': temp_players.image,
            'player_runs': temp_players.runs,
            'player_matches': temp_players.matches,
            'player_wickets':temp_players.wickets,
            'player_age':temp_players.age,
            'player_batting_style': temp_players.batting_style,
            'player_bowling_style': temp_players.bowling_style,
            'player_player_type': temp_players.player_type,
            'player_is_captain': temp_players.is_captain,
        }
        output.append(temp_dict)
    return Response(output)

@api_view(['GET'])
def player(request):
    player_id=request.GET.get('player_id',None)
    if player_id is None:
        return Response({'message':'invalid player id'})
    else:
        try:
            player_info-Player.objects.get(id=player_id)
            player_dict={
                'player_id':player_info.id,
                'player_name':player_info.name,
                'player_number': player_info.number,
                'player_image': player_info.image,
                'player_runs': player_info.runs,
                'player_matches': player_info.matches,
                'player_wickets': player_info.wickets,
                'player_age': player_info.age,
                'player_batting_style': player_info.batting_style,
                'player_bowling_style': player_info.bowling_style,
                'player_player_type': player_info.player_type,
                'player_is_captain': player_info.is_captain,
            }
            return Response(player_dict)
        except Player.DoesNotExist:
            return Response({'message':'invalid player_id'})

