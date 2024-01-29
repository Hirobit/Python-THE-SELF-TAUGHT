"""コンポジションが理解できないので参考書p167をまるまる書いてみる
犬は一人の飼い主を持つを表現しているらしい。"""

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

person = Person("Mick Jagger")              #Mick Jaggerという名前を持つPersonクラスをpersonという名前の変数でインスタンス化している。　つまり、personはMick Jaggerという名前の属性を持つ、Personクラスの実体
dog = Dog("stanley", "Bulldog", person)
print(dog.owner.name)                       #インスタンス化したdogの中のDogクラスの、ownerインスタンス変数＝Personクラスの、中のnameインスタンス変数を呼び出した
                                            #つまり、dogの中の(元Dogクラス)、ownerインスタンス変数の位置にpersonのnameを持ってきて使っている