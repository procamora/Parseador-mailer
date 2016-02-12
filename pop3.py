#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib

from email.Parser import Parser

m = poplib.POP3_SSL('pop.gmail.com',995)				# Se establece conexion con el servidor pop de gmail
m.user('USERNAME@gmail.com')
m.pass_('PASSWORD')

numero = len(m.list()[1])								# Se obtiene el numero de mensajes pendientes
for i in range (numero):								# se hace un bucle para cada mensaje
	lista = []   											# creo una lista
	print("Mensaje numero "+str(i+1))
	
	response, headerLines, bytes = m.retr(i+1)			# Se lee el mensaje
	mensaje='\n'.join(headerLines)						# Se mete todo el mensaje en un unico string
	p = Parser()										# Se parsea el mensaje
	email = p.parsestr(mensaje)							
	'''HACER COMPROBACION DE QUE EL CORREO PERTENECE A EMPRESA Y QUE EL ASUNTO ES ALGO'''
	#print "From: "+email["From"]						# Se sacan por pantalla los campos from, to y subject
	#print "To: "+email["To"]
	#print "Subject: "+email["Subject"]
	
	for part in email.get_payload():					# bucle para cada parte del mensaje
		tipo =  part.get_content_type()					# Se mira el mime type de la parte
		if ("text/plain" == tipo):						# Si es texto plano, se saca por pantalla
			lista.append(part.get_payload(decode=True))



	Texto = lista[0].split('\n')						# parto el asunto por los \n
	print('Nombre   : %s' %(Texto[0]))
	print('Direccion: %s' %(Texto[1]))
	print('Velocidad: %s' %(Texto[2]))
	print('Mac 1    : %s' %(Texto[3]))
	print('Mac 2    : %s' %(Texto[4]))
	print('Telefono : %s' %(Texto[5]))
	print("--------------------")

m.quit()												# Cierre de la conexion






