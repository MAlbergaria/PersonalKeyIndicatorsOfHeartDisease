import json


class Entity(object):

    def __init__(self, id=None) -> None:
        self.id = id

    
    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4))


    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Entity):
            return self.id == __o.id
        return False