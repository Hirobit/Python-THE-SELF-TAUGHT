"""
自分が書いたコードの式は正六角形の外周を求めるやり方で、アンサーの方は１辺ずつ明示的に計算するコードになる。
学習範囲の、クラスを作ってその中にメソッドを埋め込み、外でオブジェクトを作り(クラスのインスタンス化)そのメソッドを動かして値を出力するということは完璧にできている！！ドンピシャです。
"""

class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

a_hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(a_hexagon.calculate_perimeter())