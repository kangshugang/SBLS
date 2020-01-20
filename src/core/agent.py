class request :
    def __init__(self, agent_name, request_name, args):
        self.agent_name = agent_name
        self.method = method
        self.args = args

def post(self, requests, delay=0):
    pass

class agent:

    def __init__(self, global_data, instance_data):
        self.global_data = global_data
        self.instance_data = instance_data

    # i_XXX: instance variable
    # g_XXX: global variable
    def __getattr__(self, attr_name):
        pass

    def __setattr__(self, attr_name):
        pass

    # set this agent
    def setup(self):
        pass

    def get_local_features(self):
        pass

    def on_request(self, args):
        pass
