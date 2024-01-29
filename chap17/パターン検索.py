# [ow]は、oまたはwのどちらか１文字が該当するデータを持って来る。つまり "t[ow]o" の意味は、最初の文字はt、次点でoまたはw、最後にo、が該当するデータをstringの中から検索して持って来ているということ。

import re

string = "Two too. towo twoo"
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)