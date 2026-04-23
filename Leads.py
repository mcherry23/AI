leads = []

def chatbot(user_input, state):
    user_input = user_input.lower()

    if state == "start":
        state = "ask_interest"
        return "Hi! What are you interested in? (music promotion, booking, services)", state

    elif state == "ask_interest":
        state = "ask_budget"
        return "Nice! What’s your budget range?", state

    elif state == "ask_budget":
        state = "ask_contact"
        return "Got it. Can I get your email or phone number?", state

    elif state == "ask_contact":
        leads.append(user_input)
        state = "done"
        return "Thanks! We’ll reach out soon.", state

    else:
        return "Do you want to start again? (yes/no)", "start"


state = "start"

while True:
    user = input("You: ")
    response, state = chatbot(user, state)
    print("Bot:", response)
