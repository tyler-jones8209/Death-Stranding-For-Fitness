import random

def retrieve_order(prepper1=None, prepper2=None, location1=None, location2=None, misc_location1=None, misc_location2=None):

    standard = [f"{prepper1} needs you to take this cargo to {location1}."]
    retrieval = [f"{prepper1} lost supplies to a flood. Retrieve them from {misc_location1} and return them at {location1}."]

    order = "No Available Order"

    order_type = random.choice(["standard", "retrieval"])

    if order_type == "standard":
        order = standard[random.randint(0, len(standard) - 1)]

    elif order_type == "retrieval":
        order = retrieval[random.randint(0, len(retrieval) - 1)]

    return order