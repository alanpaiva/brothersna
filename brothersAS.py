import random
import smtplib
import ssl
import time
from email.message import EmailMessage

def realizar_sorteio(participantes):
    """Realiza o sorteio do amigo secreto, garantindo que ninguém tire a si mesmo."""
    nomes = list(participantes.keys())
    sorteio_valido = False

    while not sorteio_valido:
        random.shuffle(nomes)
        sorteio_valido = all(nomes[i] != list(participantes.keys())[i] for i in range(len(nomes)))

    pares = {}
    for i, nome in enumerate(participantes.keys()):
        pares[nome] = nomes[i]

    return pares

def enviar_emails(pares, participantes, remetente_email, remetente_senha):
    """Envia e-mails para cada participante com o resultado do sorteio."""
    smtp_server = "smtp.gmail.com"  # Servidor SMTP do Gmail (mude se usar outro)
    smtp_port = 587  # Porta para STARTTLS (ou 465 para SSL/TLS)

    # Cria um contexto SSL seguro
    context = ssl.create_default_context()

    try:
        # Conecta-se ao servidor SMTP e faz login
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()  # Saudação inicial
            server.starttls(context=context)  # Inicia a segurança TLS
            server.ehlo()
            server.login(remetente_email, remetente_senha)

            # Envia e-mails individualmente
            for remetente, destinatario in pares.items():
                destinatario_email = participantes[remetente]
                
                # Cria a mensagem de e-mail
                msg = EmailMessage()

                msg.set_content(f"""
                <html>
                  <body style="font-family: Arial, sans-serif; line-height: 1.7; color: #222;">
                    <div style="max-width: 600px; margin: 0 auto; background: #f9f9f9; border-radius: 12px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
                      <h2 style="text-align: center; color: #1b5e20;">🎁 Amigo Secreto 2025 🎁</h2>

                      <p>Fala meu filhão <b>{remetente}</b>, blza?! 😎</p>

                      <p>Este é o nosso <b>amigo secreto de 2025</b>... 
                      Sim, o evento do ano mais <b>esperado que o décimo terceiro</b> 🤣, mais polêmico que uva-passa no arroz de Natal!</b> 
                      E também aquele que ninguém lembra o presente 🎁, mas todo mundo lembra da resenha tradiça! 🍻 </p>

                      <p>Bora lá.. Abaixo está o resultado do sorteio e o doido que você vai presentear em 2025:</p>

                      <p style="font-size: 1.2em; text-align: center; background: #e8f5e9; padding: 12px; border-radius: 8px;">
                        🎉 <b>Você tirou o brother: <span style="color: #1b5e20;">{destinatario}</span>!</b> 🎉
                      </p>

                      <h3 style="color: #2e7d32;">📜 Regras de Ouro hein:</h3>
                      <ul style="list-style-type: none; padding-left: 0;">
                        <li>1️⃣ <b>Por favor, não compartilhe com ninguém!</b> Sem estragar a brincadeira porra! 😅</li>
                        <li>2️⃣ <b>Adm meteu orçamento de R$200,00</b> para o presente (ou o valor que você puder claro!) 💸</li>
                        <li>3️⃣ <b>Não deixe para comprar o presente em cima da hora</b>, tem 25 dias para comprar essa  caralha ..⏰</li>
                        <li>4️⃣ <b>Não vacile!</b> Chegue no horário e com o presente, nada de mãos vazias, os doidos agradecem! 🎁</li>
                        <li>5️⃣ <b>Se atrasar</b>, não vá até Mogi Thiago, avise imediatamente o adm ou o <b>gordão</b>, vulgo Renato Nogueira.. De Behr não tem nada, nem o nome! 📞</li>
                      </ul>

                      <p style="margin-top: 24px;">
                        Boas compras, meu brother! 😎<br>
                        <b>Os Brothers NA Corporation</b> desejam um ótimo fim de ano para você e toda sua família! 🎄🎅
                      </p>

                      <hr style="margin: 24px 0; border: none; border-top: 2px solid #c8e6c9;">

                      <p style="font-size: 1.05em;">
                        <b>Ahh, quase esquecendo...</b><br>
                        O mais importante: o rolê vai acontecer 29 de Novembro das <b>12:00 até 20:00hrs ⏰</b> no <b>Macuco, em Santos</b>!<br>
                        📍 <b>Endereço:</b> Rua Operária, 3<br><br>
                        Leve a família, estão todos convidados. Tmj! Te vejo lá, filhão! <b>Abraço!</b> 🤜🤛
                      </p>

                    </div>
                  </body>
                </html>
                """, subtype='html')

                msg['Subject'] = "Amigo Secreto Brothers NA foi sorteado com sucesso!"
                #msg['Reply-To'] = f"Amigo Secreto Brothers NA 2025 <{remetente_email}>"
                msg['From'] = f"Amigo Secreto Brothers NA 2025 <{remetente_email}>"
                msg['X-Priority'] = '3' 
                msg['To'] = destinatario_email

                server.send_message(msg)
                print(f"E-mail enviado para {remetente} ({destinatario_email})")

                # Aguarda 5 segundos antes de enviar o próximo
                time.sleep(5)

    except smtplib.SMTPException as e:
        print(f"Erro ao enviar e-mail: {e}")

# --- Configurações e Execução ---

# Dicionário de participantes: {Nome: Email}
# Substitua pelos nomes e e-mails reais
participantes = {
    "A1": "a1@hotmail.com",
    "A2": "a2@yahoo.com.br",
    "A3": "a3@icloud.com",

# Suas credenciais de e-mail
# Use uma senha de app para Gmail/Outlook, não sua senha principal
MEU_EMAIL = "xxxyyy@gmail.com"
MINHA_SENHA = "xxx xxx xxx xxx"

# 1. Realiza o sorteio
resultado_sorteio = realizar_sorteio(participantes)
print("Sorteio realizado. Enviando e-mails...")

# 2. Envia os e-mails
enviar_emails(resultado_sorteio, participantes, MEU_EMAIL, MINHA_SENHA)

