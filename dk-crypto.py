import helpers

running = True
helpers.printIntro()
helpers.printOptions()

while running:
    userIn = input('\nType the currency symbol you want a rate for: \n> ')

    if (helpers.validateUserIn(userIn)):
        response = helpers.getCurrencies(userIn.upper())
        print('\n' + response[0]["name"] + ' (' + response[0]["symbol"] + ') is currently evaluated at USD $' + helpers.roundValue(response[0]["price"]) + '.')
        check = input('Convert another coin? (Y/N):\n> ')
        if check.upper() == 'N' or check.upper() == 'NO':
            running = False
    else:
        print('\nWhoops! \'' + userIn + '\' wasn\'t valid input.')
        helpers.printOptions();

print('\n---------')
print('Quitting...')
print('Have a great day!')
print('-dk')
