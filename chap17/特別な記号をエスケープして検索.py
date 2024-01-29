# $記号は特別な意味を持つが、エスケープ処理をすることで、特別な意味を持たないただのドル記号として扱うことが出来る

import re

line = "I love $"
m = re.findall("\\$", line, re.IGNORECASE)
print(m)