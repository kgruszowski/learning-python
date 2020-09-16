from processor import Processor


class OddProcessor(Processor):
    def converter(self, data):
        return data[::2]