class Task:
    def __init__(self, beta, mec_num):
        self.B, self.C, self.T = self.init_task(beta)
        self.partition_task = self.init_partition_task(mec_num)

    def init_task(self, beta):
        return (1, 2, 3)

    def init_partition_task(self, mec_num):
        pass

    def adjust_partition_task(self):
        pass
