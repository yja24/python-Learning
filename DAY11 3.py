mydictionary={1:'yep',2:'nope',3:'why',4:'what'}
print(mydictionary)
ans=mydictionary.copy()
ans1=mydictionary.get(1)
ans2=mydictionary.items()
ans3=mydictionary.keys()
print(ans)
print(ans2)
print(ans3)
print(ans1)


ans4=mydictionary.setdefault(5,33)
print(ans4)
print(mydictionary)