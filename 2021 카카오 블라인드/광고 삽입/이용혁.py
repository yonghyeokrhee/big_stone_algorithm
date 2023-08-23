def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s


def delta(play_time):
    play_list = play_time.split(":")
    return int(play_list[0]) * 3600 + int(play_list[1]) * 60 + int(play_list[2])


def logs_to_second(log):
    log = log.split("-")
    s = delta(log[0])
    e = delta(log[1])
    return s, e


def solution(playsec, adsec, logs):
    playsec = delta(playsec)
    adsec = delta(adsec)

    play = [0] * (playsec + 1)

    for log in logs:
        s, e = logs_to_second(log)

        play[s] += 1
        play[e] -= 1

    # 누적 합 : 누적 동영상 cnt
    for i in range(1, playsec + 1):
        play[i] += play[i - 1]
    # 누적 합 : 누적 playtime sum
    for i in range(1, playsec + 1):
        play[i] += play[i - 1]
    # 누적 합 : window 계산
    mx_time = 0
    mx_view = 0
    for i in range(adsec - 1, playsec):
        if i >= adsec:
            if mx_view < play[i] - play[i - adsec]:
                mx_view = play[i] - play[i - adsec]
                mx_time = i - adsec + 1
        else:
            if mx_view < play[i]:
                mx_view = play[i]
                mx_time = i - adsec + 1
         # if
        # if (i == adsec - 1) and (mx_view < play[i]):
        #     mx_time = i - adsec + 1
        # elif mx_view < (play[i] - play[i - adsec]):
        #     mx_time = i - adsec + 1

    return int_to_str(mx_time)


a = solution("02:03:55", "00:14:15",\
         ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])

print(a)