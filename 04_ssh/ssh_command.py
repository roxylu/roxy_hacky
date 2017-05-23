from pexpect import pxssh


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before


def connect(user, host, password):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        return s
    except:
        print '[-] Error Connecting'
        exit(0)


def main():
    host = 'localhost'
    user = 'root'
    password = 'root'
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')


if __name__ == '__main__':
    main()
