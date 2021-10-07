import re
import random


def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\s\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Agregar las respuestas Array
    Daniel=["No man!","Quien es tu perra?", "Vete alv me gano la casa", "No le hago a eso", "yo no culeo gatods", "No me dormi man", "Zzzzz...."]
    Rene=["Sho solo soy el practicante!","Quien quiere jugar cartitas?"]
    Daniel=["Aaron me das un besito?","No man!","Quien es tu perra?", "Vete alv me gano la casa", "No le hago a eso", "yo no culeo gatos", "No me dormi", "Zzzzz...."]
    David=["Necesito un buen rifle","Necesito el grande, el chico no me llena (escudo)","Quiero ver gotas", "Ya me enbetune el pantalón"]
    Daniel=["este man","No man!","Quien es tu perra?", "Vete alv me gano la casa", "No le hago a eso", "yo no culeo gatos", "No me dormi", "Zzzzz...."]
    Shecho=["Ya weey!!!", "Estas bien pendejo Daniel", "Su ptm ya me quemaron", "Sacalas VL!", "Me trague mi propio pedo alv"]
    VL=["Estoy tomando", "Pssst (ruido de cheve)","Se me chingo la tele", "Deje cansado al shecho"]
    Aaron=["Ya me culie al Daniel","Daniel a mi me dijeron que culeas gatos!", "Me acabo de fumar un gallito"]
    Dani=["Me dio alergia solo de imaginarlo","Que lo haga el practicante", "Ya me dio alergia"]
    Line=["Como chinga oiga", "Aqui no vive", "Miauuu... a te la creiste", "Para que le hablas si eres alergico pinche Dani prro"]
    Mega=["Lo deje a un tiro", "Pinche daniel esta mas turbado que nunca"]
    response_list = [
        process_message(message, ['hello there'], 'General Kenobi!'),
        process_message(message, ['reneee','Reneee'], random.choice(Rene)),
        process_message(message, ['danielll','Danielll'],random.choice(Daniel)),
        process_message(message, ['Daviddd','daviddd'], random.choice(David)),
        process_message(message, ['shechooo', 'Shechooo'], random.choice(Shecho)),
        process_message(message, ['VL', 'viejo loco', 'Viejo loco'], random.choice(VL)),
        process_message(message, ['Aronnn', 'aronnn'], random.choice(Aaron)),
        process_message(message, ['Daniii', 'daniii'], random.choice(Dani)),
        process_message(message, ['Megaaa', 'megaaa'], random.choice(Mega)),

        process_message(message, ['lag'], 'Alguien ha visto al Daniel?'),
        process_message(message, ['bocina'], 'La pinche bocina es mia y mis huevotes!'),
        process_message(message, ['Fortniteee', 'fortnite','juego?'], 'ya se murio el Daniel!'),
        process_message(message, ['Lineee', 'lineee', 'paquira'], random.choice(Line)),
        process_message(message, ['no man', 'No man'], 'Alguien a visto al Danielll?'),
        process_message(message, ['oxxo', 'Oxxo'], 'Alguien a visto al Rene?'),
        process_message(message, ['cumpleañero', 'Cumpleañero'], 'Alguien se va a sentar a comer el pastel!'),
        #process_message(message, ['hora?','Hora?', 'que horas son?','Que hora son?'], datetime.now().strftime('%H:%M:%S')),
        #process_message(message, ['que dia es hoy?','Que dia es hoy?', 'a que estamos??','A que estamos?'], datetime.now().strftime('%d/%m/%Y')),
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