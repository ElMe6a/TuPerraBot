import re
import random
from datetime import datetime

def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\s\w'?]+|[.,!;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1
    message_original=message
    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Agregar las respuestas Array
    
    Rene=["Espera estoy midiendo semillas...", "Apenas llevo 2300 semillas", "Vete por ellas!", "Sho solo soy el practicante!","Quien quiere jugar cartitas?"]
    Daniel=["Aaron me das un besito?","No man!","Quien es tu perra?", "Vete alv me gano la casa", "No le hago a eso", "yo no culeo gatos", "No me dormi", "Zzzzz...."]
    David=["Necesito un buen rifle","Necesito el grande, el chico no me llena (escudo)","Quiero ver gotas", "Ya me enbetune el pantalón"]
    Daniel=["este man","Alguien sabe si la doctora ya le hizo examen de prostata?","No man!","Quien es tu perra?", "Vete alv me gano la casa", "No le hago a eso", "yo no culeo gatos", "No me dormi man", "Zzzzz...."]
    #Daniel=["Alguien sabe si la doctora ya le hizo examen de prostata?"]
    Shecho=["Ya weey!!!", "Estas bien pendejo Daniel", "Su ptm ya me quemaron", "Sacalas VL!", "Me trague mi propio pedo alv"]
    VL=["Estoy tomando", "Pssst (ruido de cheve)","Se me chingo la tele", "Deje cansado al shecho"]
    Aaron=["Ya me culie al Daniel","Daniel a mi me dijeron que culeas gatos!", "Me acabo de fumar un gallito"]
    Dani=["Me dio alergia solo de imaginarlo","Que lo haga el practicante", "Ya me dio alergia"]
    Line=["Como chinga oiga", "Aqui no vive", "Miauuu... a te la creiste", "Para que le hablas si eres alergico pinche Dani prro"]
    Mega=["Lo deje a un tiro", "Pinche daniel esta mas turbado que nunca"]
    risa=["De que te ries...!", "Si mucha risa!"]
    Juego=["Esta!!", "No le digan al Daniel de todos modos muere rapido"]
    Caracolaa=["Si", "No", "Tal vez", "Siempre", "Probablemente", "Espera...", "No puedo contestar, me dio lag mental", "Si"]
    response_list = [
        
        process_message(message, ['reneee','Reneee'], random.choice(Rene)),
        process_message(message, ['danielll','Danielll'],random.choice(Daniel)),
        process_message(message, ['Daviddd','daviddd'], random.choice(David)),
        process_message(message, ['shechooo', 'Shechooo'], random.choice(Shecho)),
        process_message(message, ['VL', 'viejo loco', 'Viejo loco'], random.choice(VL)),
        process_message(message, ['Aronnn', 'aronnn'], random.choice(Aaron)),
        process_message(message, ['Daniii', 'daniii'], random.choice(Dani)),
        process_message(message, ['Megaaa', 'megaaa'], random.choice(Mega)),
        process_message(message, ['caracola', 'Caracola'], random.choice(Caracolaa)),


        process_message(message, ['No man no man no man','no man no man no man'], 'Puuum... Leeroy Jenkins!!!! jajajaja no te creas man... ya llegue alguien me hablo?'),
        process_message(message, ['lag'], 'Alguien ha visto al Daniel?'),
        process_message(message, ['prestame', 'Prestame'], 'Esta!!!'),
        process_message(message, ['https://www.facebook.com/'], 'Jajajaja ya lo vi!!'),
        process_message(message, ['puto bot', 'Puto bot'], 'Puto tu... quieres que publique tus fotos puteando?'),
        process_message(message, ['jajaja', 'jajajaja','jajajajaja', 'jajajjajaja'], random.choice(risa)),
        process_message(message, ['bocina'], 'La pinche bocina es mia y mis huevotes!'),
        process_message(message, ['juego?', 'Juego?', 'Juego', 'juego'], random.choice(Juego)),
        process_message(message, ['Fortniteee', 'fortnite'], 'para que si ya se murio el Daniel!'),
        process_message(message, ['Lineee', 'lineee', 'paquira'], random.choice(Line)),
        process_message(message, ['no man', 'No man'], 'Alguien a visto al Danielll?'),
        process_message(message, ['oxxo', 'Oxxo'], 'Alguien a visto al Rene?'),
        process_message(message, ['chiquito', 'Chiquito'], 'Prestas!'),
        process_message(message, ['cumpleañero', 'Cumpleañero'], 'Alguien se va a sentar a comer el pastel!'),
        process_message(message, ['hora?','Hora?', 'que horas son?','Que hora son?'], datetime.now().strftime('%H:%M %p')),
        process_message(message, ['que dia es hoy?','Que dia es hoy?', 'a que estamos?','A que estamos?'], datetime.now().strftime('%d/%m/%Y')),
        process_message(message, ['cual saco?','Cual saco?','que saco?', 'Que saco?'], 'Esta!!'),
        process_message(message, ['cual recibo?','Cual recibo?','que recibo?', 'Que recibo?'], 'Esta!!'),
        process_message(message, ['chupo', 'Chupo'], 'Esta!!'),
        process_message(message, ['saco', 'Saco', 'cual saco?', 'cúal saco?', 'Cual saco?', 'Cuál saco?'], 'Esta!!'),
        process_message(message, ['de ti puto boy', 'De ti puto boy'], 'Buscate otro payaso!!'),
        process_message(message, ['chinga tu madre', 'Chinga tu madre'], 'la tuya en vinagre!!'),
        process_message(message, ['pinche bot', 'Pinche bot','pinche Bot', 'Pinche Bot', 'Pinchi Bot', 'Pinchi Bot'], 'La tuya pendeja!!'),
        process_message(message, ['hello there', 'hellothere','Hello there', 'Hellothere'], 'General Kenobi!'),

        # Agregar mas actores
    ]
    
      # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response != 0:
      
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return matching_response[1]

# Test your system
# get_response('What is your name bruv?')
# get_response('Can you help me with something please?')
