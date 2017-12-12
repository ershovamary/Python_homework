#Classwork from 7 December 2017
#объявление функции (могут использоваться те же переменные, что и в body)
def welcome_traveller(username):
    if len(username) > 0:
        print('I am glad to see you in Gondor, traveller ' + username)
    else:
        print('You have not introduced yourself, traveller...')
def welcome_fellow(username):
    if len(username) > 0:
        print('I am glad to see you in Gondor too, traveller ' + username)
    else:
        print('You have not introduced your fellow, traveller...')

#вызов функции
def main():
    a = input('Could you please write your name? ')
    welcome_traveller(a)
    b = input('May I also ask the name of your fellow? ')
    welcome_fellow(b)
    i = 0
    while i == 0:
        x = input('Is there any other fellow with you? ')
        if x == 'Yes' or x == 'yes' or x == 'Yeah' or x == 'yeah' or x == 'Yep' or x == 'yep':
            welcome_fellow(input('And how is your other fellow called? '))
        else:
            print('You may continue your way to our beautiful town.')
            i = 1

if __name__ == '__main__':
    main()
