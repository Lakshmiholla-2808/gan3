def bad(item, bucket=[]):
    bucket.append(item)
    return bucket

print(bad(1), bad(2))   # [1] then [1, 2]  <- surprise

def good(item, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(item)
    return bucket

print(good(1), good(2))
