from datetime import datetime

before = 'Mon Mar 11 14:09:34 +0000 2019'
after ='Mon Mar 11 17:09:34 +0000 2019'


before_date = datetime.strptime(before, '%a %b %d %H:%M:%S %z %Y')
after_date = datetime.strptime(after, '%a %b %d %H:%M:%S %z %Y')

print(before_date < after_date)