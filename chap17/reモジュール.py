# reモジュールのfindall関数を使って、あるテキストから、あるテキストを検索、抽出する

import re

txt = "Beautifull is better than ugly"
matches = re.findall("Beautifull", txt)       #第1引数に検索したい文字列、第2引数に検索元を入れる

print(matches)



#reモジュールのfindall関数を使って、あるテキストから、あるテキストを検索、抽出する.大文字、小文字を無視して検索したい場合は、findall関数の3つ目の引数にre.IGNORECASEと入れる。

import re

txt = "Beautifull is better than ugly"
matches = re.findall("beautifull", txt, re.IGNORECASE)       #第1引数に検索したい文字列、第2引数に検索元を入れる,小文字を無視して検索したい場合は、findall関数の3つ目の引数にre.IGNORECASE

print(matches)