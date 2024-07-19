
import sys
import pyttsx3
#pip install pyttsx3

def main():
    # Inicializar o mecanismo de conversão de texto para fala
    engine = pyttsx3.init()

    print("Please enter the text (press Ctrl+D to end input):")
    
    # Ler o texto da entrada padrão até EOF
    input_text = sys.stdin.read()

    # Reproduzir o texto lido
    engine.say(input_text)
    engine.runAndWait()

if __name__ == "__main__":
    main()
