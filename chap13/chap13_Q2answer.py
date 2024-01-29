#答えの方は正方形の縦横をすべてs1と１辺だと考えている。
#自分の答えは１辺を縦と横に区別し、問題文にあった横幅のサイズ変更を実装している。
#答えのコードでは横幅だけでなく全ての辺がサイズ変更されるので私のコードの方が優れているのでは。出力されるデータは同じ。100億点です！！！

class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)