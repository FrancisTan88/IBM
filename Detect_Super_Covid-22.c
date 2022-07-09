#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct disjointSet{
    // TODO: Determine fields to use by your method
    int parent;
    int size;
} DisjointSet;

DisjointSet ds[1 << 24];
bool set[1 << 24] = {};

int c2i(char c) { 
    if ('0' <= c && c <= '9') return c - '0';
    else if ('a' <= c && c <= 'z') return c - 'a' + 10;
    else if ('A' <= c && c <= 'Z') return c - 'A' + 36;
    return -1;
}

int hash(const char *s) { 
    int ret = 0;
    int mask = (1<<24)-1; //好想喝大冰奶
    int len = strlen(s);
    for (int i = 0; i < len; i++)
        ret = mask & (ret << 4) | c2i(s[i]);
    return ret;
}

void makeset(const char *s){
    // TODO: Initialize a set with hash value
    int hash_val = hash(s);
    ds[hash_val].parent = hash_val; //一開始的parent都是自己
    ds[hash_val].size = 1;
}

inline int static init(const char *s) {
    int i = hash(s);
    if (!set[i]) {
        makeset(s);
        set[i] = 1;
    }
    return i;
}

int find_set(int hash_s) {
    // int hash_s = init(s);
    // TODO: Implement your find algorithm here
    if(ds[hash_s].parent != hash_s){
        ds[hash_s].parent = find_set(ds[ds[hash_s].parent].parent);
    }
    return ds[hash_s].parent;
}

void group(int hash_val1, int hash_val2) {
    int a = find_set(hash_val1), b = find_set(hash_val2);
    // TODO: Implement your union algorithm here

    if(a == b) return;

    if(ds[a].size > ds[b].size){ //b join a
        ds[b].parent = ds[a].parent;
        ds[a].size += ds[b].size;
    }
    else if(ds[a].size < ds[b].size){ //a join b
        ds[a].parent = ds[b].parent;
        ds[b].size += ds[a].size;
    }
    else{
        ds[a].parent = ds[b].parent; //whatever
        ds[b].size *= 2;
    }

}

bool same_set(int a, int b) {
    // TODO: Implement your algorithm here
    if(find_set(a) == find_set(b)){
        return true;
    }
    else{
        return false;
    }
    
}

int main(void) {
    // TODO: Implement your algorithm here
    int N;
    scanf("%d", &N);

    char input1[6];
    int answer[N];
    int index = 0;
    memset(input1, 0, sizeof(input1));
    memset(answer, 0, sizeof(answer));
    for(int i = 0; i < N; i++){
        char *input2 = (char *)calloc(13,sizeof(char));
        char *input3 = (char *)calloc(13,sizeof(char));
        scanf("%s", input1);
        scanf("%s", input2);
        scanf("%s", input3);
        int len_input1 = strlen(input1);
        int hash2 = init(input2);
        int hash3 = init(input3);
        if(len_input1 == 5){
            group(hash2, hash3);
        }
        else if(len_input1 == 4){
            if(hash2 == hash3){
                answer[index] = 1;
                index++;
            }
            else if(same_set(hash2, hash3)){
                answer[index] = 1;
                index++;
            }
            else{
                answer[index] = -1;
                index++;
            }
        }       
    }

    index = 0;
    while(answer[index] != 0){
        if(answer[index] == 1){
            printf("%s\n", "Positive");
        }
        else{
            printf("%s\n", "Negative");
        }
        index++;
    }

    return 0;
}