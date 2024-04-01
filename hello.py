# This program says hello and asks for a name.

print('Hello cruel world!')
print('What is thy accursed name?')    # this line asks for name
theName = input()
print('Your cursed name is Wellington ' + theName)
print('The length of your cursed name is:')
print(len(theName) + 10)
print('What age are thoust?')
theAge = input()
print('Bhah, I will be ' + str(1054 - int(theAge)) + ' years older than you in 3 months.')
