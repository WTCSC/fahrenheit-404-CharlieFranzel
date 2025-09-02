import time

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def get_valid_choice(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        else:
            print(f"Invalid choice! Please enter one of: {', '.join(options)}")

while True:
    print('Hello, How can I help you today?')
    print('[1] Convert Celsius to Farenheit')
    print('[2] Convert Farenheit to Celsius')
    print('[3] Convert Farenheit to Kelvin')
    print('[4] Convert Celsius to Kelvin')
    print('[5] Convert Kelvin to Celsius')
    print('[6] Convert Kelvin to Farenheit')
    print('[7] Exit')

    choice = get_valid_choice('> ', ['1', '2', '3', '4', '5', '6', '7'])

    if choice == '1':
        print('Input temperature value only')
        celsius = get_valid_int('> ')
        output = celsius * 1.8 + 32
        time.sleep(0.5)
        print('Converting.')
        time.sleep(0.5)
        print('Converting..') 
        time.sleep(0.5)
        print('Converting...')
        time.sleep(0.5)
        print('Conversion complete!')
        print(f'{celsius} degrees Celsius is equal to {output} degrees Farenheit.')  
        time.sleep(1)
        print('Continue?')
        print('[1] Yes')
        print('[2] No')
        keepgoing = get_valid_choice('> ', ['1', '2'])
        if keepgoing == '1':
            continue
        else:
            break

    if choice == '2':
        print('Input temperature value only')
        farenheit = get_valid_int('> ')
        output = (farenheit - 32) * 0.55555
        time.sleep(0.5)
        print('Converting.')
        time.sleep(0.5)
        print('Converting..')
        time.sleep(0.5)
        print('Converting...')
        time.sleep(0.5)
        print('Conversion complete!')
        print(f'{farenheit} degrees Farenheit is equal to {output} degrees Celsius.')  
        time.sleep(1)
        print('Continue?')
        print('[1] Yes')
        print('[2] No')
        keepgoing = get_valid_choice('> ', ['1', '2'])
        if keepgoing == '1':
            continue
        else:
            break

    if choice == '3':
        print('Input temperature value only')
        farenheit = get_valid_int('> ')
        output = (farenheit - 32) * 0.55555 + 273
        time.sleep(0.5)
        print('Converting.')
        time.sleep(0.5)
        print('Converting..') 
        time.sleep(0.5)
        print('Converting...')
        time.sleep(0.5)
        print('Conversion complete!')
        print(f'{farenheit} degrees Farenheit is equal to {output} degrees Kelvin.')  
        time.sleep(1)
        print('Continue?')
        print('[1] Yes')
        print('[2] No')
        keepgoing = get_valid_choice('> ', ['1', '2'])
        if keepgoing == '1':
            continue
        else:
            break

    if choice == '4':
        print('Input temperature value only')
        celsius = get_valid_int('> ')
        output = celsius + 273
        time.sleep(0.5)
        print('Converting.')
        time.sleep(0.5)
        print('Converting..') 
        time.sleep(0.5)
        print('Converting...')
        time.sleep(0.5)
        print('Conversion complete!')
        print(f'{celsius} degrees Celsius is equal to {output} degrees Kelvin.')  
        time.sleep(1)
        print('Continue?')
        print('[1] Yes')
        print('[2] No')
        keepgoing = get_valid_choice('> ', ['1', '2'])
        if keepgoing == '1':
            continue
        else:
            break

    if choice == '5':
        print('Input temperature value only')
        kelvin = get_valid_int('> ')
        output = kelvin - 273
        time.sleep(0.5)
        print('Converting.')
        time.sleep(0.5)
        print('Converting..') 
        time.sleep(0.5)
        print('Converting...')
        time.sleep(0.5)
        print('Conversion complete!')
        print(f'{kelvin} degrees Kelvin is equal to {output} degrees Celsius.')  
        time.sleep(1)
        print('Continue?')
        print('[1] Yes')
        print('[2] No')
        keepgoing = get_valid_choice('> ', ['1', '2'])
        if keepgoing == '1':
            continue
        else:
            break

    if choice == '6':
        print('Input temperature value only')
        kelvin = get_valid_int('> ')
        output = (kelvin - 273) * 1.8 + 32
        time.sleep(0.5)
        print('Converting.')
        time.sleep(0.5)
        print('Converting..') 
        time.sleep(0.5)
        print('Converting...')
        time.sleep(0.5)
        print('Conversion complete!')
        print(f'{kelvin} degrees Kelvin is equal to {output} degrees Farenheit.')  
        time.sleep(1)
        print('Continue?')
        print('[1] Yes')
        print('[2] No')
        keepgoing = get_valid_choice('> ', ['1', '2'])
        if keepgoing == '1':
            continue
        else:
            break

    if choice == '7':
        print('Goodbye!')
        break

#  _,-=._              /|_/|      Meow
#  `-.}   `=._,.-=-._.,  @ @._,  /
#     `._ _,-.   )      _,.-'
#        `    G.m-"^m`m'        
