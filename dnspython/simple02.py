# coding:utf-8
# DNS
import dns.resolver

domain = raw_input('Please input a domain: ')
A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
	print j.address

