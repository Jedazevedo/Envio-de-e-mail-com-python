# caminhos de busca
import json
CONTENT_EMAIL = 'C:/content_email.html'
PATH_PASS = 'C:/dados_de_acesso.json'
BASE_EMAIL = 'C:/Ebase.csv'

with open(PATH_PASS, 'r') as senha:
    access_credences = json.load(senha)
    MY_EMAIL = access_credences['E_MAIL']
    #print(MY_EMAIL)


with open(PATH_PASS, 'r') as senha:
    access_credences = json.load(senha)
    MY_PASS = access_credences['SENHA']
    #print(MY_PASS)