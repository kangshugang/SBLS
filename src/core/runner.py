
'''
    log_database (SQLite3)
        [solutions]
            id
            parent_d
            count
            performance

        [decisions]
            agent_request
            global_features
            local_features
            decsion_info
            solution_id
'''

class Runner :

    def __init__(self, model):
        self.model = model

    def run(model):
        pass

        # loop
            # while stack is not empty
                # pop a request from the stack
                # call the agent to handle the request
                # if return False
                    # terminate (failed)
                # if return True
                    # continue
                # if return a sequence of requests
                # generate request sequences based on the quota of the model
                # if there is only once request sequence:
                    # push the request into the stack
                    # continue
                # else
                    # for each request squence
                        # create a copy of the model
                        # push/post the request sequence into the stack/event queue
                        # save the copied model
                    # end

            # if current events is not empty:
                # pick one request and push to the stack
                # continue

            # if future events are not empty:
                # pick the top request
                # advance the clock
                # push the request to the stack

