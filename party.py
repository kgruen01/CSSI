def get_guests():
    guests = []
    name = "something"
    while True:
        name = raw_input("Who's coming? ")
        if name == "":
            break
        guests.append(name)
    return guests



def say(what, guests):
    for x in guests:
        # print "Hi, {0}".format(x)
        print what + ", " + x



def inflate_balloons():
    print "The baloons are inflated."

def start_music():
    print "'I Want It That Way' is playing."

def cheer(number_of_times):
    for j in range(number_of_times):
        print "whoop de doo."




def party():
    guests = get_guests()
    say("Hello", guests)
    inflate_balloons()
    start_music()
    cheer(8)
    say("Goodbye", guests)


party()
