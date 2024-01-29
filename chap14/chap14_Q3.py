"""
2つのパレメーターを受けとる関数を書く、この関数は同じオブジェクトを渡されたらTrue と返し、そうじゃなかったらFalse を返す。
"""

class Judge:
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2

    def isfunction(self):
        if self.in1 is self.in2:
            return True
        else:
            return False
        

judge1 = Judge(10, 10)
print(judge1.isfunction())

judge2 = Judge(100, 10)
print(judge2.isfunction())

judge3 = Judge("aaa", "aaa")
print(judge3.isfunction())


judge4 = Judge("aaa", "zzz")
print(judge4.isfunction())