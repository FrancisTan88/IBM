#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>
#include <math.h>

typedef struct node{
    unsigned long long hash_val;
    unsigned long long index;
} Node;

//create node
Node *CreateNode(unsigned long long hash_val, unsigned long long index){
    Node *new_node = (Node *)malloc(sizeof(Node));
    new_node->hash_val = hash_val;
    new_node->index = index;
    return new_node;
}

//convert string into integer and store it and its index in an array
void cal_HashVal(char **string, unsigned long long num_magic, unsigned long long len_magic, Node **arr_hash, int d){
    unsigned long long hash_val = 0;
    unsigned long long q = 2.45302 * pow(10, 16); //24530200000000000
    for(unsigned long long i = 0; i < num_magic; i++){
        for(unsigned long long j = 0; j < len_magic; j++){
            int str_val = string[i][j]-32; // str to int
            hash_val = (d*hash_val + str_val) % q; //calculate hash value 
        }
        Node *new_node = CreateNode(hash_val, i);
        arr_hash[i] = new_node; // store hash value to another array
        hash_val = 0;
    }
}

void Merge(Node **arr_hash, long long left, long long middle, long long right){
    long long len_left = middle - left + 1;
    long long len_right = right - middle;
    Node *arr_left[len_left];
    Node *arr_right[len_right];
    for(long long i = 0; i < len_left; i++){
        arr_left[i] = arr_hash[left + i];
    }
    for(long long j = 0; j < len_right; j++){
        arr_right[j] = arr_hash[middle + 1 + j];
    }

    long long i = 0;
    long long j = 0;
    long long k = left;
    while(i < len_left && j < len_right){
        if(arr_left[i]->hash_val <= arr_right[j]->hash_val){
            arr_hash[k] = arr_left[i];
            i++;
        }
        else{
            arr_hash[k] = arr_right[j];
            j++;
        }
        k++;
    }
    while(i < len_left){
        arr_hash[k] = arr_left[i];
        i++;
        k++;
    }
    while(j < len_right){
        arr_hash[k] = arr_right[j];
        j++;
        k++;
    }

}

void MergeSort(Node **arr_hash, long long left, long long right){
    if(left < right){
        long long middle = left + (right-left)/2;
        MergeSort(arr_hash, left, middle);
        MergeSort(arr_hash, middle+1, right);
        Merge(arr_hash, left, middle, right);
    }
}

long long AddUp(Node **arr_hash, unsigned long long num_magic, int flag, long long *arr_index){
    unsigned long long pairs = 0;
    unsigned long long num_same = 1;
    unsigned long long prev = arr_hash[0]->hash_val; //define the prev in advance
    for(unsigned long long i = 1; i < num_magic; i++){ //start from 2rd place
        if(i == num_magic-1 && arr_hash[i]->hash_val == prev){
            if (flag == 0){
                arr_index[0] = arr_hash[i]->index;
                arr_index[1] = arr_hash[i-1]->index;
            }
            num_same++;
            pairs += num_same*(num_same-1) / 2;
            break;
        }
        if(arr_hash[i]->hash_val == prev){
            if (flag == 0){
                arr_index[0] = arr_hash[i]->index;
                arr_index[1] = arr_hash[i-1]->index;
            }
            num_same++;
        }
        else{
            pairs += num_same*(num_same-1) / 2;
            num_same = 1;
        }
        prev = arr_hash[i]->hash_val;
    }
    return pairs;
}

long long find_similar(char **string, Node **arr_hash, unsigned long long *arr_carry_bit, Node **arr_hash_without_one, unsigned long long num_magic, unsigned long long len_magic, unsigned long long q, int flag, long long *arr_index){
    unsigned long long total_pairs = 0;
    unsigned long long hash_without_one = 0;
    long long minus = 0;
    long long tmp_pairs = 0;
    for(unsigned long long j = 0; j < len_magic; j++){
        for(unsigned long long i = 0; i < num_magic; i++){
            Node *new_node = CreateNode(arr_hash[i]->hash_val, arr_hash[i]->index);
            arr_hash_without_one[i] = new_node;
            minus = arr_carry_bit[len_magic-j-1] * (int)(string[i][j]-32) % q; //assure that minus < q
            if(arr_hash[i]->hash_val < minus){
                minus -= q;
            }
            hash_without_one = arr_hash_without_one[i]->hash_val - minus;
            arr_hash_without_one[i]->hash_val = hash_without_one; 
        }
        MergeSort(arr_hash_without_one, 0, num_magic-1);
        tmp_pairs = AddUp(arr_hash_without_one, num_magic, flag, arr_index);
        total_pairs += tmp_pairs;
        memset(arr_hash_without_one, 0, sizeof(*arr_hash_without_one)); 
    }
    return total_pairs;
}

int main(void){
    unsigned long long k,l;
    int flag;
    scanf("%llu", &k); 
    scanf("%llu", &l);
    scanf("%d", &flag);

    char string[k][l];
    char *trans[k];
    memset(string, 0, k*l*sizeof(char));
    memset(trans, 0, sizeof(trans));
    int d = 94;

    //read all input strings
    for(unsigned long long i = 0; i < k; i++){
        scanf("%s", string[i]);
    }
    //transformation
    for(unsigned long long i = 0; i < k; i++){
        trans[i] = string[i];
    }

    //calculate hash value before "without one"
    Node *arr_HashVal[k];
    memset(arr_HashVal, 0, sizeof(arr_HashVal));
    cal_HashVal(trans, k, l, arr_HashVal, d); 
    
    //create HashVal_WithoutOne, arr_carry_bit
    Node *arr_HashVal_WithoutOne[k];
    unsigned long long arr_carry_bit[l];
    memset(arr_HashVal_WithoutOne, 0, sizeof(arr_HashVal_WithoutOne));
    memset(arr_carry_bit, 0, sizeof(arr_carry_bit));
    unsigned long long q = 2.45302 * pow(10, 16);
    unsigned long long exponential = 1;
    arr_carry_bit[0] = 1;
    if(l > 1){
        for(unsigned long long i = 1; i < l; i++){
            exponential *= d;
            exponential %= q;
            arr_carry_bit[i] = exponential;
        }
    }

    //calculate total pairs and all same pairs
    long long total_pairs = 0;
    long long all_same_pairs = 0;
    long long arr_index[2];
    memset(arr_index, 0, sizeof(arr_index));
    total_pairs = find_similar(trans, arr_HashVal, arr_carry_bit, arr_HashVal_WithoutOne, k, l, q, flag, arr_index);
    if(flag == 0 && total_pairs == 0){
        printf("No\n");
        return 0;
    }
    if(flag == 0 && total_pairs != 0){
        printf("Yes\n");
        printf("%lld ", arr_index[0]);
        printf("%lld\n", arr_index[1]);
        return 0;
    }

    MergeSort(arr_HashVal, 0, k-1);
    all_same_pairs = AddUp(arr_HashVal, k, flag, arr_index);
    
    // answer
    if(total_pairs == 0){
        printf("No\n");
    }
    if(total_pairs != 0){
        printf("Yes\n");
        printf("%lld\n", total_pairs - (l-1)*all_same_pairs);
    }    

    return 0;

}