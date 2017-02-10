# coding:utf-8
# DNS
import dns.resolver

domain = raw_input('Please input a domain: ')
cname = dns.resolver.query(domain, 'CNAME')
for i in cname.response.answer:
    for j in i.items:
	print j.to_text()

