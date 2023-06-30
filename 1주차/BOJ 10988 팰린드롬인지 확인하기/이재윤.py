// 파이썬에서 문자열은 [::-1]을 통해서 뒤집을 수 있다
// 혹은 문자열을 리스트로 변환한후에, reverse()를 통해 뒤집어주고, 그 다음에 ''.join() 하는 방법도 가능하다 

str = input()

if str == str[::-1]:
    print(1)
else:
    print(0)
    
