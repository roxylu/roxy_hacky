import nmap
import argparse


def nmap_scan(target_host, target_port):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(target_host, target_port)
    state = nm_scan[target_host]['tcp'][int(target_port)]['state']
    print "[*] " + target_host + " tcp/" + target_port + " " + state


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', dest='target_host', help='specify target host')
    parser.add_argument('-p', dest='target_port', help='specify target port[s] separated by comma')
    args = parser.parse_args()
    target_host = args.target_host
    target_ports = str(args.target_port).split(', ')
    if (target_host == None) | (target_ports[0] == None):
        parser.print_help()
        exit(0)

    for target_port in target_ports:
        nmap_scan(target_host, target_port)


if __name__ == '__main__':
	main()
