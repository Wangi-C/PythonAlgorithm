#성적이 낮은 순서로 학생 출력
n = int(input())
student = []
for i in range(n):
    data = input().split()
    student.append((data[0],int(data[1])))

#키를 이용하여, 점수를 기준으로 정렬
student = sorted(student, key=lambda s : s[1])
#정렬이 수행된 결과를 출력
for s in student:
    print(s[0],end=" ")