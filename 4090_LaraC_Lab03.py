#Christian Lara
#000983220
#Jul/1/2021
#Jul/1/2021
#The purpuse of this pprogram is to calculate the sales taxes that a costumer
#has to pay. The program will chrge different rates depending on which state the
#purchase was made, the program will not accept 0 or nagative numbers for the amount
#and it wil only accept some states of the nation.

#asks user for the weight of the package
weightOfPackege = float(input('Enter the weight of the package: '))
#define booleab variables to validate data
validWeight = True
validState = True

#it assigns a rate per pound or gives an error if incorrect data is entered
if weightOfPackege > 0 and weightOfPackege <= 2:
    ratePerPound = 1.50
elif weightOfPackege > 2 and weightOfPackege <= 6:
    ratePerPound = 3.00
elif weightOfPackege > 6 and weightOfPackege <= 10:
    ratePerPound = 4.00
elif weightOfPackege > 10:
    ratePerPound = 4.75
else:
    #makes the boolen false so the progam will end here
    validWeight = False
    print('Invalid entry. Weight of package must be greater than zero.')

#if the first input is valid the program will request the state abbreviation and convert the string to upper case
if validWeight == True:
    stateAbbreviation = str(input('Enter the state abbreviation to ship to: '))
    stateAbbreviation = stateAbbreviation.upper()

    #the program assign a state sales tax rate or it will give an error if incorrect data is entered
    if stateAbbreviation == 'AR':
        stateSalesTaxRate = 6.50
    elif stateAbbreviation == 'KS':
        stateSalesTaxRate = 6.50
    elif stateAbbreviation == 'LA':
        stateSalesTaxRate = 5.00
    elif stateAbbreviation == 'NM':
        stateSalesTaxRate = 5.125
    elif stateAbbreviation == 'OK':
        stateSalesTaxRate = 4.50
    elif stateAbbreviation == 'TX':
        stateSalesTaxRate = 6.25
    else:
        #turns the valid state boolean to falso so the program will end here
        validState = False
        print('Invalid entry. State abbreviation must be AR or KS or LA or NM or OK or TX.')



    if validState == True:
        #calculates the shiiping charge, sales tax, and total
        print('SHIPPING SUMMARY')
        shippingCharge = weightOfPackege * ratePerPound
        salesTax = shippingCharge * stateSalesTaxRate / 100
        totalShippingCharge = shippingCharge + salesTax

        #prints the resutls of the calculations
        print('The rate per pound is $' + str(format(ratePerPound, ',.2f')))
        print('The shipping charge is $' + str(format(shippingCharge, ',.2f')))
        print('the state to be shipped is to ' + stateAbbreviation)
        print('The state sales tax rate is ' + str(format(stateSalesTaxRate, '.3f')) + '%')
        print('The state sales tax is $' + str(format(salesTax, ',.2f')))
        print('The total shipping charge is $' + str(format(totalShippingCharge, ',.2f')))
