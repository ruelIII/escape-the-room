def describe_room():
    print("You find yourself in a dimly lit room. Around you, you see:")
    print("1. A dusty bookshelf full of old books.")
    print("2. A locked drawer in a wooden desk.")
    print("3. A small window with rusty bars.")

def examine_bookshelf():
    global has_key
    if not has_key:
        print("You search the bookshelf and find an old, rusty key hidden between the pages of a book.")
        has_key = True
    else:
        print("You already found the key here. There is nothing else of interest.")

def open_drawer():
    if has_key:
        print("You use the key to unlock the drawer. Inside, you find a door handle mechanism.")
        print("Congratulations! You have escaped the room!")
        return True
    else:
        print("The drawer is locked. Maybe there is a key somewhere in the room.")
        return False

def look_out_window():
    print("Through the dirty glass, you see a dark alley outside. There’s no way to escape through here.")

def main():
    global has_key
    has_key = False
    escaped = False
    
    print("Welcome to 'Escape the Room'!")
    describe_room()
    
    while not escaped:
        action = input("What do you want to do? (examine bookshelf / open drawer / look out window / quit): ").strip().lower()
        
        if action == "examine bookshelf":
            examine_bookshelf()
        elif action == "open drawer":
            escaped = open_drawer()
        elif action == "look out window":
            look_out_window()
        elif action == "quit":
            print("You give up. Game over!")
            break
        else:
            print("Invalid action. Try again.")

if __name__ == "__main__":
    main()
