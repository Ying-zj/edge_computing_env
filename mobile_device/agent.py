class Device:
    def __init__(self, interference_power, noise_power):
        self.connect_list = self.init_connectivity()
        self.beta = self.init_beta()
        self.machine_frequency = self.init_frequency()
        self.power = self.init_power()
        self.interference_power = interference_power
        self.noise_power = noise_power
        self.uplink_trans_speed = 0
        self.state = True
        self.task_list = None

    def init_connectivity(self):
        pass

    def init_beta(self):
        pass

    def init_frequency(self):
        pass

    def init_power(self):
        pass

    def cal_uplink_trans_speed(self):
        pass

    def task_partition(self):
        pass

    def trans_task(self):
        pass

    def cal_local_time(self):
        pass

    def cal_local_power_consumption(self):
        pass
