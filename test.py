from decouple import config

COMMIT_SHA = config('COMMIT_SHA')
print(COMMIT_SHA)