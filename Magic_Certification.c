#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>
#define STR_SIZE 10000000

//reverse the original string
void create_reverse(char *string, int len_string, char *rev_string){
    int len_rev_string = len_string; // two length are equal
    for(int i = 0; i < len_rev_string; i++){
        if(len_string > 0){
            rev_string[i] = string[len_string-1];
            len_string--;
        }       
    }
}

int shortest_palindrome(char *string, char *rev_string, char *rev_without_match, char *ans_string, int len_string, int add_num){
    strcat(strcat(string, " "), rev_string);
    int len_string_cat = strlen(string);
    int arr_palindrome[len_string_cat];
    arr_palindrome[0] = 0;
    for (int i = 1; i < len_string_cat; i++){
        int tmp = arr_palindrome[i-1];
        while(tmp > 0 && string[i] != string[tmp]){
            tmp = arr_palindrome[tmp-1];
        }
        if(string[i] == string[tmp]){
            tmp++;
        }
        arr_palindrome[i] = tmp;
    }
    
    // rev_string without matching
    for(int i = 0; i < len_string - arr_palindrome[len_string_cat-1]; i++){
        rev_without_match[i] = rev_string[i];
    }
    add_num = strlen(rev_without_match);
    string[len_string] = '\0';
    strcat(rev_without_match, string);
    strcpy(ans_string, rev_without_match); //store the answer
    memset(rev_without_match, 0, 2*STR_SIZE); //clean the rev_without_match
    return add_num;

}


int main(void){
    char string[2*STR_SIZE+2];
    char rev_string[2*STR_SIZE+2];
    char rev_without_match[2*STR_SIZE];
    char ans_front[2*STR_SIZE];
    char ans_end[2*STR_SIZE];

    scanf("%s", string);
    int len_string = strlen(string);
    int add_num1;
    int add_num2;

    // reverse the input string
    create_reverse(string, len_string, rev_string); // reverse it

    // generate the shortest palindrome
    add_num1 = shortest_palindrome(string, rev_string, rev_without_match, ans_front, len_string, add_num1); // now we store add_num1 and ans_front
    add_num2 = shortest_palindrome(rev_string, string, rev_without_match, ans_end, len_string, add_num2);
    if (add_num1 < add_num2){
        printf("%d\n", add_num1);
        printf("%s\n", ans_front);
    }
    else if (add_num1 > add_num2){
        printf("%d\n", add_num2);
        printf("%s\n", ans_end);
    }
    else{
        if (add_num1==0 && add_num2==0){
            printf("%d\n", add_num1);
            printf("%s\n", ans_front);
        }
        else{
            printf("%d\n", add_num1);
            printf("%s\n", ans_front);
            printf("%s\n", ans_end);
        }
    }    
    char *check = add_num1 < add_num2?ans_front:ans_end;
    int check_len = strlen(check);
    for(int start=0,end=check_len-1;start<end;start++,end--){
        if(check[start]!=check[end]){
            printf("wrong answer");
        }
    }
    return 0;
}