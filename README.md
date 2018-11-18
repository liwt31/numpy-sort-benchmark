# numpy-sort-benchmark
Benchmark result for numpy sorting algorithms

### Benchmark output
```
python benchmark.py
Array size: 10000. Loop num: 100
Testing random array:
    quick: 555.112±143.800 us per loop. Relative: 100%
    merge: 439.970±88.608 us per loop. Relative: 79%
    heap: 864.573±166.900 us per loop. Relative: 156%
    tim: 453.041±140.378 us per loop. Relative: 82%

Testing ordered array:
    quick: 71.297±32.906 us per loop. Relative: 100%
    merge: 172.279±49.136 us per loop. Relative: 242%
    heap: 571.239±119.181 us per loop. Relative: 801%
    tim: 6.578±3.208 us per loop. Relative: 9%

Testing reversed array:
    quick: 110.769±45.496 us per loop. Relative: 100%
    merge: 271.356±76.049 us per loop. Relative: 245%
    heap: 609.262±142.444 us per loop. Relative: 550%
    tim: 11.041±5.111 us per loop. Relative: 10%

Testing same_elem array:
    quick: 128.412±48.271 us per loop. Relative: 100%
    merge: 116.882±40.219 us per loop. Relative: 91%
    heap: 39.163±22.984 us per loop. Relative: 30%
    tim: 16.439±8.431 us per loop. Relative: 13%

Testing sorted_block_size_10 array:
    quick: 463.052±89.128 us per loop. Relative: 100%
    merge: 328.794±60.286 us per loop. Relative: 71%
    heap: 769.053±152.490 us per loop. Relative: 166%
    tim: 318.875±94.272 us per loop. Relative: 69%

Testing sorted_block_size_100 array:
    quick: 481.994±118.741 us per loop. Relative: 100%
    merge: 302.658±86.095 us per loop. Relative: 63%
    heap: 797.091±153.682 us per loop. Relative: 165%
    tim: 218.103±45.817 us per loop. Relative: 45%

Testing sorted_block_size_1000 array:
    quick: 336.759±64.729 us per loop. Relative: 100%
    merge: 249.314±62.653 us per loop. Relative: 74%
    heap: 708.401±68.196 us per loop. Relative: 210%
    tim: 127.838±42.676 us per loop. Relative: 38%

Testing swapped_pair_50_percent array:
    quick: 525.255±127.933 us per loop. Relative: 100%
    merge: 453.367±108.433 us per loop. Relative: 86%
    heap: 846.596±128.636 us per loop. Relative: 161%
    tim: 447.114±109.019 us per loop. Relative: 85%

Testing swapped_pair_10_percent array:
    quick: 236.528±52.280 us per loop. Relative: 100%
    merge: 374.525±153.183 us per loop. Relative: 158%
    heap: 691.171±137.551 us per loop. Relative: 292%
    tim: 371.609±110.122 us per loop. Relative: 157%

Testing swapped_pair_1_percent array:
    quick: 89.276±34.294 us per loop. Relative: 100%
    merge: 282.655±74.108 us per loop. Relative: 317%
    heap: 604.951±84.920 us per loop. Relative: 678%
    tim: 227.041±62.966 us per loop. Relative: 254%

Testing random_unsorted_area_50_percent array:
    quick: 218.461±69.381 us per loop. Relative: 100%
    merge: 267.591±64.033 us per loop. Relative: 122%
    heap: 684.850±141.361 us per loop. Relative: 313%
    tim: 140.715±37.951 us per loop. Relative: 64%

Testing random_unsorted_area_10_percent array:
    quick: 95.243±26.151 us per loop. Relative: 100%
    merge: 185.523±34.714 us per loop. Relative: 195%
    heap: 609.698±91.590 us per loop. Relative: 640%
    tim: 41.602±18.934 us per loop. Relative: 44%

Testing random_unsorted_area_1_percent array:
    quick: 77.276±34.708 us per loop. Relative: 100%
    merge: 181.234±49.420 us per loop. Relative: 235%
    heap: 599.561±114.445 us per loop. Relative: 776%
    tim: 12.274±5.462 us per loop. Relative: 16%

Testing random_bubble_1_fold array:
    quick: 213.075±68.113 us per loop. Relative: 100%
    merge: 265.121±50.630 us per loop. Relative: 124%
    heap: 669.203±131.142 us per loop. Relative: 314%
    tim: 133.908±48.098 us per loop. Relative: 63%

Testing random_bubble_5_fold array:
    quick: 347.090±89.593 us per loop. Relative: 100%
    merge: 351.810±61.638 us per loop. Relative: 101%
    heap: 752.678±140.045 us per loop. Relative: 217%
    tim: 288.360±84.300 us per loop. Relative: 83%

Testing random_bubble_10_fold array:
    quick: 403.938±94.977 us per loop. Relative: 100%
    merge: 400.937±80.454 us per loop. Relative: 99%
    heap: 780.716±122.684 us per loop. Relative: 193%
    tim: 377.831±105.591 us per loop. Relative: 94%
```

### Comments
* For shapes of the arrays involved in this benchmark, see the jupyter-notebook.
* Timsort shows minimal overhead while performs well at nearly sorted array.
* For swapped pair arrays timsort seems not fast enough, however this is because quicksort is so good at this kind of array.
