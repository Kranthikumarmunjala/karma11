from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Leaderboard
# Create your views here.

@api_view(['GET'])
def leaderboards(request):
    all_leaderboards= Leaderboard.objects.all()
    output=[

    ]
    for temp_leaderboards in all_leaderboards:
        temp_dict={
            'leaderboard_id':temp_leaderboards.id,
            'leaderboard_player':temp_leaderboards.player,
            'leaderboard_points':temp_leaderboards.points,
            'leaderboard_rank':temp_leaderboards.rank,
        }
        output.append(temp_dict)
    return Response(output)

@api_view(['GET'])
def leaderboard(request):
    leaderboard_id=request.GET.get('leaderboard_id',None)
    if leaderboard_id is None:
        return Response({'message':'invalid leaderboard id'})
    else:
        try:
            leaderboard_info=Leaderboard.objects.get(id=leaderboard_id)
            leaderboard_dict={
                'leaderboard_id':leaderboard_info.id,
                'leaderboard_player':leaderboard_info.player,
                'leaderboard_points':leaderboard_info.points,
                'leaderboard_rank':leaderboard_info.rank
            }
            return Response(leaderboard_dict)
        except Leaderboard.DoesNotExist:
            return Response({'message':'invalid leaderboard_id'})
