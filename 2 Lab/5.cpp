#include <iostream>
#include <vector>

using namespace std;


int quickSort(vector<int> &array, int low, int high, int k) {
    int i = low;
    int j = high;
    int pivot = array[(i + j) / 2];
    while (i <= j) {
        while (array[i] < pivot) i++;
        while (array[j] > pivot) j--;
        if (i <= j) {
            swap(array[i++], array[j--]);
        }
    }
    if (k <= j) quickSort(array, low, j, k);
    if (k >= i) quickSort(array, i, high, k);
    return array[k];
}

int main() {
    freopen("kth.in", "r", stdin);
    freopen("kth.out", "w", stdout);

    int n, k, A, B, C;
    cin >> n >> k >> A >> B >> C;
    vector<int> arr(n);
    cin >> arr[0] >> arr[1];
    for (int i = 2; i < n; i++) {
        arr[i] = A * arr[i - 2] + B * arr[i - 1] + C;
    }
    cout << quickSort(arr, 0, n - 1, k - 1);
}
