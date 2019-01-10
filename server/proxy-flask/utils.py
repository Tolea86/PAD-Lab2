from itertools import cycle, islice


class UrlHandling:
    def __init__(self):
        pass

    @classmethod
    def parse_url(klass, url, server_route):
        if url[-1] == '/':
            url = url[:-1]

        return '{}{}/'.format(server_route, url)


class RoundRobin:
    def __init__(self, nodes):
        self.nodes = nodes

    def rotate_nodes(self):
        self.nodes = self.nodes[-1:] + self.nodes[:-1]

    def next_host(self):
        self.rotate_nodes()
        rotated_nodes = self.round_robin(self.nodes)
        return next(rotated_nodes)

    @staticmethod
    def round_robin(*iterables):
        pending = len(iterables)
        nexts = cycle(iter(it).__next__ for it in iterables)
        while pending:
            try:
                for next in nexts:
                    yield next()
            except StopIteration:
                pending -= 1
                nexts = cycle(islice(nexts, pending))
