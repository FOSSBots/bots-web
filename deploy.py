from git import *
import time
from datetime import datetime, date
import os
start = time.time()
repo = Git('/data/project/zppixbot/testrepo')
out = repo.pull('origin', 'master')
if out == 'Already up to date.':
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print('[{0} - {1}] Found nothing to update in {2}s'.format(today,current_time,str(time.time()-start)[:3]))
else:
    repo = Repo('/data/project/zppixbot/testrepo')
    for submodule in repo.submodules:
        out = submodule.update(init=True)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    os.system('dologmsg "auto-update@website: Synced website repo in {0}s"'.format(str(time.time()-start)[:3]))
