import requests
import time
import io
import colorama
from args import options


arguments = options()



def status_200():
    pass

if arguments.target:
    target =arguments.target
    with open(arguments.wordlist, 'r') as fil:
        lines = fil.readlines()
        for line in lines:
            req = requests.get(target+line)
            if req.status_code == 200:
                print(f'success {"200"} {line}')
            elif req.status_code == 301:
                print(f'redirect {req.status_code} {line}')
            elif req.status_code == 403:
                print(f'forbidden {req.status_code} {line}')
  



# aqui é o teste de colorir a saida que ainda vou implementar depois
'''
colorama.init()

print(colorama.Fore.RED + "Esta string é vermelha!")
print(colorama.Fore.GREEN + "Esta string é verde!")
print(colorama.Fore.YELLOW + "Esta string é amarela!")

colorama.deinit()
'''