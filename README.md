# numpy-sort-benchmark
Benchmark result for numpy sorting algorithms. Includes Quicksort, Mergesort, Heapsort and Timsort. Focused on nearly sorted data.

### Benchmark output
![sort_type](https://user-images.githubusercontent.com/22628546/50800096-bbf4bf00-1319-11e9-885b-51acd062673b.png)
![distribution](https://user-images.githubusercontent.com/22628546/50800095-bac39200-1319-11e9-8312-61f63a2b45de.png)
For detailed numbers, see the *.txt Files.

### Comments
* For shapes of the arrays involved in this benchmark, see the jupyter-notebook.
* Timsort shows minimal overhead on random array while performs well at nearly sorted array.
* For swapped pair arrays timsort seems not fast enough, however this is because quicksort is so good at this kind of array.
