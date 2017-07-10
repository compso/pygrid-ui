
class Color(object):
    '''
    Color class
    '''
    def __init__(self, r, g, b, a=255):
        self.color = []
        self.color.extend([r, g, b, a])

    @property
    def red(self):
        return self.color[0]

    @property
    def green(self):
        return self.color[1]

    @property
    def blue(self):
        return self.color[2]

    @property
    def rgb(self):
        return "rgb({})".format(",".join([str(item) for item in self.color[:-1]]))

    @property
    def rgba(self):
        return "rgba({})".format(",".join([str(item) for item in self.color]))

    def __repr__(self):
        return str(self.color)

    def __str__(self):
        return self.rgb
