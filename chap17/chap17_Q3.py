"""
Pythonのreモジュールを使って、何かの文字の後ろに o が２回登場する単語に一致する正規表現を書こう。
そして、"The ghost that says boo haunts the loo" の文中にあるbooやlooに一致するか試そう
"""

# 正解！自分のコードは問題の文をmという変数に入れてから re.findall の引数に渡しているが、やっている事は解答と同じ。


import re

m = "The ghost that says boo haunts the loo"

result = re.findall(".oo", m, re.MULTILINE)
print(result)