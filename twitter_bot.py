#para correrlo: python twitter_bot.py
import config
import tweepy
import time
from random import randint

print("\n*************************")
print("       TWITTER BOT       ")
print("*************************\n")

#Llaves en config.py

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

NOMBRE_ARCHIVO = "ultima_id.txt"
respuesta_bot =  "🖥Respuesta generada por un bot creado por Santiago Yeomans🖥 \n\n 🖥Answer generated by a bot created by Santiago Yeomans🖥 \n\nfor more information visit : https://github.com/SYM1000"
respuestas = ["Hola!", 
        "Asombroso!", 
        "Gran comentario", 
        "Excelente respuesta",
        "Gracias por mencionar a Santiago Yeomans",
        "WOW!", 
        "Hoy es un gran día",
        "Buen dia", 
        "Que tal, amigo",
        "Soy un bot", 
        "Este es un bot",
        "Saludos!"]


def regresar_ultimo_id(archivo):
    leer_archivo = open(archivo, "r")
    ultimo_id = int(leer_archivo.read().strip())
    leer_archivo.close()
    return ultimo_id

def almacenar_ultimo_id(ultimo_id, archivo):
    escribir = open(archivo, "w")
    escribir.write(str(ultimo_id))
    escribir.close()
    return

#NOTA: 1112140386171011072
#NOTA Segunda prueba del bot: 1133902620618371077
#NOTA ID final: 1133980480678838272

def mostrar_menciones():
    print("Revisando Tweets\n")
    ultimo_id = regresar_ultimo_id(NOMBRE_ARCHIVO)
    menciones = api.mentions_timeline(
                        ultimo_id,
                        tweet_mode = "extended")
                    

    for mencion in reversed(menciones):
        print(str(mencion.id) +  " - " + mencion.full_text)
        ultimo_id = mencion.id
        almacenar_ultimo_id(ultimo_id, NOMBRE_ARCHIVO)



def responder_tweets():
    print("Revisando Tweets\n")
    ultimo_id = regresar_ultimo_id(NOMBRE_ARCHIVO)
    menciones = api.mentions_timeline(
                        ultimo_id,
                        tweet_mode = "extended")
                    

    for mencion in reversed(menciones):
        print(str(mencion.id) +  " - " + mencion.full_text)
        ultimo_id = mencion.id
        almacenar_ultimo_id(ultimo_id, NOMBRE_ARCHIVO)
        
        if "#bot" in mencion.full_text.lower(): 
            api.update_status("@" + mencion.user.screen_name + " " + respuesta_bot, mencion.id)
            print("se respondio a un tweet con el #bot")

        elif (mencion.user.screen_name == "anamolina1900"):
            api.update_status("@" + mencion.user.screen_name + " ❤", mencion.id)
            print("se respondio a un tweet de Ana B")
        
        elif (mencion.user.screen_name == "angela7744"):
            api.update_status("@" + mencion.user.screen_name + " Te amo, Ángela ❤", mencion.id)
            print("se respondio a un tweet de Angela <3")

        else:
            numero = randint(0,11)
            respuesta = respuestas[numero]
            api.update_status("@" + mencion.user.screen_name + " " + respuesta +  "\n\n Este mensaje fue generado por un bot creado por Santiago Yeomans \n\n\n para mas información visitia: https://github.com/SYM1000", mencion.id)
            print("Se respondio al tweet de " + mencion.user.screen_name)

def imprimir_timeline():
    for tweet in api.home_timeline():
        print (tweet.user.screen_name)


#Obtener id de un usuario: http://gettwitterid.com/

#Seguir a un usuario: api.create_friendship(user_id)
#Para retweetear: mencion.retweet()
#Acceder a los tweets en la linea del tiempo:   for tweet in api.home_timeline():
                                                    #print tweet.text

#Loop infinito para que siempre se este ejecutando el programa
while True:
    responder_tweets()
    #imprimir_timeline()
    #mostrar_menciones()
    time.sleep(10)
