import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from path_routes import MY_EMAIL, MY_PASS, BASE_EMAIL, CONTENT_EMAIL
import csv

send_sucess = []
def enviar_email_html(destinatario, assunto, arquivo_html):
    with open(arquivo_html, 'r', encoding='utf8') as f:
                html = f.read()

                print('Enviando aguarde!...')
                msg = MIMEMultipart()
                msg['From'] = MY_EMAIL
                msg['To'] = destinatario
                msg['Subject'] = assunto
                msg.attach(MIMEText(html, 'html'),)

    try: 
        """
        caso o email for gmail só trocar smtp-mail.outlook.com', 587
        pelos dados do gmail.
        gmail terá que desativar vericação de duas etapas!
        """     
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp: #587
                smtp.starttls()
                smtp.login(MY_EMAIL, MY_PASS)
                smtp.sendmail(MY_EMAIL, destinatario, msg.as_string())
                print(f'E-mail enviado com sucesso: {destinatario}')
                send_sucess.append(destinatario)
                

    except smtplib.SMTPException as error:
                print(f" Error message: {str(error)}")

    except TimeoutError as error_server:
                print(f'Tempo do servidor expirou: {error_server}')
    
    
    
email_extc = []
with open(BASE_EMAIL, 'r', encoding='UTF8') as arquivo_email:
            reader = csv.reader(arquivo_email)
            for get_email in reader:
                email_extc.append(get_email)
        

for element in range(email_extc.__len__()):
            for intens_element in email_extc[element]:       
                receiver_email = intens_element
                if receiver_email == '':
                    continue
                print(intens_element)
                enviar_email_html(intens_element, 'Email de verificação - teste', CONTENT_EMAIL)

print(f'Envios:{send_sucess}\nTotal de Envios:{len(send_sucess)}')