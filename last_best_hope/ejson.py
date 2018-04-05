import json
import arrow
from datetime import datetime

class Encodable(object):
    json_attrs = ()
    def json(self):
        res = {}
        for attr in self.json_attrs:
            res[attr] = getattr(self, attr)
        return res

class Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Encodable):
            return o.json()
        elif isinstance(o, datetime):
            return arrow.get(o)
        elif isinstance(o, arrow.Arrow):
            return str(o)
        else:
            return super(Encoder, self).default(o)
