from git import *
repo = Git('/data/project/zppixbot/ZppixBot')
out = repo.pull('origin', 'master')
print(out)
