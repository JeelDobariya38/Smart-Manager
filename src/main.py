import app

import sys

ISDEBUGGING = False

def main():
    try:
        app.init()
        app.main()
    except Exception as e:
        print("Error Occured!!!\n")
        print(e)

def debug():
    app.init()
    app.main()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        ISDEBUGGING = "--debug" == sys.argv[1]

    if ISDEBUGGING:
        print("Active Debugging...\n")
        debug()
    else:
        main()
