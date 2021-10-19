# reverse() vs reversed()
lst = [1, 2, 3, 4, 5]
print(lst)
lst.reverse()  # reverse() : Reverse the order of "lst"
print(lst)

lst2 = [1, 2, 3, 4, 5]
print("lst2 뒤집기 전 : ", lst2)

# reversed() : Return a return var which is reversed ; lst2 is not changed unlike "lst"
lst3 = reversed(lst2)
print("리트스 2 뒤집은 후 : ", lst2)
print("리스트3 : ", list(lst3))


# << zip library >>
kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

# zip : Combine lists down >> [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(kor, eng)))

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
# * : Unzip[Seperate] >> [('사과', '바나나', '오렌지'), ('apple', 'banana', 'orange')]
print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2) # >> ('사과', '바나나', '오렌지')
print(eng2) # >> ('apple', 'banana', 'orange')
