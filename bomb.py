import amino,time, threading
####Переменные####
Login = input('Логин:')
Pass = input('Пароль:')
Chat = input('Ссылка на чат:')
client = amino.Client()
client.login(email=Login, password=Pass)
subclient = amino.SubClient(comId="202247760", profile=client.profile)
oldMessages = []
chatid = client.get_from_code(Chat).objectId
print(chatid)
msg3 = 'godisdead!'*40000
def anonsay():
    global msg
    while True:
        mesg = input('>')
        if mesg == 'Tactical nuke 1':
            threading.Thread(target=lox).start()
        elif mesg== 'ATOM NUKE':
            threading.Thread(target=bbbb).start()
        else:
            subclient.send_message(chatid, message=mesg, messageType=100)
def moment():
    subclient.send_message(chatid, message=msg, messageType=100)
    subclient.send_message(chatid, message=msg, messageType=100)
    subclient.send_message(chatid, message=msg, messageType=100)
def lox():
    subclient.send_message(chatid, 'TACTICAL NUKE INCOMING', messageType=100)
    subclient.send_message(chatid, 'Three.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'Two.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'One.', messageType=100)
    subclient.send_message(chatid, message=msg3, messageType=100)
    msg = 'kaboom-'
def bomb():
    while True:
        subclient.send_message(chatid, message=msg3, messageType=100)
def bbbb():
    subclient.send_message(chatid, 'NUCLEAR BOMB INCOMING', messageType=100)
    subclient.send_message(chatid, 'Ten.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'Nine.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'Eight.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'Seven.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'Six.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'Five.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'Four.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'Three.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'Two.', messageType=100)
    time.sleep(0.5)
    subclient.send_message(chatid, 'One.', messageType=100)
    for i in range(10):
        threading.Thread(target=bomb).start()

if __name__ == '__main__':
    anonsay()