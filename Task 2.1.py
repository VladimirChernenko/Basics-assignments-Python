int1 = 5
float1 = 3.14
complex1 = complex(1, 2)
none_type1 = None
bool1 = True
line1 = "Number Pi"
cortege1 = tuple(line1)
multitude1 = set(line1)
dictionary1 = dict(line1=float1)
list1 = [int1, float1, complex1, none_type1, bool1, line1, cortege1, multitude1, dictionary1]
for i in range(len(list1)):
    print(type(list1[i]))
