# ip-address-info

Get WHOIS information about an IP address.

Use it to get information about a list of IP addresses contained in `iplist.txt`:

    $ python -W ignore ipinfo.py iplist.txt

Or, import it to get information about an IP address:

    import ipinfo

    results = ipinfo.get_ip_info('8.8.8.8')
    print results['name']

