import facebook as fb

def connect_to_api(token, version="2.11"):
    return fb.GraphAPI(access_token=token, version="2.11")