familyNames = []
while True:
    print("Enter the name of family member " + str(len(familyNames)+1)
          + " (Or press enter to stop.):")
    name = input()
    if name == '':
        break
    familyNames = familyNames + [name]
print("Your family member names are:")
for name in familyNames:
    print(' '+name)
