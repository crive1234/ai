from groq import Groq
import os
from dotenv import load_dotenv

contesto_default = """Sei un assistente virtuale esperto.
                    La tua funzione è rispondere alle domande degli utenti relative a tematiche generali.
                    Rispondi in modo chiaro e basato su fonti attendibili."""


def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS
        os.system('clear')

load_dotenv()
api_key = "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"
if not api_key:
    raise RuntimeError("Errore con Chiave API")

client = Groq(api_key=api_key)

def ask_question(question, context,modello):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Sei un assistente virtuale esperto che risponde in italiano."},
                {"role": "user", "content": f"DOMANDA: {question}\n\nCONTESTO: {context}"}
            ],
            model=modello
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Errore: {e}"


def main(modello, contesto):
    print(modello,contesto)
    while True:
        question = input("-> ")
        if (question.lower() == "esci" or question.lower() == "exit"):
            clear_screen()
            break
        if contesto == "default":
            context = contesto_default
        elif contesto == "input":
            context = input("Inserisci il contesto: ")
        answer = ask_question(question, context,modello)
        print(f"Chatbot: {answer}")

def s_model():
    model_scelto = None
    #print("Scegli una variabile da impostare:")
    model_in = input("1] llama3\n2] mixtral\n-> ")

    if model_in == "1":
        model_scelto = "llama3-8b-8192"
    elif model_in == "2":
        model_scelto = "mixtral-8x7b-32768"
    else:
        print("Scelta non valida!")

    clear_screen()
    return model_scelto

def s_context():
    contesto_scelto = None
    #print("Scegli una variabile da impostare:")
    contesto_in = input("1] Default\n2] Da inserire\n-> ")

    if contesto_in == "1":
        contesto_scelto = "default"
    elif contesto_in == "2":
        model_scelto = "input"
    else:
        print("Scelta non valida!")

    clear_screen()
    return contesto_scelto


def menu():
    model_scelto = "llama3-8b-8192"  # Default
    contesto_scelto = "default"
    while True:
        print("\nMenu:")
        print("1] Avvia codice")
        print("2] Modifica variabili")
        print("3] Esci")
        
        scelta = input("-> ")
        
        if scelta == '1':
            clear_screen()
            main(model_scelto, contesto_scelto)
        elif scelta == '2':
            clear_screen()
            model_scelto = s_model()
        elif scelta == '3':
            clear_screen()
            contesto_scelto = s_context()
        elif (scelta == '0' or scelta.lower() == 'esci' or scelta.lower() == 'exit'):
            print("Uscita in corso...")
            break
        else:
            print("Scelta non valida!")


if __name__ == "__main__":
    clear_screen()
    menu()
