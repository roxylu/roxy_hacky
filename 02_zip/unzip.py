import zipfile
import optparse
from threading import Thread


def extract_file(z_file, password):
    # Extract with correct pwd
    # z_file.extractall(pwd='roxy')
    try:
        z_file.extractall(pwd=password)
        print '[+] Password = ' + password
    except Exception, e:
        pass


def main():
    parser = optparse.OptionParser("usage%prog " + \
        "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='z_name', type='string',
                      help='specify zip file')
    parser.add_option('-d', dest='d_name', type='string',
                      help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.z_name == None) | (options.d_name == None):
        print parser.usage
        exit(0)
    else:
        z_name = options.z_name
        d_name = options.d_name

    z_file = zipfile.ZipFile(z_name)
    pass_file = open(d_name)
    for line in pass_file.readlines():
        password = line.strip()

        #extract_file(z_file, password)
        # Multithreading
        t = Thread(target=extract_file, args=(z_file, password))
        t.start()


if __name__ == '__main__':
    main()
