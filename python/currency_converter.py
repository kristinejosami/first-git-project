'''
Create a program that:
Contains information on currency conversion rates from USD to four other currencies
User can enter in an amount in USD and the currency they want to convert it into
The programme then outputs the amount in the new currency
'''
print('This is a Currency Converter')
country_currency={'Philippines':49.03,'Japan':105.48,'UAE':3.67,'Taiwan':29.36}
your_money=int(input('Enter amount in USD:'))
currency=input('Enter country name (Philippines,Japan,UAE,Taiwan): ')
converter = your_money * country_currency[currency]
print('The currency conversion is {}.'.format(converter))
'''
if currency == 'Philippines':
    print('The currency conversion is {} pesos.'.format(converter))
elif currency == 'Japan':
    print('The currency conversion is {} yen.'.format(converter))
elif currency == 'UAE':
    print('The currency conversion is {} dirham.'.format(converter))
else:
    print('The currency conversion is {} NT dollar.'.format(converter))
'''



