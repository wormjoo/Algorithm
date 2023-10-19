from collections import defaultdict

def solution(genres, plays):
    answer = []
    play_of_genre = defaultdict(int)
    information = []
    
    for i in range(len(genres)):
        play_of_genre[genres[i]] += plays[i]
        information.append([i, genres[i], plays[i]])
    
    information.sort(key=lambda x:(-x[2], x[0]))
    play_of_genre = sorted(play_of_genre.items(), key=lambda x:-x[1])
    
    for genre, play in play_of_genre:
        count = 0
        for i in range(len(information)):
            if genre == information[i][1]:
                answer.append(information[i][0])
                count += 1
            if count >= 2:
                break
    
    return answer
