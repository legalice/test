#imports
from time import sleep
from json import loads
from requests import get

#declaracao de variaveis
paises = {}
endereco_api = "http://ip-api.com/json/"

#obtendo os ips
file = open('/home/rafael/Downloads/ips.txt')
save = open('/home/rafael/Downloads/salveip.txt','w')
ips = []
lista_ip = file.read().replace('\'','').split('\n')
file.close()

#acessando a API
for ip in lista_ip:
	requisicao = get(endereco_api+ip)
	retorno = loads(requisicao.text)['country']
	if(requisicao.status_code == 200):
		print "O ip "+ip+" pertence ao pais "+retorno #comente para modo nao verboso
                if(retorno == 'Brazil'):
			ips.append(ip)
		if(paises.has_key(retorno)):
			paises[retorno] += 1
		else:
			paises.update({retorno:1})
	sleep(60/150) #garante no maximo 150 execucoes por minuto

#contabilizando os paises
print "Exibindo quantidade de ips por pais"
for p in paises:
	print(p+" : "+paises[p])
save.writelines(ips)
save.close()

