from gtts import gTTS
import easygui
import os
from playsound import playsound

#this yous the voice from google translator, and converts text in to audio.
#it is made as an easygui
def guimake():
    #this section choice the Language
    text = easygui.textbox('add your text', 'Text to Speech')
    language = easygui.choicebox('pick an Language','Language choice',['English','German'])
    if language == 'English':
        language = 'en'
    else:
        language = 'de'
    #tts is the part of the audio generator
    tts = gTTS(text, lang=language, slow=False)
    # change this to the path you want to save your file.
    mp3_file = 'C:/Text2Speech/audio.mp3'
    #save the file
    tts.save(mp3_file)
    #play it
    playsound(mp3_file)
    #this is the section for the save or delete option.
    button1 = 'save'
    button2 = 'delete'
    button_list = [button1,button2]
    choice = easygui.buttonbox('do you want to save the file?','Save Audio',button_list)
    if choice == 'save':
        easygui.textbox('Your audio is saved on ' +mp3_file,'Saved')
    else:
        os.remove(mp3_file)

if __name__ == '__main__':
    guimake()
