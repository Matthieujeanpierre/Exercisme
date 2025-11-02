def response(hey_bob):
    hey_bob = hey_bob.strip()
    
    if not hey_bob:  # silence
        return "Fine. Be that way!"
    elif hey_bob.isupper() and hey_bob.endswith("?"):  # cri + question
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():  # cri
        return "Whoa, chill out!"
    elif hey_bob.endswith("?"):  # question normale
        return "Sure."
    else:
        return "Whatever."
