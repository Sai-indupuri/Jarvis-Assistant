from speech_recognition_module import recognize_speech
from nlp_processing import process_command
from command_handler import handle_command
from tts_response import speak

def main():
    while True:
        command = recognize_speech()
        if command:
            processed_command = process_command(command)
            response = handle_command(processed_command)
            speak(response)

if __name__ == "__main__":
    main()
