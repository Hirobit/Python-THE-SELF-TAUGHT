# 三角形を表すTriangleをクラスとして定義し、面積を返すareaメソッドを持たせる。そうして、Triangleオブジェクトを作って、areaメソッドを呼び出して結果を出力する。
# 底辺＝base, 高さ＝height
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height / 2
    
triangle = Triangle(20,30)
print(triangle.area())