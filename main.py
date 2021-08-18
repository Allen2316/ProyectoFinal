import JarvisAI
import re
import pprint
import random
import os

obj = JarvisAI.JarvisAssistant()



def t2s(text):    
    obj.text2speech(text, lang='es')



def inicio() :
    t2s('Bienvenido de nuevo señor')
    while True:        
        res = obj.mic_input(lang = 'es')      
        if re.search('clima|temperatura', res):
            city = res.split(' ')        
            print(f'city len {city[len(city)-1]}')
            weather_res = obj.weather(city=city[len(city)-1])
            print(weather_res)
            t2s(weather_res)

        if re.search('noticias', res):
            news_res = obj.news()
            pprint.pprint(news_res)
            t2s(f"He encontrado noticias de {len(news_res)}. Puedes leerlo. Déjame contarte los primeros 2 de ellos")
            t2s(news_res)
            t2s(news_res)

        if re.search('hablame de|háblame de', res):
            topic = res.split(maxsplit=3)
            print(f'topiccccc {topic}')
            wiki_res = obj.tell_me(topic)
            print(wiki_res)
            t2s(wiki_res)

        if re.search('fecha', res):
            date = obj.tell_me_date()
            print(date)
            print(t2s(date))

        if re.search('hora', res):
            time = obj.tell_me_time()
            print(time)
            t2s(time)

        if re.search('abrir|abre|abras', res):
            domain = res.split(' ')
            print(domain)
            open_result = obj.website_opener(domain[len(domain)-1])        
            print(open_result)
            t2s('Abriendo ' + domain[len(domain)-1])

        if re.search('ejecuta|ejecutar|abriendo', res):
            dict_app = {
                'chrome': 'C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe',
                'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe'
            }
            app = res.split(' ')
            path = dict_app.get(app[len(app)-1])
            if path is None:
                t2s('Ruta de la aplicación no encontrada')
                print('Ruta de la aplicación no encontrada')
            else:
                t2s('Abriendo ' + app[len(app)-1])
                obj.launch_any_app(path_of_app=path)

        if re.search('hola', res):
            print('Hola')
            t2s('Hola')

        if re.search('cómo estás|como estas', res):
            li = ['bien', 'normal', 'genial']
            response = random.choice(li)
            print(f"Estoy {response}")
            t2s(f"Estoy {response}")

        if re.search('tu nombre|eres', res):
            print("Mi nombre es Jarvis, soy tu asistente personal.")
            t2s("Mi nombre es Jarvis, soy tu asistente personal.")

        if re.search('gracias|muchas gracias', res):        
            print("Estoy para ayudarle")
            t2s("Estoy para ayudarle")

        if re.search('adios|adiós|hasta mañana|chao', res):
            sh = obj.shutdown()
            print(sh)
            t2s(sh)


        if re.search('puedes hacer', res):
            li_commands = {
                "abrir sitios web": "Ejemplo: 'abrir youtube.com",
                "tiempo": "Ejemplo: '¿qué hora es?'",
                "fecha": "Ejemplo: '¿qué fecha es?'",
                "abrir aplicaciones": "Ejemplo: 'lanzar Chrome'",
                "contarte acerca de algo": "Ejemplo: 'cuéntame sobre la India'",
                "clima": "Ejemplo: '¿qué clima / temperatura hay en Loja?'",
                "noticias": "Ejemplo: 'noticias de hoy'",
            }
            ans = """Puedo hacer muchas cosas, por ejemplo, puedes preguntarme la hora, la fecha, el clima de tu ciudad,
            Puedo abrir sitios web para ti, lanzar aplicaciones y más. Ver la lista de comandos-"""
            print(ans)
            pprint.pprint(li_commands)
            t2s(ans)



if __name__ == "__main__":
    if not os.path.exists("config/config.ini"):
        res = obj.setup()
        if res:
            print("Configracion guardada. Reinicie su asistente")
    else:
        inicio()