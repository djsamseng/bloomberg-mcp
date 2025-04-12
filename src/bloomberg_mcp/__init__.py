import blpapi

def main() -> None:
    print("blpapi version:", blpapi.version())

    options = blpapi.SessionOptions()
    # On windows this will be BBComm which runs on the same PC as the Terminal (localhost)
    # On linux this will be a different machine's ip address
    options.setServerHost("localhost")
    options.setServerPort(8194)
    session = blpapi.Session(options)
    res = session.start()
    print("Created session:", session, res)
