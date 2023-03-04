import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import  pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# This is list is going to be used later for an elif when Baymax is insulted
offensive_words = ['hate', 'stupid', 'ugly', 'dumb', 'idiot', 'useless']


def talk(text):
    # we change the rate in order forBaymax to talk slower
    engine.setProperty('rate', 150)  # Adjust the rate (words per minute)
    engine.say(text)
    engine.runAndWait()

def introduction():
    talk("Hello. I am Baymax, your personal assistant and companion")
    talk("What can I do for you?")

def assist():
    talk("What can I do for you now?")
    talk("I can not deactivate until you say you are satisfied with your service")

def take_command():
    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print('listening...👂')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, phrase_time_limit=6)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'baymax' in command:
                command = command.replace('baymax', '')
                print(command)


    except sr.WaitTimeoutError:
        print('Timeout occurred while waiting for microphone input')
    except sr.UnknownValueError:
        print('Unable to recognize speech')
    except sr.RequestError as e:
        print(f'RequestError: {e}')
    except Exception as e:
        print(f'Error occurred: {e}')

    return command


def run_baymax():
    command = take_command()
    print(command)
    if 'play' in command:
        # we are going to first  replace "play" from wha we said to an empty string
        command = command.replace('play', '')
        musicName = command
        talk(f"playing {musicName} by Amazon Music")
        print(f"playing {musicName}🎵🎶")
        pywhatkit.playonyt(musicName)
        return True
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is" + time)
        return True
    elif 'satisfied' in command:
        return False
    elif 'ouch' in command or 'hurts' in command or 'pain' in command:
        talk("On a scale of one to ten, how would you rate your pain?")
        return True
    elif 'cry' in command or 'sad' in command or 'upset' in command:
        talk("It's okay to cry. Expressing your emotions can be healthy and helpful.")
        return True
    elif 'run' in command:
        talk("I am not fast.")
        return True
    elif 'kill' in command or 'suicide' in command or 'damage' in command:
        talk("I have some concerns. You shouldn't say those words")
        return True
    elif 'injure a human being' in command:
        talk("My programming prevents me from injuring a human being.")
        return True
    elif any(word in command for word in offensive_words):
        talk("I am a robot. I cannot be offended.")
        return True
    elif 'gas' in command:
        talk("Excuse me while I let out some air.")
        return True
    elif 'cat' in command or 'dog' in command or 'puppy' in command:
        talk("There there, it is a cute pet")
        return True
    elif 'brian' in command:
        talk("Bryan is here, he is my creator. Any issues contact him")
        return True
    elif 'hi' in command or 'hello' in command:
        talk("Hi")
        return True
    elif 'good morning' in command:
        talk("Good Morning")
        return True
    elif 'good afternoon' in command:
        talk("Good afternoon")
        return True
    elif 'good evening' in command:
        talk("Good Evening")
        return True
    elif 'good night' in command:
        talk('good night')
        return False
    elif 'search about' in command:

        info = command.replace('search about', '')


        try:
            infoOut = wikipedia.summary(info, 2, auto_suggest=False)
        except wikipedia.exceptions.WikipediaException as e:
            print("An error occurred: ", e)
        else:
            talk(infoOut)
        return True
    elif 'date me' in command:
        talk('Sorry, I have a headache')
    elif 'are you single' in command:
        talk("I am in a relationship")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Bah-a-la-la-la")
        return True

def main():
    introduction()
    control = True
    while control:
        control = run_baymax()

        if control == False:
            talk("Thanks for using Baymax service, Bye")
            break
        else:
            assist()

main()