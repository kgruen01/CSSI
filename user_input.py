dictionary = {"hello" : "I don't know that word.", "yes" : "Okay."}


def get_something():
    print "Please type something"
    print dictionary[raw_input()]
    dictionary["hello"] = "I know that word now!"
    print "Want to help me learn? Try again"
    print dictionary[raw_input()]
    print "I bet you want to leave me now..."
    print dictionary[raw_input()]
    return "I'll let you go now."
print get_something()
