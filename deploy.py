from git import *
import time
from datetime import datetime, date
start = time.time()
repo = Git('/data/project/zppixbot/ZppixBot')
out = repo.pull('origin', 'master')
if out == 'Already up to date.':
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print('[{0} - {1}] Found nothing to update in {2}s'.format(today,current_time,str(time.time()-start)[:3]))

