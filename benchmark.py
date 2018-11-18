# -*- encoding: utf-8 -*-
import time
import argparse

import numpy as np


class BenchSuite:

    sort_kinds = ['quick', 'merge', 'heap', 'tim']

    def __init__(self):
        self.funcs = dict()

    def __call__(self, func):
        self.funcs[func.__name__] = func
        return func

    def run(self, seed, size, loops):
        np.random.seed(seed)
        print(f'Array size: {size}. Loop num: {loops}')
        for name, func in self.funcs.items():
            base_time = None
            print(f'Testing {name} array:')
            for kind in self.sort_kinds:
                times = []
                for i in range(loops):
                    arr, answer = func(size)
                    time1 = time.time()
                    arr.sort(kind=kind)
                    time2 = time.time()
                    times.append(time2 - time1)
                    assert np.allclose(arr, answer)
                times = np.array(times) * 1e6
                mean, std = times.mean(), times.std()
                if base_time is None:
                    base_time = times.mean()
                print(f'    {kind}: {mean:.3f}±{std:.3f} us per loop. Relative: {mean/base_time*100:.0f}%')
            print()


bench_suite = BenchSuite()


@bench_suite
def random(size):
    a = np.arange(size)
    np.random.shuffle(a)
    return a, np.arange(size)


@bench_suite
def ordered(size):
    return np.arange(size), np.arange(size)


@bench_suite
def reversed(size):
    return np.arange(size-1, -1, -1), np.arange(size)


@bench_suite
def same_elem(size):
    return np.ones(size), np.ones(size)


def sorted_block(size, block_size):
    a = np.arange(size)
    b = []
    if size < block_size:
        return a, a
    block_num = size // block_size
    for i in range(block_num):
        b.extend(a[i::block_num])
    return np.array(b), a


@bench_suite
def sorted_block_size_10(size):
    return sorted_block(size, 10)


@bench_suite
def sorted_block_size_100(size):
    return sorted_block(size, 100)


@bench_suite
def sorted_block_size_1000(size):
    return sorted_block(size, 1000)


def swapped_pair(size, swap_frac):
    a = np.arange(size)
    b = a.copy()
    for i in range(int(size * swap_frac)):
        x, y = np.random.randint(0, size, 2)
        b[x], b[y] = b[y], b[x]
    return b, a


@bench_suite
def swapped_pair_50_percent(size):
    return swapped_pair(size, 0.5)


@bench_suite
def swapped_pair_10_percent(size):
    return swapped_pair(size, 0.1)


@bench_suite
def swapped_pair_1_percent(size):
    return swapped_pair(size, 0.01)


def random_unsorted_area(size, frac, area_num):
    area_num = int(area_num)
    a = np.arange(size)
    b = a.copy()
    unsorted_len = int(size * frac / area_num)
    for i in range(area_num):
        start = np.random.randint(size-unsorted_len)
        end = start + unsorted_len
        np.random.shuffle(b[start:end])
    return b, a


AREA_NUM = 10


@bench_suite
def random_unsorted_area_50_percent(size):
    return random_unsorted_area(size, 0.5, AREA_NUM)


@bench_suite
def random_unsorted_area_10_percent(size):
    return random_unsorted_area(size, 0.1, AREA_NUM)


@bench_suite
def random_unsorted_area_1_percent(size):
    return random_unsorted_area(size, 0.01, AREA_NUM)


BUBBLE_SIZE = 10


@bench_suite
def random_bubble_1_fold(size):
    return random_unsorted_area(size, 1, size / BUBBLE_SIZE)


@bench_suite
def random_bubble_5_fold(size):
    return random_unsorted_area(size, 5, size / BUBBLE_SIZE)


@bench_suite
def random_bubble_10_fold(size):
    return random_unsorted_area(size, 10, size / BUBBLE_SIZE)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--random_seed', type=int, default=123)
    parser.add_argument('--array_size', type=int, default=10000)
    parser.add_argument('--loops', type=int, default=100)
    args = parser.parse_args()
    bench_suite.run(args.random_seed, args.array_size, args.loops)
