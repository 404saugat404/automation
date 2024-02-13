
# from vosk import Model, KaldiRecognizer
# import pyaudio
# import json

# model = Model(r"C:\Users\sauga\Desktop\automation\mj\automation\vosk-model-small-en-in-0.4")
# recognizer = KaldiRecognizer(model, 16000)

# mic = pyaudio.PyAudio()
# stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
# stream.start_stream()

# while True:
#     data = stream.read(4096)
#     if len(data) == 0:
#         break
#     if recognizer.AcceptWaveform(data):
#         result = json.loads(recognizer.Result())
#         text = result["text"]
#         print(text)





# import os
# import subprocess
# from vosk import Model, KaldiRecognizer
# import pyaudio
# import json

# model = Model(r"C:\Users\sauga\Desktop\automation\mj\automation\vosk-model-small-en-in-0.4")
# recognizer = KaldiRecognizer(model, 16000)

# mic = pyaudio.PyAudio()
# stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
# stream.start_stream()

# def listen_vosk():
#     while True:
#         data = stream.read(4096)
#         if len(data) == 0:
#             break
#         if recognizer.AcceptWaveform(data):
#             result = json.loads(recognizer.Result())
#             text = result["text"]
#             return text.lower()

# def create_folder():
#     print('What do you want to name the folder?')
#     folder_name = listen_vosk()
#     path = f'D:\\{folder_name}'

#     if os.path.exists(path):
#         print(f'The folder "{folder_name}" already exists at {path}')
#         print('Please choose another name.')
#         create_folder()
#     else:
#         os.mkdir(path)
#         print(f'Folder "{folder_name}" created successfully at {path}')

# def delete_folder():
#     print('What is the name of the folder you want to delete?')
#     folder_name = listen_vosk()
#     path = f'D:\\{folder_name}'

#     if os.path.exists(path):
#         os.rmdir(path)
#         print(f'Folder "{folder_name}" deleted successfully.')
#     else:
#         print(f'The folder "{folder_name}" does not exist.')

# def open_folder():
#     print('What is the name of the folder you want to open?')
#     folder_name = listen_vosk()
#     path = f'D:\\{folder_name}'

#     if os.path.exists(path):
#         subprocess.Popen(['explorer', path])
#     else:
#         print(f'The folder "{folder_name}" does not exist.')

# if __name__ == "__main__":
#     print("1. Create Folder\n2. Delete Folder\n3. Open Folder")
#     choice = listen_vosk()

#     if choice == 'create a folder':
#         create_folder()
#     elif choice == 'delete' or choice=="deleted" or choice=="dit it":
#         delete_folder()
#     elif choice == 'open':
#         open_folder()
#     else:
#         print('Invalid choice. Please say "create folder", "delete folder", or "open folder".')

import os
import subprocess
import json
import pyaudio
from vosk import Model, KaldiRecognizer

model = Model(r"C:\Users\sauga\Desktop\automation\mj\automation\vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
stream.start_stream()

def listen_vosk():
    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result["text"]
            return text.strip().lower()

def perform_action():
    print("What action would you like to perform?")
    print("1. Shutdown\n2. Logoff\n3. Restart\n4. Create Folder\n5. Delete Folder\n6. Open Folder\n7. Nothing")
    choice = listen_vosk()

    if choice == 'shutdown':
        os.system('shutdown /s /t 20')
        print('Shutting down in 20 seconds...')
    elif choice == 'logoff':
        os.system('shutdown /l /t 20')
        print('Logging off in 20 seconds...')
    elif choice == 'restart':
        os.system('shutdown /r /t 20')
        print('Restarting in 20 seconds...')
    elif choice == 'create folder':
        create_folder()
    elif choice == 'delete folder':
        delete_folder()
    elif choice == 'open folder':
        open_folder()
    elif choice == 'nothing':
        print('Okay, doing nothing.')
    else:
        print('Invalid choice. Please select a valid option.')

def create_folder():
    print('What do you want to name the folder?')
    folder_name = listen_vosk()
    path = f'D:\\{folder_name}'

    if os.path.exists(path):
        print(f'The folder "{folder_name}" already exists at {path}')
        print('Please choose another name.')
        create_folder()
    else:
        os.mkdir(path)
        print(f'Folder "{folder_name}" created successfully at {path}')

def delete_folder():
    print('What is the name of the folder you want to delete?')
    folder_name = listen_vosk()
    path = f'D:\\{folder_name}'

    if os.path.exists(path):
        os.rmdir(path)
        print(f'Folder "{folder_name}" deleted successfully.')
    else:
        print(f'The folder "{folder_name}" does not exist.')

def open_folder():
    print('What is the name of the folder you want to open?')
    folder_name = listen_vosk()
    path = f'D:\\{folder_name}'

    if os.path.exists(path):
        subprocess.Popen(['explorer', path])
    else:
        print(f'The folder "{folder_name}" does not exist.')

if __name__ == "__main__":
    perform_action()
