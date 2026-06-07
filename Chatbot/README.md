# Rule-Based Chatbot in Python

## Overview

This project is a simple Rule-Based Chatbot developed in Python. The chatbot responds to predefined user inputs such as greetings, questions about itself, requests for book recommendations, expressions of gratitude, and farewell messages.

The chatbot uses a dictionary-based response system and randomly selects a response from a predefined list for each recognized user input.

---

## Features

* Responds to common greetings (Hi, Hey, Hello)
* Answers questions about its identity and purpose
* Provides book recommendations
* Handles thank-you messages
* Responds to farewell messages
* Displays fallback responses for unknown inputs
* Uses random responses to make conversations feel more natural

---

## Technologies Used

* Python 3.x
* Random Module

---

## Project Structure

```text
Chatbot_Project/
│
├── chatbot.py
└── README.md
```

---

## How It Works

1. The chatbot stores predefined user inputs and corresponding responses in a dictionary.
2. User input is converted to lowercase to ensure case-insensitive matching.
3. If the input matches a predefined key, a random response is selected.
4. If no match is found, the chatbot returns a fallback response.
5. The conversation continues until the user enters:

   * exit
   * quit
   * bye
   * goodbye

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to the Project Folder

```bash
cd Chatbot_Project
```

### Run the Program

```bash
python chatbot.py
```

---

## Sample Interaction

```text
==================================================
Chatbot Activated
==================================================

You: hi
Chatbot: Hello! Great to see you!

You: what is your name ?
Chatbot: I'm an AI assistant built with Python.

You: suggest me some good books
Chatbot: Surely! Here is a list of good books to read...

You: thanks
Chatbot: You're welcome, I'm glad I could help

You: goodbye
Chatbot: Take care!
```

---

## Supported Commands

### Greetings

* hi
* hey
* hello

### Personal Questions

* what is your name ?
* who are you

### General Questions

* how are you ?
* how have you been ?
* what's up
* what can you do
* what is your job
* what do you do ?

### Book Recommendations

* suggest me some good books
* give me a list of books to read

### Gratitude

* thankyou
* thanks

### Exit Commands

* exit
* quit
* bye
* goodbye

---

## Future Improvements

* Add Natural Language Processing (NLP)
* Support partial matching instead of exact matching
* Store conversation history
* Add more knowledge domains
* Implement a graphical user interface (GUI)
* Integrate speech recognition and text-to-speech
* Connect with external APIs for dynamic responses

---

## Learning Outcomes

Through this project, you can learn:

* Python dictionaries and lists
* Functions and loops
* Conditional statements
* String manipulation
* Random response generation
* Basic chatbot development concepts

---

## Author

Developed as a Python Rule-Based Chatbot project for learning conversational AI fundamentals.
