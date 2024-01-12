from SmartManager.App import app  # noqa: F401, F403
from SmartManager.Api import api  # noqa: F401, F403
from SmartManager.Database.sqlitedriver import SqliteDriver  # noqa: F401, F403

import sys
import uvicorn
from typing import Dict, List


def help(option: str = ""):
    print("Smart Manager: Securing Passwords, Streamlining Authentication")
    print("")

    if option == "":
        print("Options:")
        print("\t--serve: Run the API")
        print("\t--help:  Show help message")

    if option == "serve" or option == "--serve":
        print("\"Serve\" option:")
        print("\t--serve: Used for running the API")
        print()
        print("Suboptions:")
        print("\t--host: Provide a host for the API (default: 127.0.0.1)")
        print("\t--port: Provide a port for the API (default: 8000)")

    print()
    print("use \"--help [option]\" to get further infomation about the option")
    sys.exit()


def argparser(args: List) -> Dict:
    result = dict()
    if len(args) > 1:
        try:
            for index, arg in enumerate(args, 1):
                if arg == "--help":
                    if len(args) - 1 == index:
                        result["help"] = args[index]
                        return result
                    help()

                # api server
                if arg == "--serve":
                    result["serve"] = True

                if arg == "--host":
                    result["host"] = args[index]

                if arg == "--port":
                    result["port"] = int(args[index])

        except IndexError as e:
            raise ValueError("Provide args ar not valid.")
    return result


def api_run(hostaddress: str = "127.0.0.1", portno: int = 8000):
    uvicorn.run(app=api, host=hostaddress, port=portno)


def app_run():
    app.init(SqliteDriver())
    app.main()


if __name__ == "__main__":
    args = argparser(sys.argv)

    option = args.get("help", None)

    if option != None:  # noqa: E711
        help(option)

    if args.get("serve", False):
        host = args.get("host", "127.0.0.1")
        port = args.get("port", 8000)
        api_run(host, port)
    else:
        app_run()
