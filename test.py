a = {1: 3, 2: 2, 3: 3, 4: 4, 5: 5}
print(list(a.keys()))
print(list(a.values()))
# 순서 보존됨

print([1] * 2)


# 옳은 문법

class A:
    is_a = True


a_as = [A() for x in range(5)]

_ = []
for a in a_as:
    _.append(a.is_a)
print(_)

a_as[3].is_a = False

_ = []
for a in a_as:
    _.append(a.is_a)
print(_)
# 객체

c = 1
a = c
b = c
c = 2
print(a, b)
# 참조

a = [0, 1, 2]
print(a[:1])
print(a[1:])
# 슬라이싱

a = None
if a:
    print('None is True')
else:
    print('None is False')
# None 은 False

a = [x for x in range(5)]
print(a)
# 올은 문법

a = [(1, 1), (2, 2)]
print(dict(a))
