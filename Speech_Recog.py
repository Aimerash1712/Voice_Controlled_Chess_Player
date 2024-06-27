import speech_recognition as sr


Recog = sr.Recognizer()

def Listen_Speech():
    while(1):
        try:
            with sr.Microphone() as source2:

                Recog.adjust_for_ambient_noise(source2,duration=0.2)

                audio2 = Recog.listen(source2)

                MyText = Recog.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print("couldn't get result")

        except sr.UnknownValueError:
            print("Error Occured")

    return

def write_text_to_file(text, filename):
    try:
        # Open the file in write mode. If the file does not exist, it will be created.
        with open(filename, 'w') as file:
            # Write the text to the file
            file.write(text)
        print(f"Text has been successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

while(1):
    text = Listen_Speech()
    filename = "out.txt"
    write_text_to_file(text,filename)
    print("Text is written")

