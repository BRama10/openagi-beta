from pydantic import BaseModel


class Submodule:
    def __init__(self, name: str, version: float):
        self.presets = None

    def run_clean(self, message):
        pass

    def run_json(self, message):
        pass

    

class Kernel:
    def __init__(self, submodule: Submodule):
        self.submodule = submodule

    def inference(self, message: str, json: bool, schema: dict | BaseModel, **kwargs):
        self.submodule.
        if not json:
            return self.submodule.run_clean(message)
        else:
            return self.submodule.run_json(message)