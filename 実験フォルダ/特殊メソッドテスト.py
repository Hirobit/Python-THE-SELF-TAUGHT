class Sample:
    def __init__(self, val):
        self.val = val

    def __mod__(self, other):
        return self.val % other.val


o1 = Sample(20)
o2 = Sample(5)
print(o1 % o2)

## 出力
3