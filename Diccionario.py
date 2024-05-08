meme_dict ={
           'CRINGE' : 'Algo exepcionalmente raro o embarazoso',
           'LOL': 'Una respuesta común a algo gracioso',
           'CREEPY': 'Aterrador o siniestro',
           'GTG': 'Es un slang común cuando estas chateando con otra persona y  te tienes que ir',
           'NOOB': 'Se utiliza para referirse a una persona que es nuevo en una profesion o lugar',
           'ASAP': 'Se utiliza cuando necesitas algo urgente,',
           'F ': ' Se utiliza para mostrar sus respetos a una persona muerta o cuando estan molestando y les ganaron',
           }

word = input ('Escribe una palabra que no entiendas (con mayúsculas):')

if word in meme_dict.key():
    print(word,':', meme_dict[word])
else:
    print ('esa palabra no está en el diccionario, revisa si has escritó bien')
