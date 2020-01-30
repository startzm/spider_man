class SpiderMixin():
    name: str=None

    def start_requests(self):
        return self.next_requests()

