from git import *
repo = Git('/Users/samuelkirwin/ZppixBot')
out = repo.pull('origin', 'master')
print(out)
