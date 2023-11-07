import app

if __name__ == "__main__":
    try:
        app.init()
        app.main()
    except Exception as e:
        print("Error Occured!!!\n")
        print(e)
