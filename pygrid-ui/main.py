
import sys
from QStatApplication import QStatApplication


def main(*args, **kwargs):

    app = QStatApplication()
    return app.run()


if __name__ == '__main__':
    main(sys.argv)
