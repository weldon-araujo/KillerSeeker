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

def status_404():
    pass


def main_status():         
    with open(arguments.wordlist, 'r') as fil:
        lines = fil.readlines()
        for line in lines:
            url = urljoin("http://" + instance_target + "/", line)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
            if arguments.useragent:
                headers = headers.copy()
            else:
                headers = {}
            req = requests.get(url, headers=headers)
            if req.status_code == 200:
                print(f'{instance_target}/{line.strip()} \t {colored(req.status_code, "green")} success')
            elif req.status_code == 301:
                print(f'{instance_target}/{line.strip()} \t {colored(req.status_code, "blue")} moved to new location')
            elif req.status_code == 302:
                print(f'{instance_target}/{line.strip()} \t {colored(req.status_code, "blue")} temporarily moved to a new location')
            elif req.status_code == 403:
                print(f'{instance_target}/{line.strip()} \t  {colored(req.status_code, "yellow")} forbidden')
                
            

    
if arguments.target:
    instance_target = arguments.target
    main_status()