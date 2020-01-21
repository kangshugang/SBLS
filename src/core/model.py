
class RuninngFacilities :
    def __init__(self):
        self.clock = 0
        self.future_events = []
        self.current_events = []
        self.stack = []

class Model :

    def __init__(self, beam_width):
        self.beam_width = beam_width
        self.global_data = {}
        self.agents = {}
        self.running_facilities = RuninngFacilities()

    def save(self, file_name):
        pass

    def load(self, file_name):
        pass

    # create new agent
    def new_agent(self, name, class_name):
        pass

    # access an agent
    def agent(self, name):
        pass

    # evaluate the performance of the system
    def evaluate(self):
        pass
