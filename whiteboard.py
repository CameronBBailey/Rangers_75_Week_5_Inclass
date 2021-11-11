#Find Bold Words In String
#Given a string as a parameter to a function, find all of the words inside the string that should be bolded. A bolded word starts with any of the regular vowels in the alphabet. Return the words that should be bolded in a list/array
#Example:
#Input: The Black Dog sits among the apple tree
#Output: [ 'among', 'apple']
#Input: The umbrella company strikes again.
#Output: [ 'umbrella', 'again']



def bold(w):
    v = ['a','e','i','o','u']
    newlist = []
    alist = w.split(' ')
    for i in alist:
        if i[0].lower() in v:
            newlist.append(i)
    return newlist

print(bold('The umbrella company strikes again.'))
print(bold('Are you more of an Uber-er or Lift-ee?'))


def bolded(astring):
    alist = astring.split(' ')
    return [x for x in alist if x[0].lower() in 'aeiou']
