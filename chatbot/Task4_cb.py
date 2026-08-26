def chatbot(): # Define a simple chatbot function
    Bot = ["Hi!", 
           "I'm fine, thanks! And you?",
           "That's great!",
           "Bye! See you later!",
           "I'm a simple chatbot!",
           "{Simple definition of python} Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace.",
           "{Simple definition of AI} Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.",
           "{Simple definition of security} Computer security, also known as cybersecurity or IT security, is the protection of computer systems and networks from digital threats.",
           "Sorry, I didn't understand that."]
    
    print("==> Welcome to the ChatBot! <==")
    print("Type 'exit' to end the chat.")
    
    Chat_On = True
    Chat_Off = False
    while Chat_On:
        user_input = input("You: ").strip().lower() # Get user input and convert to lowercase for uniformity
        
        if user_input == "exit": # Exit condition
            print("Bot:", Bot[3])
            Chat_On = Chat_Off
        # Check for various greetings and questions
        elif any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
            print("Bot:", Bot[0])
        elif any(question_0 in user_input for question_0 in ["how are", "how's it"]):
            print("Bot:", Bot[1])
        elif any(response_0 in user_input for response_0 in ["fine", "good", "great"]):
            print("Bot:", Bot[2])
        elif any(question_1 in user_input for question_1 in ["what are you", "who are you"]):
            print("Bot:", Bot[4])
        elif any(question_2 in user_input for question_2 in ["define python", "what is python"]):
            print("Bot:", Bot[5])
        elif any(question_3 in user_input for question_3 in ["define ai", "what is ai"]):
            print("Bot:", Bot[6])
        elif any(question_4 in user_input for question_4 in ["define security", "what is security"]):
            print("Bot:", Bot[7])
        else:
            print("Bot:", Bot[8]) # Default response for unrecognized input

# Run the chatbot
chatbot()       