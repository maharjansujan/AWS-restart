dict={
    "Name":"sujan",
    "Age" :16,
    "Salary":100000


}
print(dict)

dict.update({"Age": 18})
dict["Age"]=19
dict["Company"]="Unlimited"
key=dict.values()
#remove age form list
dict.pop("Age")
print(dict)
print(len(dict))
