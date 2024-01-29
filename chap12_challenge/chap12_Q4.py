# 六角形を表すHexagonクラスを定義する。そのクラスには外周の長さを計算して返すメソッドcalculate_perimeterを定義する
# そして、Hexagonオブジェクトを作って、calculate_perimeterメソッドを呼び出し、結果を出力する。
# 六角形の外周を求める式を、 １辺＊６　とする。　辺＝side
class Hexagon:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 6
    
hexagon = Hexagon(10)
print(hexagon.calculate_perimeter())