from threading import Thread
import time
import json

class Bot(Thread):
    def __init__(self, x, key1, key2, key3, key4):
        Thread.__init__(self)
        self.x = x
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3
        self.key4 = key4
    def run(self):
        print("Key1 do Bot " + str(self.x) + ": " + key1)
        print("Key2 do Bot " + str(self.x) + ": " + key2)
        print("Key3 do Bot " + str(self.x) + ": " + key3)
        print("Key4 do Bot " + str(self.x) + ": " + key4)
        print("\n")

keys_js = {'key1': 'key1', 'key2': 'key2', 'key3': 'key3', 'key4': 'key4'}
with open('keys.json', 'w') as f:
        json.dump(keys_js, f)

keys_block = []

def get_keys():
    with open('keys.json', 'r') as f:
        keys = json.load(f)
    return keys

def put_keys(mode, key1, key2, key3, key4):
    keys_js = {'key1': key1, 'key2': key2, 'key3': key3, 'key4': key4}
    
    if(mode == "overwrite"):
        keys_block.append(keys_js)
        with open('keys.json', 'w') as f:
            json.dump(keys_block, f)
    else:
        with open('keys.json', 'a') as f:
            json.dump(keys_js, f)

q = 1
t = 1

qtd_keys_js = 0
keys_js = get_keys()
qtd_keys_js = len(keys_js)

#Inicia UI

qtd = int(input("Quantidade de bots: "))
exist = input("Usar keys salvas no sistema? [y] ")
if(exist == "y"):
    if(qtd < qtd_keys_js):
        print("O número de keys encontradas é menor do que o solicitado " + str(qtd_keys_js))
        time.sleep(1)
        opt = input("Inserir novas keys? [y] ")
        if(opt == "y"):
            mode = "append"
            while qtd < qtd_keys_js:
                key1 = input("Insira a key1 do bot " + str(q) + ": ")
                key2 = input("Insira a key2 do bot " + str(q) + ": ")
                key3 = input("Insira a key3 do bot " + str(q) + ": ")
                key4 = input("Insira a key4 do bot " + str(q) + ": ")
                f.write('\n')
                put_keys(mode, key1, key2, key3, key4)
        else:
            print("Prosseguindo com a ativação de " + str(qtd_keys_js) + " bots pré registrados ")
            qtd = qtd_keys_js
else:
    print("Prosseguindo com o registro de " + str(qtd) + " novos bots ")
    if(qtd_keys_js > 0):
        opt = input("Deseja sobrescrever as keys anteriores? [y] ")
        if(opt == "y"):
            for x in range(qtd):
                mode = "overwrite"
                key1 = input("Insira a key1 do bot " + str(t) + ": ")
                key2 = input("Insira a key2 do bot " + str(t) + ": ")
                key3 = input("Insira a key3 do bot " + str(t) + ": ")
                key4 = input("Insira a key4 do bot " + str(t) + ": ")
                print('')
                put_keys(mode, key1, key2, key3, key4)
                t += 1
        else:
            mode = "append"
            while qtd < qtd_keys_js:
                key1 = input("Insira a key1 do bot " + str(q) + ": ")
                key2 = input("Insira a key2 do bot " + str(q) + ": ")
                key3 = input("Insira a key3 do bot " + str(q) + ": ")
                key4 = input("Insira a key4 do bot " + str(q) + ": ")
                f.write('\n')
                put_keys(mode, key1, key2, key3, key4)
                q += qtd_keys_js
    else:
        while qtd < qtd_keys_js:
            mode = "append"
            key1 = input("Insira a key1 do bot " + str(q) + ": ")
            key2 = input("Insira a key2 do bot " + str(q) + ": ")
            key3 = input("Insira a key3 do bot " + str(q) + ": ")
            key4 = input("Insira a key4 do bot " + str(q) + ": ")
            f.write('\n')
            put_keys(mode, key1, key2, key3, key4)
            qtd_keys_js += 1
class Make_a_Bot(Thread):
    def __init__(self, i, q):
        Thread.__init__(self)
        self.i = i
        self.q = q
    def run(self):
        print("Preparando bot...")
        #recuperar o json das keys e registrá-las 1 por 1 no bot conforme index q - 1
        key1 = keys_js[self.i]['key1']
        key2 = keys_js[self.i]['key2']
        key3 = keys_js[self.i]['key3']
        key4 = keys_js[self.i]['key4']

        list_class.append(Bot(self.q, key1, key2, key3, key4)) 
        time.sleep(2)
        print("Bot pronto!")
list_class = []
keys_js = get_keys()
i = 0
while q <= qtd:
    mk_bot = Make_a_Bot(i, q)
    mk_bot.start()
    q += 1
    i += 1
list_len = len(list_class)
for w in range(list_len):
    print("Iniciando bots..")
    time.sleep(10)
    list_class[w].start()