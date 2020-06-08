from git import repo
repo = Repo('/data/project/zppixbot/ZppixBot')
out = repo.pull('origin', 'master')
print(out)
