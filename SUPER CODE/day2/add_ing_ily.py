def function(string1):
    if len(string1) <3:
        return string1
    elif string1[-3:]=="ing":
        return string1 + "ly"
    else:
        return string1 + "ing"
print(function("amazing"))
print(function("is"))
print(function("sleep"))