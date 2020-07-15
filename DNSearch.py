import dns
import dns.resolver
import requests
import http

domain = input("Enter the Domain: ")

#DNS Record Types
searchs = [
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

for types in searchs:
    try:
        t = dns.resolver.query(domain, types)
        for i in t.response.answer:
            for j in i.items:
                print(types + " Record: ", j.to_text())
    except:
        print(types + " Record: N/A")


tests = input("Run admin page search? (y/n): ")

if tests == "y":
    #admin page search
    urls = [
        "admin",
        "wp-admin",
        "wp-login",
        "login",
        "config"
    ]

    for x in urls:
        r = requests.get("http://" + domain + "/" + x)
        if r.status_code != 404:
            print(x, r.status_code, r.headers['Content-Type'])
