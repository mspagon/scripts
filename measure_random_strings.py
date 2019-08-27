import os
import timeit
import uuid

from binascii import hexlify


class Names:
    @staticmethod
    def get_urandom():
        """Gets a random name of length 6 using os.urandom."""
        return hexlify(os.urandom(3))

    @staticmethod
    def get_uuid():
        """Gets a random name of length 6 using uuid4."""
        return str(uuid.uuid4())[:6]


def test_time(executions=1000000):
    time_urandom = timeit.timeit(stmt='Names.get_urandom()',
                                 setup='from __main__ import Names',
                                 number=executions)
    time_uuid = timeit.timeit(stmt='Names.get_uuid()',
                              setup='from __main__ import Names',
                              number=executions)

    print('Generating random names (6 characters long) using UUIDs and os.urandom')
    print('Running {:,} times...'.format(executions))
    print('-' * 25)
    print('urandom: {} seconds'.format(time_urandom))
    print('uuid: {} seconds'.format(time_uuid))


def _test_collisions(func, executions=1000000):
    ok, collision = 0, 0
    names = set()
    for _ in range(executions):
        name = func()
        if name in names:
            collision += 1
        else:
            names.add(name)
            ok += 1

    return ok, collision


def test_collisions():
    from spagon_code.runtime import names
    import time

    tests = [names.get_urandom, names.get_uuid]

    for func in tests:
        start = time.time()
        ok, bad = _test_collisions(func)
        end = time.time()

        print('{} results'.format(func.__name__))
        print('-' * 30)
        print('{bad} collisions, {ok} ok, {total} total | '
              .format(bad=bad, ok=ok, total=bad + ok), end='')
        print('runtime: {} seconds\n'.format(end - start))


def main():
    test_time()
    test_collisions()


if __name__ == '__main__':
    main()
