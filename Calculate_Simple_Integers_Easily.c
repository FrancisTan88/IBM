#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <math.h>

#define SIZE 100000
#define LEN_DIGIT 30


int comparison_stack(char stack[SIZE], char *ptr){ // the order would be * / -> + - -> (   
    switch (stack[*ptr])
    {
    case '(':
        return 1;
    case '*': case '/': case '%':
        return 9;
    case '+': case '-':
        return 8;
    default:
        return -3; 
    }
}

int comparison_token(char token){
    switch (token)
    {
    case '*': case '/': case '%':
        return 8;
    case '+': case '-':
        return 7;
    default:
        return 1; // this suppose not to be return
    }
}

void push(char stack[SIZE], char *ptr, char token){
    *ptr += 1;
    stack[*ptr] = token;
}

char pop(char stack[SIZE], char *ptr){
    char pop_value = stack[*ptr];
    *ptr -= 1;
    return pop_value;
}

long long negative_floor(long long num1, long long num2){
    long long result_floor = (num2 / num1) - 1;
    return result_floor;
}

void push_number(long long stack_num[SIZE], long long *ptr_num, long long number){
    *ptr_num += 1;
    stack_num[*ptr_num] = number;
}

long long pop_number(long long stack_num[SIZE], long long *ptr_num){
    long long pop_num = stack_num[*ptr_num];
    *ptr_num -= 1;
    return pop_num;
}


long long answer_calculator(char postfix[SIZE][LEN_DIGIT], long long post_position){
    long long stack_number[SIZE];
    long long stack_number_position = 0;
    long long cal_position = 0;

    long long initial_ptr_num = -1;
    long long *stack_number_ptr = &initial_ptr_num;

    long long number;
    long long pop_num_right;
    long long pop_num_left;
    long long result;
    long long final_result;

    while (cal_position < post_position){
        if ((postfix[cal_position][0] >= '0' && postfix[cal_position][0] <= '9') || (strlen(postfix[cal_position]) > 1)){ // consider the "negative" condition
            push_number(stack_number, stack_number_ptr, (long long)atoll(postfix[cal_position]));
        }
        
        else{
            if (postfix[cal_position][0] == '+'){
                pop_num_right = pop_number(stack_number, stack_number_ptr);
                pop_num_left = pop_number(stack_number, stack_number_ptr);
                result = pop_num_right + pop_num_left;
                push_number(stack_number, stack_number_ptr, result);
            }

            else if (postfix[cal_position][0] == '-'){
                pop_num_right = pop_number(stack_number, stack_number_ptr);
                pop_num_left = pop_number(stack_number, stack_number_ptr);
                result = pop_num_left - pop_num_right;
                push_number(stack_number, stack_number_ptr, result);
            }

            else if (postfix[cal_position][0] == '*'){
                pop_num_right = pop_number(stack_number, stack_number_ptr);
                pop_num_left = pop_number(stack_number, stack_number_ptr);
                result = pop_num_right * pop_num_left;
                push_number(stack_number, stack_number_ptr, result);
            }

            else if (postfix[cal_position][0] == '/'){   // consider the "floor" function
                pop_num_right = pop_number(stack_number, stack_number_ptr);
                pop_num_left = pop_number(stack_number, stack_number_ptr);

                if (((pop_num_right < 0 && pop_num_left > 0) || (pop_num_right > 0 && pop_num_left < 0)) && (pop_num_left % pop_num_right != 0)){
                    result = negative_floor(pop_num_right, pop_num_left);
                }
                else{
                    result = pop_num_left / pop_num_right;
                }
                push_number(stack_number, stack_number_ptr, result);
            }

            else if (postfix[cal_position][0] == '%'){
                pop_num_right = pop_number(stack_number, stack_number_ptr);
                pop_num_left = pop_number(stack_number, stack_number_ptr);
                result = pop_num_left % pop_num_right;
                push_number(stack_number, stack_number_ptr, result);
            }
        }
        cal_position++;
    }
    final_result = pop_number(stack_number, stack_number_ptr);
    printf("Print: %lld\n", final_result);
    return final_result;  // long long 
}

void infix_to_postfix(char infix[SIZE], char postfix[SIZE][LEN_DIGIT], char stack_operator[SIZE]){
    long long post_position = 0;
    long long infix_position = 0;
    long long len_infix = strlen(infix);
    long long digit_position = 0;
    long long catch_result;

    char initial_ptr = -1;
    char *stack_operator_ptr = &initial_ptr; //start from -1
    char token;
    char pop_ope;

    while (infix_position < len_infix){
        token = infix[infix_position];
        
        switch (token)
        {
        case '(':
            push(stack_operator, stack_operator_ptr, token);
            infix_position++;
            break;
        
        case ')':
            while (comparison_stack(stack_operator, stack_operator_ptr) != 1){
                pop_ope = pop(stack_operator, stack_operator_ptr);
                postfix[post_position][digit_position] = pop_ope;
                post_position++;
            }
            pop(stack_operator, stack_operator_ptr);
            infix_position++;
            break;

        case '+': case '-': case '*': case '/': case '%':
            while (comparison_stack(stack_operator, stack_operator_ptr) > comparison_token(token)){
                pop_ope = pop(stack_operator, stack_operator_ptr);
                postfix[post_position][digit_position] = pop_ope;
                post_position++;
            }
            push(stack_operator, stack_operator_ptr, token);
            infix_position++;
            break;
        
        case '=':
            while (comparison_stack(stack_operator, stack_operator_ptr) != -3) 
            {
                pop_ope = pop(stack_operator, stack_operator_ptr);
                postfix[post_position][digit_position] = pop_ope;
                post_position++;  
            }   
            // now the stack should be empty with the ptr points to address -1.            

            catch_result = answer_calculator(postfix, post_position); 

            for (int i = 0; i < post_position; i++){  // clean the postfix
                memset(postfix[i],0,LEN_DIGIT); 
            }

            post_position = 0;
            sprintf(&postfix[post_position][digit_position], "%lld", catch_result); // ll to char
            post_position++;
            infix_position++;  // finally, here, the outtest while loop should jump out
            break;   

        default: // is number
            while (token >= '0' && token <= '9'){
                postfix[post_position][digit_position] = token;
                digit_position++;
                infix_position++;
                token = infix[infix_position];
            }
            digit_position = 0;
            post_position++;
            break;
        }
    }
}

int main(void){
    char infix[SIZE];
    char postfix[SIZE][LEN_DIGIT];
    char stack_operator[SIZE];

    scanf("%s", infix);
    infix_to_postfix(infix, postfix, stack_operator);
}