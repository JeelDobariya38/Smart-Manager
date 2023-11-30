import app


def main():
    try:
        app.init()
        app.main()
    except Exception as e:
        print("Error" + e)
        input()


if __name__ == "__main__":
    main()
