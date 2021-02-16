from calendar import monthrange
from datetime import datetime

today = datetime.today()

mr = monthrange(today.year, today.month)

n_days = mr[1]

progress = int(today.day / n_days * 100)

p = ""
p += "["
for i in range(1, 20):
	if progress / 5 < i:
		p += "□"
	else:
		p += "■"
p += "]"
p += str(progress) + "%"

print(today.strftime("%B"))
print(p)
