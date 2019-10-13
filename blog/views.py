from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#MVT
#MODEL
#VIEW
#TEMPLATE
#Importacion de librerias personales 
from . import models


def listar_noticias(resquest):
	"""
		obtiene las noticias de la base de datos

		Retorna:
			El listado de las noticias
	"""
	#obtiene el listado de todas las noticias
	#De la base de datos y la asigna a la variable
	#noticias
	noticias = models.Noticia.objects.all()
	
	#Retorna todo renderizado para ser leido en el
	#explorador, tiene tres parametros
	#solicitud(resquest), plantilla de datos y datos
	return render(
					resquest, 
					'./noticias/index.html', 
					{'news':noticias}
				)

def ver_noticia(resquest, id_noticia):
	"""
		obtiene una noticia de la base de datos

		parametros:
			id noticia es numerico y hace referencia
			al identificador de la noticia buscada

		retorna:
			la noticia buscada si existe
	"""

	noticia = models.Noticia.objects.get(id=id_noticia)

	return render(
					resquest,
					'./noticias/detalle.html',
					{'noticia':noticia}
				)