def time_to_min(tm):
    [h, m] = tm.split(':')
    return int(h) * 60 + int(m)


def to_flat(mel):
    return mel.replace('C#', '1').replace('D#', '2').replace('F#', '3').replace('G#', '4').replace('A#', '5')


def solution(m, musicinfos):
    cand_answer = []
    music_dict = {}
    flatten = to_flat(m)
        
    for idx, info in enumerate(musicinfos):
        [st, end, title, melody] = info.split(',')
        play_time = time_to_min(end) - time_to_min(st)
        flatten_melody = to_flat(melody)
        
        if len(flatten_melody) <= play_time:
            full_melody = flatten_melody * play_time
        else:
            full_melody = flatten_melody[:play_time + 1]
        
        if flatten in full_melody:
            cand_answer.append(title)
        music_dict[title] = [play_time, idx]
    
    cand_answer.sort(key = lambda x : music_dict[x][1])
    cand_answer.sort(key = lambda x : music_dict[x][0], reverse=True)

    return cand_answer[0] if cand_answer else "(None)"