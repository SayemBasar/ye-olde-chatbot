from chatbot import Chatbot

def main():
    bot=Chatbot()
    encoded = bot.encode_prompt("Hello, how are you?")
    print(encoded)

    reply = bot.decode_reply([15496, 11, 703, 389, 345, 30]) 
    # Pass in a string of generated token IDs here from your tokenizer
    print(reply)

    prompt = "What is the weather like today?"
    reply = bot.generate_reply(prompt)
    print(f"Prompt: {prompt}")
    print(f"Reply: {reply}")

    # You should see a natural language response like:
    # "It's sunny and warm in most areas today."
    # (Although the response may be quite off-topic - this is normal with smaller models!)

    prompt = "What is the weather like today?"
    reply = bot.generate_reply(prompt)
    print(f"Prompt: {prompt}")
    print(f"Reply: {reply}")
    # You should see a natural language response like:
    # "It's sunny and warm in most areas today."
    # (Although the response may be quite off-topic - this is normal with smaller models!)


main()