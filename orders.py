import random

def retrieve_order(character1=None, character2=None, location1=None, location2=None, misc_location1=None, misc_location2=None):

    standard = [f"{character1} needs you to make a delivery to {location1}.", f"{character1} requests that you deliver cargo to {character2} at {location1}"]
    retrieval = [f"{character1} lost supplies to a flood. Retrieve them from {misc_location1} and return them to {location1}.", f"An evil group of rental owners stole facility building materials from {character1}. Retrieve the stolen supplies from {location1} and return them to {character1} at {location2}"]

    order = "No Available Order"

    order_type = random.choice(["standard", "retrieval"])

    if order_type == "standard":
        order = standard[random.randint(0, len(standard) - 1)]

    elif order_type == "retrieval":
        order = retrieval[random.randint(0, len(retrieval) - 1)]

    return order