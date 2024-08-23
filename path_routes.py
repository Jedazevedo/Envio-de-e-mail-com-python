# caminhos de busca
import json
'''
#informe o seu caminho após c:/
exemplo: 'c:\\user\\desktop\\content_email.html' 1
exemplo: 'c:\\user\\desktop\\dados_de_acesso.json' 2
exemplo: 'c:\\user\\desktop\\Ebase.csv' 3
'''
CONTENT_EMAIL = 'C:\\content_email.html' #informe 1 
PATH_PASS = 'C:\\dados_de_acesso.json'   #informe 2
BASE_EMAIL = 'C:\\Ebase.csv'             #informe 3

with open(PATH_PASS, 'r') as senha:
    access_credences = json.load(senha)
    MY_EMAIL = access_credences['E_MAIL']
    #print(MY_EMAIL)


with open(PATH_PASS, 'r') as senha:
    access_credences = json.load(senha)
    MY_PASS = access_credences['SENHA']
    #print(MY_PASS)