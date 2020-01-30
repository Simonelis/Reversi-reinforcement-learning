import json
from django.http import JsonResponse

import engine.api


def play(request):

    player_color = 1

    data = {
        'board': engine.api.INIT_BOARD,
    }

    if request.POST.get('action') == 'post':
        data = json.loads(request.body)
        if engine.api.is_valid_move(data.move, data.board, player_color):
            engine.api.get_next_board(data.board, player_color)
            return JsonResponse({'method': 'POSTED!'})
    
    return JsonResponse(data)