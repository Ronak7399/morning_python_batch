# set datatype
# frozan datatype

# list data = [12,24,23,23]
# tupal = (12,124,423)
# dictionary = {"name": "bascom"}
# set

list = {112,2443,56,34,23,35,12,35}
# can not take duplicat values
# don't no maintain order # unordered

print(list)
print(type(list))

list.add(13)

print(list)

list2 = {55,66,77,88}
list.update(list2)
print(list)

list3 = [12,35,65]
list.update(list3)

print(list3)

list.discard(12)
print(list)

list.pop()
print(list)

#list => set

name = [ "hello","hi","kem cho","hello"]

print(name)

name2 = frozenset(name)

print(name2)


