#include "price.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>
#define ANS_SIZE 1000000

// node
typedef struct node{
    unsigned long long stock_price;
    unsigned long long stock_id;
}Node;

// create node
Node *genNode(unsigned long long stock_id, unsigned long long price){
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->stock_id = stock_id;
    new_node->stock_price = price;
    return new_node;
}

// heap
struct Heap{
    Node **arr;
    int count;
    int length;
};
typedef struct Heap Heap;

// Create heap
Heap *CreateHeap(int length){ // A*N(最大=1024*1024)
    Heap *h = (Heap *)malloc(sizeof(Heap)); //one is number of heap
    assert(h != NULL);
    h->count = 0;
    h->length = length;
    h->arr = (Node **)malloc(length*sizeof(Node*)); 
    return h;
}

void heapify_bt(Heap *heap,int index){
    Node *temp;
    int parent_node = (index-1)/2;
    Node *node_child = heap->arr[index];
    Node *node_parent = heap->arr[parent_node];

    if(node_parent->stock_price > node_child->stock_price){
        temp = heap->arr[parent_node];
        heap->arr[parent_node] = heap->arr[index];
        heap->arr[index] = temp;
        heapify_bt(heap, parent_node); //from child to parent
    }
}

void heapify_tb(Heap *heap, int parent_node){
    int left = parent_node*2+1;
    int right = parent_node*2+2;
    int min;
    Node *temp;
    Node *new_parent_node = heap->arr[parent_node];
    Node *left_node;
    Node *right_node;

    if(left >= heap->count){
        return;
    }
    else{
        left_node = heap->arr[left];
        if (right < heap->count){
            right_node = heap->arr[right];
        } 
    }

    if(left_node->stock_price < new_parent_node->stock_price)
        {min = left;}
    else
        {min = parent_node;}

    Node *min_node = heap->arr[min];
    if(right < heap->count && right_node->stock_price < min_node->stock_price)
        {min = right;}

    if(min != parent_node){
        temp = heap->arr[min];
        heap->arr[min] = heap->arr[parent_node];
        heap->arr[parent_node] = temp;
        heapify_tb(heap, min);
    }
}

void insert(Heap *heap, Node *new_node){
    if( heap->count < heap->length){ // count從0開始，每次+1
        heap->arr[heap->count] = new_node;
        heapify_bt(heap, heap->count); // 每插入新的值就heapify一次
        heap->count++;
    }
}

int find_stock(unsigned long long *arr_A, unsigned long long pop_stock_id, int length_A){
    for(int i = 0; i < length_A; i++){
        if(arr_A[i] == pop_stock_id){
            return i;
        }
    }
    printf("can't not find");
    return -1;
}

int main(void){
    int A,Q,N;
    scanf("%d", &A);
    scanf("%d", &Q);
    scanf("%d", &N);

    //read {A} and store them in array
    unsigned long long stock_id;
    unsigned long long arr_A[A];
    memset(arr_A, 0, sizeof(arr_A));
    for(int i = 0; i < A; i++){
        scanf("%lld", &stock_id);
        arr_A[i] = stock_id;
    }

    // 
    Heap *heap = CreateHeap(A*N); //Min Heap
    assert(heap != NULL);
    for(int i = 0; i < A; i++){
        for(int j = 0; j < N; j++){
            Node *new_node = genNode(arr_A[i], price(arr_A[i], j+1));
            insert(heap, new_node);
        }
    }

    ////////////以上為排好的A*N個price///////////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    unsigned long long arr_ans[ANS_SIZE]; 
    memset(arr_ans, 0, sizeof(arr_ans));

    unsigned long long pop_stock_id;
    unsigned long long pop_stock_price;

    unsigned long long arr_rise_day[A];
    memset(arr_rise_day, 0, sizeof(arr_rise_day));
    int index;
    
    //fill up the arr_rise_day with all N+1
    for(int i = 0; i < A; i++){
        arr_rise_day[i] = N+1;
    }

    for(unsigned long long i = 0; i < ANS_SIZE; i++){ 
        Node *pop_node = heap->arr[0];
        pop_stock_id = pop_node->stock_id;
        pop_stock_price = pop_node->stock_price;

        arr_ans[i] = pop_stock_price; //fill up the answer
        
        index = find_stock(arr_A, pop_stock_id, A); 
        heap->arr[0] = genNode(pop_stock_id, price(pop_stock_id, arr_rise_day[index])); // insert new node
        heapify_tb(heap, 0); // heapify
        arr_rise_day[index] += 1; 
    } 
    // now the arr_ans should be done

    for(int i = 0; i < Q; i++){
        unsigned long long extra;
        unsigned long long num;
        scanf("%lld", &extra);
        scanf("%lld", &num);
        printf("%lld\n", arr_ans[num-1]);
    }

    return 0;
}