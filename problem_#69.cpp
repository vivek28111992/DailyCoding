
// Good morning! Here's your coding interview problem for today.

// This problem was asked by Facebook.

// Given a list of integers, return the largest product that can be made by multiplying any three integers.

// For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

// You can assume the list has at least three integers.


#include <bits/stdc++.h>
using namespace std;

/* Function to find a maximum product of a triplet in array of integers of size n */
int maxProduct(int arr[], int n) {
	// if size is less than 3, no triplet exists
	if (n < 3) {
		return -1;
	}

	// Construct four auxillary vectors of size n and initialize them by -1
	vector<int> leftMin(n , -1);
	vector<int> rightMin(n, -1);
	vector<int> leftMax(n, -1);
	vector<int> rightMax(n, -1);

	// // will contain max product
	int max_product = INT_MIN;

	// // to store maximum element on left of array
	int max_sum = arr[0];

	// // to store minimum element on left of array
	int min_sum = arr[0];

	// // leftMax[i] will contain max element on left of arr[i] excluding arr[i]
	// // leftMin[i] will contain min element on left of arr[i] excluding arr[i]
	for (int i = 1; i < n; i++) {
		leftMax[i] = max_sum;
		if(arr[i] > max_sum) {
			max_sum = arr[i];
		}

		leftMin[i] = min_sum;
		if(arr[i] < min_sum) {
			min_sum = arr[i];
		}
	}

	// // reset max_sum to store maximum element on right of array
	max_sum = arr[n - 1];

	// // reset min_sum to store maximum element on right of array
	min_sum = arr[n - 1];

	// // rightMax[j] will contain max element on right of arr[j] excluding arr[j]
	// // rightMin[j] will contain min element on right of arr[j] excluding arr[j]
	for(int j = n - 2; j > -1; j--) {
		rightMax[j] = max_sum;
		if(arr[j] > max_sum) {
			max_sum = arr[j];
		}

		rightMin[j] = min_sum;
		if(arr[j] < min_sum) {
			min_sum = arr[j];
		}
	}

	// for all array indexes i except first & last, compute maximum of arr[i]*x*y
	// where x can be leftMax[i] or leftMin[i] & y can be rightMax[i] or rightMin[i]
	for(int i = 1; i < n -1; i++) {
		int max1 = max(arr[i] * leftMax[i] * rightMax[i], arr[i] * leftMin[i] * rightMin[i]);

		int max2 = max(arr[i] * leftMax[i] * rightMin[i], arr[i] * leftMin[i] * rightMax[i]);

		max_product = max(max_product, max(max1, max2));
	}

	return max_product;
}

// Driver program to test above functions
int main() {
	int arr[] = { -10, -10, 5, 2 };
	int n = sizeof(arr) / sizeof(arr[0]);

	int max = maxProduct(arr, n);

	if (max == -1) {
		cout << "No Triplet Exists"; 
	} else {
		cout << "Maximum product is " << max;
	}
	return 0;
}
