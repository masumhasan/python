notice = '''
Dear <|name|>
You Are Selected
Date: <|date|>
'''
name = input("Enter Your Name: \n")
date = input("Enter Application Receiving date:\n")
s = notice
s = s.replace("<|name|>", name)
s = s.replace("<|date|>", date)
print(s)
