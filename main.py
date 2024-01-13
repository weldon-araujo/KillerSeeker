import requests
import time
import io
import colorama
from args import options


arguments = options()


def status_200():
    with open(arguments.wordlist, 'r') as fil:
        lines = fil.readlines()
        for line in lines:
            req = requests.get(instance_target+line)
            if req.status_code == 200:
                print(f'success {req.status_code} {line}')


def main_status():         
    with open(arguments.wordlist, 'r') as fil:
        lines = fil.readlines()
        for line in lines:
            req = requests.get(instance_target+line)
            if req.status_code == 200:
                print(f'success {req.status_code} {line}')
            elif req.status_code == 301:
                print(f'redirect {req.status_code} {line}')
            elif req.status_code == 403:
                print(f'forbidden {req.status_code} {line}')


if arguments.target:
    instance_target = arguments.target
    main_status()
