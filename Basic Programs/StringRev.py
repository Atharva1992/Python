def reversestring (str) :
    strlength = len(str)
    i = 0
    while i < strlength :
        print(str[i])
        j = str[i]
        i = i + 1
        strrev[strlength - i] = j
#    while j < strlength :
#       strrev[strlength-j] = str[j]
#    print(strrev)

 #       strrev[int(strlength-i)] = str[i]
  #  print(strrev)
    
str = input("Enter Your Name :")

reversestring(str)
