# string methods in Python

userName : str = "Muhammad Afzal" # String with Double Quote
print(userName)

name : str = 'afzal faizi' # string with single quote
print(name)

myName : str = '''afzal faizi''' # string with triple quote
print(myName)

## Define multiline string "" "" "" triple line string
studentName : str = "Muhammad Afzal"
fName : str = "Iqbal Yousaf"
age : int = 26
qualifaction : str = "Cloud Computing and Agentic AI Engineering."
address : str = "Chak No 5 Kalan G.B P/O same Tahsil & District Nankana Sahib"

card : str = f"""
PIAIC Student Card
Student Name : {studentName}
First Name : {fName}
Age : {age}
Qualification : {qualifaction}
Address : {address}

"""
print(card)