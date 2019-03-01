from json import JSONEncoder


class JsonObjectEncoder(JSONEncoder):

    def default(self, obj):
        return obj.to_dict()
