# coding: utf-8
# DNS
import dns.resolver

domain = raw_input('Please input a domain: ')
NS = dns.resolver.query(domain, 'NS')
for i in NS.response.answer:
    for j in i.items:
	print j.to_text()

