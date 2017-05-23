import pxssh


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print s.before


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connection'
    conn_str = 'ssh ' + user + '@' + host
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print '[-] Error Connecting'
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
    if ret == 0:
        print '[-] Error Connecting'
        return
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    host = 'localhost'
    user = 'root'
    password = 'root'
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')


if __name__ == '__main__':
    main()
