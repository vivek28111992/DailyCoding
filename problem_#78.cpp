#include <bits/stdc++.h>
using namespace std;

// A Linked List node
struct Node
{
    /* data */
    int data;
    Node* next;
};

void printList(Node* node)
{
    while (node != NULL)
    {
        /* code */
        printf("%d ", node->data);
        node = node->next;
    }
}

/* Takes two lists sorted in increasing order, and merge 
   their nodes together to make one big sorted list. Below 
   function takes O(Log n) extra space for recursive calls, 
   but it can be easily modified to work with same time and 
   O(1) extra space  */
Node* SortedMerge(Node* a, Node* b) 
{
    Node* result = NULL;

    /* Base Case */
    if(a == NULL) {
        return (b);
    } else if(b == NULL) {
        return (a);
    }

    /* Pick either a or b, & recur */
    if(a->data <= b->data) {
        result = a;
        result->next = SortedMerge(a->next, b);
    } else {
        result = b;
        result->next = SortedMerge(a, b->next);
    }

    return result;
}

// The main function that takes an array of lists 
// arr[0..last] and generates the sorted output 
Node* mergeKLists(Node* arr[], int last)
{
    // repeat untill only one list is left
    while (last != 0)
    {
        int i = 0, j = last;

        // (i, j) forms a pair
        while (i < j)
        {
            // merge List i with List j and store
            // merge list in List i
            arr[i] = SortedMerge(arr[i], arr[j]);

            // consider the next pair
            i++, j--;

            // if all pairs are merged, update last
            if(i >= j) {
                last = j;
            }
        }
    }
    return arr[0];
}

// Utility function to create a new node. 
Node *newNode(int data) 
{ 
    struct Node *temp = new Node; 
    temp->data = data; 
    temp->next = NULL; 
    return temp; 
}   

// Driver program to test above functions 
int main() 
{ 
    int k = 3; // Number of linked lists 
    int n = 4; // Number of elements in each list 
  
    // an array of pointers storing the head nodes 
    // of the linked lists 
    Node* arr[k]; 
  
    arr[0] = newNode(1); 
    arr[0]->next = newNode(3); 
    arr[0]->next->next = newNode(5); 
    arr[0]->next->next->next = newNode(7); 
  
    arr[1] = newNode(2); 
    arr[1]->next = newNode(4); 
    arr[1]->next->next = newNode(6); 
    arr[1]->next->next->next = newNode(8); 
  
    arr[2] = newNode(0); 
    arr[2]->next = newNode(9); 
    arr[2]->next->next = newNode(10); 
    arr[2]->next->next->next = newNode(11); 
  
    // Merge all lists 
    Node* head = mergeKLists(arr, k - 1); 
  
    printList(head); 
  
    return 0; 
} 
