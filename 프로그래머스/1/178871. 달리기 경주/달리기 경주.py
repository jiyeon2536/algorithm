def solution(players, callings):
    player_rank = {p: i for i, p in enumerate(players)}
    rank_player = {i: p for i, p in enumerate(players)}
    
    for call in callings:
        player_rank[call] -= 1  
        pre = rank_player[player_rank[call]]  
        player_rank[pre] += 1 
        rank_player[player_rank[call]] = call
        rank_player[player_rank[call] + 1] = pre

    return list(rank_player.values())
