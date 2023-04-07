from functions import *
from datetime import datetime


content = get_json()

dat = find_last_five(content)
for i in dat:
    thedate = datetime.fromisoformat(i)
    print(thedate.year)