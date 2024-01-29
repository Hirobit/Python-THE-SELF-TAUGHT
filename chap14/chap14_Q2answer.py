"""
自分のコードは完全に間違っている。Squareクラスのオブジェクトをprint関数に渡したら4辺それぞれの長さを出力ができていない
print文の中で表示方法を指定しているからオブジェクト指向的ではないと思われる。

答えのコードでは__repr__メソッドが使われてる
__repr__メソッドとは、特殊メソッドに分類され、インスタンス化したクラスのオブジェクトをprint関数に渡すと
自動で__repr__が内部で呼び出される。このメソッドの元の働きは、print関数に渡されたオブジェクトのクラス名とメモリアドレスを返す働きがある。
このメソッドをコード内で明示的に上書き(オーバーライド)して、出力したい返したい内容を変更している
このコードではここ def __repr__(self):
                       return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)
オーバーライドすることによって、コード最後のprint文にインスタンス化したオブジェクトを入れるだけで、__repr__が呼び出され
明示的に変更を加えた内容の__repr__メソッドか処理され返される。

つまり、このコードは、__repr__ メソッドを使ってオブジェクトの文字列表現をカスタマイズする良い例です。
"""

class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(29)
print(a_square)