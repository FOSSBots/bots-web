from git import *
import time
from datetime import datetime, date
import os, subprocess
start = time.time()
## WARNING ##
# This script should not be changed without caution. 
# It will auto-deploy every 15 minutes and changes can break the auto-deploy infrastructure.
# This script auto-logs and if that fails can spam #wikimedia-cloud.
## WARNING ##
repo = Git('/data/project/zppixbot/ZppixBot')
out = repo.pull('origin', 'master')
if out == 'Already up to date.' or out == 'Already up-to-date.':
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print('[{0} - {1}] Found nothing to update in {2}s'.format(today,current_time,str(time.time()-start)[:3]))
else:
    repo = Repo('/data/project/zppixbot/ZppixBot')
    for submodule in repo.submodules:
        out = submodule.update(init=True)
    subprocess.call(['sh', '/data/project/zppixbot/ZppixBot/logmsg.sh', 'auto-update@website: Synced website repo in {0}s'.format(str(time.time()-start)[:3])])