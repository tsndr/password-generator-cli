#!/usr/bin/env python3
import sys
import string
import random
import getopt

def usage(password_length, number_of_passwords, charcters):
    print('Usage: ' + sys.argv[0] + ' [OPTIONS]')
    print('')
    print('  -h, --help         This dialog')
    print('  -l, --length       Password length (default: ' + str(password_length) + ')')
    print('  -c, --count        Number of passwords (default: ' + str(number_of_passwords) + ')')
    print('      --chars        List of charcters (default: ' + charcters + ')')

def generate_passsword(password_length, charcters):
    return ''.join([random.choice(charcters) for _ in range(password_length)])

def main():
    password_length = 16
    number_of_passwords = 1
    charcters = string.ascii_letters + string.digits

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hl:c:', ['help', 'length=', 'count=', 'chars='])
    except getopt.GetoptError as err:
        print(err)
        usage(password_length, number_of_passwords, charcters)
        sys.exit(2)
    
    for k, v in opts:
        if k == '-h':
            usage(password_length, number_of_passwords, charcters)
            sys.exit()
        elif k == '-l' or k == '--length':
            password_length = int(v)
        elif k == '-c' or k == '--count':
            number_of_passwords = int(v)
        elif k == '--chars':
            charcters = v
        else:
            continue
    for i in range(number_of_passwords):
        print(generate_passsword(password_length, charcters))

if __name__ == '__main__':
    main()
