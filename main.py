import requests
import time
import io
from termcolor import colored
from args import options
from urllib.parse import urljoin


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
            #req = requests.get('https://' + instance_target + line)
            url = urljoin("https://" + instance_target + "/", line)
            req = requests.get(url)
            if req.status_code == 200:
                print(f'{instance_target}/{line} {colored(req.status_code, "blue")}')
            elif req.status_code == 301:
                print(f'{instance_target}/{line} {colored(req.status_code, "blue")}')
            elif req.status_code == 403:
                print(f'{instance_target}/{line} {colored(req.status_code, "yelow")}')
            elif req.status_code == 404:
                print(f'{instance_target}/{line} {colored(req.status_code, "red")}')

def useragent():
    pass


if arguments.target:
    instance_target = arguments.target
    main_status()