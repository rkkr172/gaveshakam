
print("Welcome to India".find("l"))
print("Welcome to India".find("o",5,10)) 
# start-5th, end-10th place

print("Hello Raja Text".split())
print("July-Aug XYZ".split())
print("2*2=4".split("*"))

print("\tTAB")
print(r"\tTAB") # raw pringting

#import re # part13
#print(re.findall("[06-9]","1+2==3"))
#print(re.findall(^"[0-9]","1+2==3"))

# Vid_13
print(re.findall(r'[0-9]','1+2==3'))
print(re.findall(r'[a-cA-Z0-5]','Barbeque Nation Cc249'))

# Vid_14
print(re.findall(r"[0-9]","Mr Tyagi 8943"))
print(re.findall(r"[A-Z]","Mr KumarM 1264"))
print(re.findall(r"[0-9]","9-6==3"))
