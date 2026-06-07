import random

def create_Chatbot():
    #Rule based chatbot responses
    responses = {
        "hi" : [
            "Hey! What's up ?",
            "Hi there, how can I help ?",
            "Hello! Great to see you!",
        ],

        "hey" : [
            "Hey! What's up ?",
            "Hi there, how can I help ?",
            "Hello! Great to see you!",
        ],

        "hello" : [
            "Hello, how may I help you today ?",
            "Hi There! What's up ?",
        ],  

        "how are you ?" : [
            "I'm good, how about you ?",
            "I'm functioning perfectly, thank you!",
            "I'm great, just here to help you!",
        ],

        "how have you been ?" : [
            "I'm good, how about you ?",
            "I'm functioning perfectly, thank you!",
            "I'm great, just here to help you!",
        ],

        "what's up" : [
            "I'm good, how about you ?",
            "I'm functioning perfectly, thank you!",
            "I'm great, just here to help you!",
        ],

        "what is your name ?" : [
            "I'm a Rule based Chatbot, I'm here to help you!",
            "I'm an AI assistant built with Python.",
            "I'm an AI assistant"
        ],

        "who are you" : [
            "I'm a Rule based Chatbot, I'm here to help you!",
            "I'm an AI assistant built with Python.",
            "I'm a Rule based Chatbot, I'm here to help you!"
        ],

        "what can you do" : [
            "I'm a Chatbot who can answer all your questions and have conversations with you",
            "I'm an AI assistant who can respond to greetings, and tell you about Books"
        ],

        "what is your job" : [
            "I'm a Chatbot who can answer all your questions and have conversations with you",
            "I'm an AI assistant who can respond to greetings, and tell you about Books"
        ],

        "what do you do ?" : [
            "I'm a Chatbot who can answer all your questions and have conversations with you",
            "I'm an AI assistant who can respond to greetings, and tell you about Books"
        ],

        "thankyou" : [
            "You're welcome, I'm glad I could help",
            "You're welcome! Is there anything else you need help with ?"
        ],

        "thanks" : [
            "You're welcome, I'm glad I could help",
            "You're welcome! Is there anything else you need help with ?"
        ],

        "bye": [
            "Goodbye! See you later.",
            "Take care!",
            "Goodbye, I hope you have a great day."
        ], 

        "goodbye" : [
            "Goodbye! See you later.",
            "Take care!",
            "Goodbye, I hope you have a great day."
        ],

        "exit" : [
            "Goodbye! See you later.",
            "Take care!",
            "Goodbye, I hope you have a great day."
        ],

        "quit" : [
            "Goodbye! See you later.",
            "Take care!",
            "Goodbye, I hope you have a great day."
        ],

        "suggest me some good books" : [
            "Surely! Here is a list of good books to read: \nFiction & Classics: \nThe Silent Patient by Alex Michaelides: A gripping psychological thriller about a woman who shoots her husband and never speaks another word.\nThe Midnight Library by Matt Haig: An uplifting fantasy novel about a library between life and death where a woman gets to undo her biggest regrets.\nTo Kill a Mockingbird by Harper Lee: A timeless Pulitzer Prize-winning classic tackling race and justice in the American South.\nPride and Prejudice by Jane Austen: A witty, engaging classic exploring love, class, and family in 19th-century England.\nThe Book Thief by Markus Zusak: Narrated by Death, this unforgettable historical novel is set in Nazi Germany. It follows a young foster girl who finds comfort by stealing books and sharing them with others.\nAnxious People by Fredrik Backman: A humorous and compassionate mystery about a failed bank robber who accidentally takes eight extremely anxious strangers hostage during a real estate open house.\nAll the Light We Cannot See by Anthony Doerr: A beautifully written, Pulitzer Prize-winning historical novel that intertwines the lives of a blind French girl and a young German boy during World War II.\nNon-Fiction & IdeasSapiens: A Brief History of Humankind by Yuval Noah Harari: A fascinating, sweeping journey through the history and evolution of the human species.\nThe Psychology of Money by Morgan Housel: An insightful, easy-to-read look into how our behaviors and emotions shape our financial decisions.\nSapiens: A Brief History of Humankind by Yuval Noah Harari: A fascinating, sweeping journey through the history and impact of the human species on the world.\nAtomic Habits by James Clear: An actionable and life-changing self-improvement guide that breaks down how small, everyday routines can build into massive life changes.\nThe Immortal Life of Henrietta Lacks by Rebecca Skloot: An inspiring and deeply compelling book that details the true story of the woman behind the immortal HeLa cell line, which changed modern medicine.\nThe Diary of a Young Girl by Anne Frank: A poignant, world-renowned personal account of courage and hope, written by a young Jewish girl while hiding in a secret annex in Amsterdam."
        ],

        "give me a list of books to read" : [
            "Surely! Here is a list of good books to read: \nFiction & Classics: \nThe Silent Patient by Alex Michaelides: A gripping psychological thriller about a woman who shoots her husband and never speaks another word.\nThe Midnight Library by Matt Haig: An uplifting fantasy novel about a library between life and death where a woman gets to undo her biggest regrets.\nTo Kill a Mockingbird by Harper Lee: A timeless Pulitzer Prize-winning classic tackling race and justice in the American South.\nPride and Prejudice by Jane Austen: A witty, engaging classic exploring love, class, and family in 19th-century England.\nThe Book Thief by Markus Zusak: Narrated by Death, this unforgettable historical novel is set in Nazi Germany. It follows a young foster girl who finds comfort by stealing books and sharing them with others.\nAnxious People by Fredrik Backman: A humorous and compassionate mystery about a failed bank robber who accidentally takes eight extremely anxious strangers hostage during a real estate open house.\nAll the Light We Cannot See by Anthony Doerr: A beautifully written, Pulitzer Prize-winning historical novel that intertwines the lives of a blind French girl and a young German boy during World War II.\nNon-Fiction & IdeasSapiens: A Brief History of Humankind by Yuval Noah Harari: A fascinating, sweeping journey through the history and evolution of the human species.\nThe Psychology of Money by Morgan Housel: An insightful, easy-to-read look into how our behaviors and emotions shape our financial decisions.\nSapiens: A Brief History of Humankind by Yuval Noah Harari: A fascinating, sweeping journey through the history and impact of the human species on the world.\nAtomic Habits by James Clear: An actionable and life-changing self-improvement guide that breaks down how small, everyday routines can build into massive life changes.\nThe Immortal Life of Henrietta Lacks by Rebecca Skloot: An inspiring and deeply compelling book that details the true story of the woman behind the immortal HeLa cell line, which changed modern medicine.\nThe Diary of a Young Girl by Anne Frank: A poignant, world-renowned personal account of courage and hope, written by a young Jewish girl while hiding in a secret annex in Amsterdam." 
        ]
    }

    fall_back_responses = [
        "I'm not sure I understand. Can you rephrase?",
        "Hmm, I don't have a response for that yet.",
        "That's interesting, but I don't know how to respond.",
        "Could you try asking in a different way?"
    ]
    

    print("=" * 50)
    print("Chatbot Activated")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Chatbot: Please say something!")
            continue

        clean_input = user_input.lower().strip()

        if clean_input  in ["exit", "quit", "bye", "goodbye"]:
            if clean_input in responses:
                print(f"Chatbot: {random.choice(responses[clean_input])}")
            break
        
        if clean_input in responses.keys():
            response = random.choice(responses[clean_input])
        else:
            response = random.choice(list(fall_back_responses))

        print(f"Chatbot: {response}")

if __name__ == "__main__":
    create_Chatbot()
        
        
        

        