seg1=int(input('Por favor, entre com o número de segundos que deseja converter:'))
seg=seg1%60
seg1=seg1//60
minut1=seg1//60
minut=seg1%60
hora=minut1%24
dia=minut1//24
ano=dia//365
ano1=dia%365
print('{} dias, {} horas, {} minutos e {} segundos.'.format(dia,hora,minut,seg))
print(ano,ano1)
