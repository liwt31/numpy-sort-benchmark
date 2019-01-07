# -*- encoding: utf-8 -*-
import time
import argparse

import numpy as np

from benchmark import bench_suite


def run(bs, seed, size, loops):
    np.random.seed(seed)
    print(f'Array size: {size}. Loop num: {loops}')
    for name, func in bs.funcs.items():
        base_time = None
        print(f'Testing {name} array:')
        for kind in bs.sort_kinds:
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--random_seed', type=int, default=123)
    parser.add_argument('--array_size', type=int, default=10000)
    parser.add_argument('--loops', type=int, default=100)
    args = parser.parse_args()
    run(bench_suite, args.random_seed, args.array_size, args.loops)
