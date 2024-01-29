class AlwaysPositive:
    def __init__(self, number):
        self.number = number

    #def __add__(self, other):
        #return abs(self.number + other.number)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)


"""
一回クラスに数字を入れて、それを変数に代入して（インスタンス化）、その変数を足し算しようとしても、
クラスに四則演算の特殊メソッドを書かないとエラーになる。
"""