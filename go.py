from SimplifyPython import scrypto
from urllib.parse import quote

def retrive(data):
    database = {"fKZKuYlGQ8Z5EvWfMZEGRz2Uubg66q": {"title": "gAAAAABiw_THjocJWyOZs0bR3EplC_t-944O6omZb8kZ4vy-aOcNvY80NtzNqQm0D4fEoScDYB1Hx046203-vCGzgTuqWejFCg==", "text": "gAAAAABiw_THmycXADPxh9YTlP0msTm1wUxUTQxcRjKkWrrJ6LmTSYMiOzvDxQ48YAmFEQvjbYz9bRRGCPE4k_v5fKXbAO0pcg=="}}

    if data['id'] in database:
        key = scrypto.generate_key(data['password'], b'')

        enc_title = database[data['id']]['title'].encode()
        
        enc_text = database[data['id']]['text'].encode()

        title = scrypto.decrypt(key, enc_title)

        text = scrypto.decrypt(key, enc_text)

        return f'title={quote(title)}&text={quote(text)}'
        
    return 'title=404&text=Your%20id%20either%20does%20not%20exist%20or%20your%20passowrd%20is%20not%20valid.'

print(retrive([('title', 'fKZKuYlGQ8Z5EvWfMZEGRz2Uubg66q'), ('password', 'Test')]))