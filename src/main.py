from app.input_handler import InputHandler

def init() -> None:
    print("Welcome to Smart Manager Application")
    print()

def main(inputhandler: InputHandler) -> None:
    while True:
        inp = inputhandler.input(">>").strip()
        
        if inp == "quit":
            print("Quitting the app...")
            return
        
        if inp != "":
            print("Invalid Input!!!")

if __name__ == "__main__":
    init()
    main(InputHandler())
