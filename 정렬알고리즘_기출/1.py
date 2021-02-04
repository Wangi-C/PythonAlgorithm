#국영수
n = int(input())
grade = []
for i in range(n):
    grade.append(input().split())

#[정렬 기준]
#두번째원소를 기준으로 내림차순 정렬
#두번째원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
#세번째원소가 같은 경우, 네 번째 원소를 기준으로 내림차순
#네번째원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순

grade.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for student in grade:
    print(student[0])