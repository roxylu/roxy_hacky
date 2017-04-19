#!/usr/bin/env python
import argparse
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, \
                   gethostbyaddr, setdefaulttimeout


def conn_scan(target_host, target_port):
    try:
        conn_socket = socket(AF_INET, SOCK_STREAM)
        conn_socket.connect((target_host, target_port))
        conn_socket.send('HelloWorld\r\n')
        results = conn_socket.recv(100)
        print '[+]%d/tcp open' % target_port
        print '[+] ' + str(results)
        conn_socket.close()
    except:
        print '[-]%d/tcp closed' % target_port


def port_scan(target_host, target_ports):
    try:
        target_ip = gethostbyname(target_host)
    except:
        print "[-] Cannot resolve '%s': Unkown host" % target_host
        return

    try:
        target_name = gethostbyaddr(target_ip)
        print '\n[+] Scan Results for: ' + target_name[0]
    except:
        print '\n[+] Scan Results for: ' + target_ip

    setdefaulttimeout(1)

    for target_port in target_ports:
        print 'Scanning port ' + target_port
        conn_scan(target_host, int(target_port))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', dest='target_host',
        help='specify target host')
    parser.add_argument('-p', dest='target_port',
        help='specify target port[s] separated by comma')
    args = parser.parse_args()
    target_host = args.target_host
    target_ports = str(args.target_port).split(', ')
    if (target_host == None) | (target_ports[0] == None):
        parser.print_help()
        exit(0)
    port_scan(target_host, target_ports)


if __name__ == '__main__':
    main()
