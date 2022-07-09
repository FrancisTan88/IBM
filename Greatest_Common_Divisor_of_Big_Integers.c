#include <stdio.h>
#include <stdint.h>
#include <assert.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#define max_size 260

void str_to_arr(char *str_input, int *arr_output, int length){
    for (int i = 0; i < length; i++){
        arr_output[i] = str_input[i] - '0';
    }
}
void make_zero(int *small_arr, int diff_len, int len_big){ //when the digits are diff_lenerent
    for (int i = len_big-1; i >= 0 ; i--){
        if (i <= diff_len-1){
            small_arr[i] = 0;
        }
        else{
            small_arr[i] = small_arr[i - diff_len];
        }
    }
}
void subtraction(int *arr1, int *arr2, int length_big, int *answer){
    bool borrow = false;
    for (int i = length_big-1; i >= 0; i--){
        if (borrow){
            if (arr1[i] == 0){
                arr1[i] = 9;
                borrow = true;
            }
            else{
                arr1[i] -= 1;
                borrow = false;
            }
        }
        if (arr1[i] >= arr2[i]){
            answer[i] = arr1[i] - arr2[i];
        }
        else{
            answer[i] = arr1[i] + 10 - arr2[i];
            borrow = true;
        }
    }
}
bool b_not_zero(int *arr_b, int len_arr_b){
    for (int i = 0; i < len_arr_b; i++){
        if (arr_b[i] != 0){
            return true;
        }
    }
    return false;
}
bool a_bigger(int *array1, int *array2, int len_eql){
    for (int i = 0; i < len_eql; i++){
        if (array1[i] > array2[i]){
            return true;
        }
        if (array1[i] < array2[i]){
            return false;
        }
    }
    return false;
}

int main(void){

    char str_a[max_size]; 
    char str_b[max_size];
    int array_a[max_size];
    int array_b[max_size];
    
    scanf("%s", str_a); //enter string num
    scanf("%s", str_b);

    int str_len_a = strlen(str_a);
    int str_len_b = strlen(str_b);

    str_to_arr(str_a, array_a, str_len_a);
    str_to_arr(str_b, array_b, str_len_b);

    int result[max_size];
    while (b_not_zero(array_b, str_len_b))
    {
        if (str_len_a == str_len_b){
            if (a_bigger(array_a, array_b, str_len_a)){
                subtraction(array_a, array_b, str_len_a, result);  // a-b
                for (int i = 0; i < str_len_a; i++){
                    array_a[i] = result[i]; // A = A - B
                }
                
            }
            else{  // B >= A
                subtraction(array_b, array_a, str_len_a, result);
                for (int i = 0; i < str_len_a; i++){
                    array_b[i] = result[i]; // B = B - A
                }
            }
        }
        if (str_len_a > str_len_b){
            int diff_len_ab = str_len_a - str_len_b;
            make_zero(array_b, diff_len_ab, str_len_a);  // add zero to b
            subtraction(array_a, array_b, str_len_a, result);  // a-b
            for (int i = 0; i < str_len_a; i++){
                array_a[i] = result[i]; // A = A - B = result
            }
            str_len_b = str_len_a;
        }       
        if (str_len_a < str_len_b){
            int diff_len_ab2 = str_len_b - str_len_a;  
            make_zero(array_a, diff_len_ab2, str_len_b); // add zero to a
            subtraction(array_b, array_a, str_len_b, result);  // b-a
            for (int i = 0; i < str_len_b; i++){
                array_b[i] = result[i]; // B = B - A = result
            } 
            str_len_a = str_len_b;
        }
    }    
    int j = 0;
    while (array_a[j] == 0){
        j++;
        if (j > str_len_a - 1){
            break;
        }
    }
    for (int i = j; i < str_len_a; i++){
        printf("%d", array_a[i]);
    }
    return 0;
}
