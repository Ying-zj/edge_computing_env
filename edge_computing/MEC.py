class MEC:
    def __init__(self, connection_matrix):
        self.connect_list = self.init_connectivity(connection_matrix)
        self.machine_frequency = self.init_frequency()
        self.communication_resource = self.init_communication_resource()

    def init_connectivity(self, connection_matrix):
        pass

    def init_frequency(self):
        pass

    def init_communication_resource(self):
        pass

    def trans_task_to_md(self, md_index):
        pass
