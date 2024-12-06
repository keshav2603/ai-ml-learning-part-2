import pyttsx3

engine = pyttsx3.init()
l=["keshav", "avnish", "abhinav", "aryan", "ansh"]

engine.setProperty('rate', 150)
def give_shout_out(name_list):
    for name in name_list:
        engine.say(f"shout out to {name}")
        engine.runAndWait()


give_shout_out(l)