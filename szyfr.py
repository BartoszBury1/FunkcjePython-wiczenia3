import base64

def encode_base64 (text):

    encoded_text = base64.b64encode(text.encode("utf-8"))

    return encoded_text.decode()

def decode_base(encoded_text):
    decoded_text = base64.b16decode(encoded_text.encode("utf-8")).decode()
    return decoded_text

text = "Ta wiadomosc jest zaszyfrowana"
encoded_text = encode_base64(text)
print (encoded_text)

decoded_text = encode_base64(encoded_text)
print (decoded_text)