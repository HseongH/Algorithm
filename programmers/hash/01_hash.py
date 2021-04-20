def solution(participant, completion):
    part = {}
    
    for i in participant:
        try:
            part[i] += 1
        except KeyError:
            part[i] = 1
        
    for i in completion:
        part[i] -= 1
        
    for key, value in part.items():
        if value > 0:
            return key
