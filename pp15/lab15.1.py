
def safe_int(arg):
    try:
        return int(arg)
    except:
        return None

print(safe_int(1))
print(safe_int(7.9))
print(safe_int("jeden"))