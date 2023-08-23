from collections import defaultdict
from queue import PriorityQueue


def delta(play_time):
    play_list = play_time.split(":")
    return int(play_list[0]) * 3600 + int(play_list[1]) * 60 + int(play_list[0])


def logs_to_second(log):
    log = log.split("-")
    s = delta(log[0])
    e = delta(log[1])
    return s, e


def solution(play_time, adv_time, logs):
    mx = 0
    playsec = delta(play_time)
    adsec = delta(adv_time)

    play = [0] * playsec

    for log in logs:
        s, e = logs_to_second(log)
        for i in range(s, e):
            play[i] += 1
    print(sum(play))
    earlist = defaultdict(PriorityQueue)
    for i in range(playsec, playsec - adsec):
        ad_exp = sum(play[i:i + adsec])
        if mx <= ad_exp:
            mx = ad_exp
            earlist[mx].append(i)
    return earlist[mx].get()