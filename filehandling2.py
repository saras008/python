f=open("/Users/saras008/repo-iyus/python/test.txt", "a")

# a = append
# r = read
# w = overwrite
# x = create new file
f.write("\nThis is a newline using append")
f.close()

f=open("/Users/saras008/repo-iyus/python/test.txt", "r")

print(f.read())

f=open("test2.txt", "x")
