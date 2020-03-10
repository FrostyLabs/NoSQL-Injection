# NoSQL-Injection
Blind MongoDB NoSQL Injection tool. Must have a known username. 

It works on the basis that a successful login attempt responds with HTTP satus 302. 

## Usage
```
$ ./blind-nosql.py --help
 ____  _ _           _       _   _      ____   ___  _     _ 
| __ )| (_)_ __   __| |     | \ | | ___/ ___| / _ \| |   (_)
|  _ \| | | '_ \ / _` |_____|  \| |/ _ \___ \| | | | |   | |
| |_) | | | | | | (_| |_____| |\  | (_) |__) | |_| | |___| |
|____/|_|_|_| |_|\__,_|     |_| \_|\___/____/ \__\_\_____|_|
                                                            

usage: brute-argparse.py [-h] [-u USERNAME] [-t TARGET]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        The target username
  -t TARGET, --target-url TARGET
                        The target login page

``` 

Example (this is a fake URL): 

```
$ ./blind-nosql.py -u sam -t http://www.XXXXXX.com/nosql-login
```