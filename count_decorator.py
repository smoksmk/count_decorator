import logging
logger = logging.getLogger('count_decorator')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Counter:
    count = 0

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            self.count += 1
            func = f(*args, **kwargs)
            logger.debug(self.count)
            return func

        return wrapper


count_decorator = Counter()


@count_decorator
def hello_world():
    logger.info('hello world')


if __name__ == '__main__':
    logger.setLevel(logging.DEBUG)
    for i in range(0, 10):
        hello_world()
