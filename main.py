# main.py
import asyncio
from core.speech import speak
from core.personality import load_personality
from core.brain import generate_response

def main():
    #Função principal que inicia o assistente Niko.
    #Mostra a saudação, espera o input do usuário e responde de forma interativa.

    # Carrega o perfil do Niko
    personality = load_personality()

    # Exibe a frase de boas-vindas
    greeting = personality['default_phrases']['greeting']
    print(f"Niko: {greeting}")
    asyncio.run(speak(greeting))

    # Loop principal de conversa
    while True:
        user_input = input("Você: ")

        # Se o usuário quiser encerrar
        if user_input.lower() in ["sair", "exit", "tchau"]:
            goodbye = personality['default_phrases']['goodbye']
            print(f"Niko: {goodbye}")
            asyncio.run(speak(goodbye))
            break

        # Gera resposta e exibe
        response = generate_response(user_input)
        print(f"Niko: {response}")
        asyncio.run(speak(response))

# Verifica se este é o arquivo principal sendo executado
if __name__ == "__main__":
    main()
