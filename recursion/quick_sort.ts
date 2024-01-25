// partition
function partition(arr: number[], hi: number, lo: number): number {
  const pivot = arr[hi];
  let idx = lo - 1;

  for (let i = lo; i < hi; i++) {
    // swap if element is smaller than pivot
    if (arr[i] <= pivot) {
      idx++;
      const tmp = arr[i];
      arr[i] = arr[idx];
      arr[idx] = tmp;
    }
  }

  idx++;
  arr[hi] = arr[idx];
  arr[idx] = pivot;

  return idx;
}
// qs
function qs(arr: number[], lo: number, hi: number) {
  if (lo >= hi) {
    return;
  }
  const pivotIdx = partition(arr, lo, hi);

  qs(arr, lo, pivotIdx - 1);
  qs(arr, pivotIdx + 1, hi);
}

export default function quick_sort(arr: number[]): void {
  qs(arr, 0, arr.length - 1);
}
