import facebook as fb

def connectToAPI(token, version="2.11"):
    return fb.GraphAPI(access_token=token, version="2.11")