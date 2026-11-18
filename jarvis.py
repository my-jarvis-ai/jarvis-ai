import datetime

def jarvis():
    hour = datetime.datetime.now().hour

    print("Hello! I am JARVIS.")
    print("Your personal AI assistant.")

    if hour < 12:
        print("Good Morning!")
    elif hour < 17:
        print("Good Afternoon!")
    else:
        print("Good Evening!")

    while True:
        command = input("You: ").lower()

        if "hello" in command:
            print("JARVIS: Hello! How can I help you?")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            print("JARVIS:", time)

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d-%m-%Y")
            print("JARVIS:", date)

        elif "exit" in command:
            print("JARVIS: Goodbye!")
            break

        else:
            print("JARVIS: I am still learning.")

jarvis()
