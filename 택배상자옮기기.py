
n,w,num = map(int,input().split())

def solution(n, w, num):
    # 몇 개를 꺼내야하는지
    answer = 0
    # 행
    row = (n+w-1) // w
    a = [[0] * w for _ in range(row)]
    number = 1
    
    # 리스트에 택배 상자 쌓기
    for i in range(row): # 1~4
        # 홀수 행일 때 왼쪽에서 오른쪽으로 쌓이는 반복문
        if i % 2 == 0:
            for j in range(w):
                a[i][j] = number
                number += 1 # 6까지 쌓임
                if number > n: break
        else:
            for j in range(w-1,-1,-1):
                a[i][j] = number
                number += 1
                if number > n: break
        if number > n : break # 외부 반복문 나가기
    
    # 찾는 택배상자 열 번호 찾기
    for row in a:
        if num in row:  # num이 리스트에 있는지 확인
            col = row.index(num)  # 존재하면 인덱스 찾기
            break  # 찾았으면 종료
    
    # 해당 열번호에 있는 택배상자들 꺼내기
    for row in a:
        for i in row:
            if (i > num and row.index(i) == col):
                answer += 1
            number += 1
            
            
    return answer


print(solution(n,w,num))