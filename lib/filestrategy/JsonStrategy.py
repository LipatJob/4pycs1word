import json
class JsonDecoder:
    """ Json Facade for Decoder type """
    def decode(self, data):
        if data.strip() == "":
            data = "[]"
        return json.loads(data)
    
import json
class JsonEncoder:
    """ Json Facade for Encoder type """
    def encode(self, data):
        return json.dumps(data)