import sys
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

def sortSecond(val):
    return val[2] 
array=[]
for line in sys.stdin:
    value=line.split()
    value[2]=int(value[2])
    array.append(value)
array.sort(key=sortSecond) 
for i in array:
    print(name_format(i))
    
    
# todo eso s epuede resumi en un lambda:
return map(f, sorted(people, key=lambda x: int(x[2])))
