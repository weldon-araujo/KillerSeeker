import argparse

def options():
    parser = argparse.ArgumentParser(description='This is spider for discovery directories and files in web servers')

    parser.add_argument('-u', dest='target', required=True, help='target for spider')
    parser.add_argument('-w', dest='wordlist', required=True, help='file or path wordlist')
    parser.add_argument('-T', dest='time', required=None, help='time for every single request')

    return parser.parse_args()

#options()