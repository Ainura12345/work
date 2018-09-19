#Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
"""
a=input()

b=a.split(".")
print((b[1]))

"""

#Write a Python program to display the first and last colors from the following list.
"""
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[len(color_list)-1])
"""

#  Write a Python program that accepts an integer (n)
#and computes the value of n+nn+nnn

a=int(input())
n1=int("%s" % a)
n2=int("%s%s" % (a,a))
n3=int("%s%s%s" % (a,a,a))
n=n1+n2+n3
print(n)
