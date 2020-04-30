from datetime import datetime, timedelta

dfr = datetime.now() - timedelta(days=1)
print (dfr)
if datetime.now() > dfr:
    print (True)
