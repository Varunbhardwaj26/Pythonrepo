import re
def cleanstr(str1):
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', str1)
    return cleaned

print(cleanstr("This is a @@ student."))
 
 

  