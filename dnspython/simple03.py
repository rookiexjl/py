# coding: utf-8
# DNS
import dns.resolver

domain = raw_input('Please input a domain: ')
MX = dns.resolver.query(domain, 'MX')
for i in MX:
    print 'MX preference =', i.preference, 'email exchanger =', i.exchange

