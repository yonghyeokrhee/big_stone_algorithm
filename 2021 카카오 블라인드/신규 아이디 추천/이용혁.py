def solution(new_id):
    new_id = new_id.lower()  # 1단계
    answer = ''  # 2단계
    for s in new_id:
        if s.isalnum():
            answer += s
        elif s in ['-', '_', '.']:
            answer += s
    new_id = answer
    answer = ''  # 불변 객체라서 가능하다.
    for i in range(len(new_id)):
        if i == 0:
            answer += new_id[i]

        elif new_id[i] == '.' and answer[-1] == new_id[i]:
            continue
        else:
            answer += new_id[i]

    answer = answer.strip('.')
    # 5단계
    if len(answer) == 0:
        answer = "a"
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15].strip('.')

    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))

    return answer