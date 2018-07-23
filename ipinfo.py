from ipwhois import IPWhois
import argparse
from pprint import pprint
import re

def get_ip_info(addr):
    '''
    Get information about an IP address.

    This script returns certain fields, as well as the entire WHOIS record.

    To see the whole record, do:

        result = get_ip_info('0.0.0.0')
        pprint result['info']
    '''
    result = {}
    # Retrieve WHOIS info
    info = IPWhois(addr).lookup_rdap(depth=1)
    result['info'] = info
    # Parse entity
    entity = info['entities'][0]
    result['entity'] = entity
    # Parse organization name
    name = info['objects'][entity]['contact']['name']
    result['name'] = name
    # Return result
    return result

def main():
    # Get list of IP addresses
    parser = argparse.ArgumentParser(description='Find information about an IP address')
    parser.add_argument('iplist', type=str,help='the file that contains a list of IP addresses')
    args = parser.parse_args()
    iplist = args.iplist
    # Process each IP address
    lines = [val.strip() for val in open(iplist, 'r')]
    i = 0
    for address in lines:
        i = i + 1
        print '--'
        print 'Processing IP address ' + str(i) + ' of ' + str(len(lines))
        try:
            result = get_ip_info(address)
            print address
            print result['name']
        except Exception as e:
            print '**Error**'
            print e
    # Print stats
    print '-' * 80
    print 'Total IP addresses processed: ' + str(len(lines))

if __name__ == '__main__':
    main()
