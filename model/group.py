from sys import maxsize

class Group:
    def __init__(self, name=None, header=None, footer=None, gr_id=None):
        self.name = name
        self.header =  header
        self.footer = footer
        self.id = gr_id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize