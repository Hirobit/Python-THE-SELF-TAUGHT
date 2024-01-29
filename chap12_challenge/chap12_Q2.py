# 円を表すCircleクラスを定義する。面積を計算して返すメソッドareaを持たせる、面積の計算にはPythonの組み込みモジュールmathのpi定数を使う。
# 次にCircleオブジェクトを作ってareaメソッドを呼び出し、結果を出力する。
# 半径＝radius、　円周率＝pi、　直径＝a diameter

import math
pi = math.pi

class Circle:
    def __init__ (self, r, p):
        self.radius = r
        self.pi = p

    def area(self):
        return self.radius * self.radius * self.pi
    
circle = Circle(4,pi)
print(circle.area())

"""
わざわざmath.piを、piという変数に入れないで、良い。シンプルに radius**2*meth.pi で同じ処理ができる。
オブジェクト指向で行うので、あまりグローバル変数を作らずクラスの中に入れったほうがいいかも、、、
"""