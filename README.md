# DNSearch

A tool that finds the avalible DNS records for a given domain, and can do a fuzz search for give pages (Currently set up of admin pages)

## Imports
- dns
- dns.resolver
- requests
- http

## Types of domain records
```json
records = [
    'A',
    'AAAA',
    'MX',
    'CNAME',
    'TXT',
    'NS',
    'SRV',
    'SOA',
    'PTR',
    'ALIAS',
    'CAA',
    'CERT',
    'DHCID',
    'RT',
    'HINFO',
    'MB'
    ]
```
