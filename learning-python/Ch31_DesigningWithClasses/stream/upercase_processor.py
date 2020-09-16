from processor import Processor


class UppercaseProcessor(Processor):
    def converter(self, data):
        return data.upper()