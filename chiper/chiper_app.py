import os
from colorama import Fore, Style, init
from chipers_for_app import caesar_cipher, breaking_caesar_cipher, zigzag_cipher, breaking_zigzag_cipher

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

ciphers = {
    '1': {
        'name': 'Caesar cipher',
        'func': caesar_cipher,
        'func_break': breaking_caesar_cipher,
        'key_desc': 'Enter shift (Enter for breaking):',
        'desc': 'Each letter is shifted a certain number of positions in the alphabet.',
        'settings': {'upper_letter': 'A', 'lower_letter': 'a', 'alphabet_size': 26, 'format_text': False},
    },
    '2': {
        'name': 'Zigzag cipher',
        'func': zigzag_cipher,
        'func_break': breaking_zigzag_cipher,
        'key_desc': 'Enter number of rows (Enter for breaking): ',
        'desc': 'The message is written in a zigzag pattern on an imaginary fence, then read off in rows.',
        'settings': {'format_text': False, 'symbol_for_space': 'X'},
    }
}


def setting(choice):
    global ciphers
    while True:
        clear()
        print('Current settings for', Fore.GREEN + Style.BRIGHT + ciphers[choice]['name'] + Style.RESET_ALL + ':')
        setting_with_index = enumerate(ciphers[choice]['settings'].items(), start=1)
        for index, (key, value) in setting_with_index:
            print(f'{index} - {key}: {value}')
        print('0 - Back')
        setting_choice = input(Fore.YELLOW + Style.BRIGHT + 'Choose setting: ' + Style.RESET_ALL)
        if setting_choice == '0' or setting_choice == '':
            return
        elif setting_choice in [str(i) for i in range(1, len(ciphers[choice]['settings']) + 1)]:
            setting_key = list(ciphers[choice]['settings'].keys())[int(setting_choice) - 1]
            setting_value = input(f'{Fore.YELLOW}{Style.BRIGHT}Enter new value for {setting_key}:{Style.RESET_ALL} ')
            ciphers[choice]['settings'][setting_key] = setting_value
        else:
            print(Fore.RED + Style.BRIGHT + 'Invalid choice. ' + Style.RESET_ALL + 'Enter to continue...', end='')
            input()

def main():

    while True:

        clear()
        print("""
 █████╗ ██╗██████╗ ██╗  ██╗███████╗██████╗   ████████╗ █████╗  █████╗ ██╗     
██╔══██╗██║██╔══██╗██║  ██║██╔════╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║     
██║  ╚═╝██║██████╔╝███████║█████╗  ██████╔╝     ██║   ██║  ██║██║  ██║██║     
██║  ██╗██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗     ██║   ██║  ██║██║  ██║██║     
╚█████╔╝██║██║     ██║  ██║███████╗██║  ██║     ██║   ╚█████╔╝╚█████╔╝███████╗
 ╚════╝ ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝    ╚════╝  ╚════╝ ╚══════╝
""")


        for key, value in ciphers.items():
            print(f'{key}. {value["name"]}')
        print('0. Exit')

        choice = input('Choose cipher: ')

        if choice == '0':
            break

        if choice in ciphers:
            while True:
                clear()

                print(Fore.GREEN + Style.BRIGHT + f'{ciphers[choice]["name"]}')
                print(ciphers[choice]['desc'])
                print('Settings:', end=' ')
                print(', '.join([f'{key}: {value}' for key, value in ciphers[choice]['settings'].items()]))
                print('0 - Back, s - Settings')
                text = input(Fore.YELLOW + Style.BRIGHT + 'Enter text: ' + Style.RESET_ALL)
                if text == '0':
                    break

                elif text.lower() == 's':
                    setting(choice)
                    continue


                key = input(Fore.YELLOW + Style.BRIGHT + ciphers[choice]['key_desc'] + Style.RESET_ALL)

                if key:
                    print(Fore.GREEN + Style.BRIGHT + 'Result:')
                    print(ciphers[choice]['func'](text, int(key), ciphers[choice]['settings']))
                else:
                    print(Fore.GREEN + Style.BRIGHT + 'Breaking:')
                    ciphers[choice]['func_break'](text, settings=ciphers[choice]['settings'])
                input()

        else:
            print('Invalid choice')
            input('Press Enter to continue...')


if __name__ == '__main__':
    main()