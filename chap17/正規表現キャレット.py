#　python正規表現でキャレット記号(^)を使って、行の先頭に一致する文字列を抽出

import re

zen = """Although never is 
often better than 
*right* now.
If the implementation 
is hard to explain, 
it's a bad idea.
If the implementation 
is easy to explain, 
it may be a good 
idea.Namespaces 
are one honking 
great idea -- let's 
do more of those!"""

m = re.findall("^If", zen, re.MULTILINE)         # re.MULTILINE を第3引数に入れることで複数行のテキストを、複数行として扱う,とpythonに教えている
print(m)