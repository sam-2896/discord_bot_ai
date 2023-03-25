import random
import chatai

def get_response(message: str) -> str:
    p_message = message.lower()


    if len(p_message)>1 and p_message[0]=="?":
        return chatai.ask(p_message[1:])

    return
