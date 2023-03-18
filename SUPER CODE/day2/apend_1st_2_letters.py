def function(string):
    if len(string)<2:
         return -1
    else:
        return string[0:2]+string[-2:]
# string=["manikanta"]
print(function("string"))