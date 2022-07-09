#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// node: inputs
typedef struct node{
  char instruction;
  int first;
  int second;
} Node;

Node *SetUpNode(char instruction, int first, int second){
  Node *newNode = (Node *)malloc(sizeof(Node));
  newNode->instruction = instruction;
  newNode->first = first;
  newNode->second = second;
  return newNode;
}

// boom: linked list of what day to go
typedef struct boom{
    int day;
    struct boom *next;
} Boom;

Boom *SetUpBoom(int day){
    Boom *newBoom = (Boom *)malloc(sizeof(Boom));
    newBoom->day = day;
    newBoom->next = NULL; 
    return newBoom;
}

// disjoint set
typedef struct disjoint_set{
    int parent;
    int rank;
} DisjointSet;

typedef struct insert{
    int root_insert;
    int root_rank_var;
} Insert;

Insert *SetUpInsert(int root_insert, int root_rank ){
    Insert *new_insert = (Insert *)malloc(sizeof(Insert));
    new_insert->root_insert = root_insert;
    new_insert->root_rank_var = root_rank;
    return new_insert;
}

void MakeSet(int shop, DisjointSet **arr_disjoint, bool *arr_set){
    if(arr_set[shop] == true) return;

    else if(arr_set[shop] == false){
        DisjointSet *newSetNode = (DisjointSet *)malloc(sizeof(DisjointSet));
        newSetNode->parent = shop;
        newSetNode->rank = 1;
        arr_disjoint[shop] = newSetNode;
        arr_set[shop] = true;
    }
}

int find_root(int shop, DisjointSet **arr_disjoint){
    if(arr_disjoint[shop]->parent != shop){
        return find_root(arr_disjoint[shop]->parent, arr_disjoint);
    }
    return arr_disjoint[shop]->parent;
}

bool Union(int shop1, int shop2, DisjointSet **arr_disjoint, Insert **arr_insert, int current_day){
    int root1 = find_root(shop1, arr_disjoint);
    int root2 = find_root(shop2, arr_disjoint);
    if(root1 == root2){   //ineffective merge
        Insert *new_insert = SetUpInsert(0, 0);
        arr_insert[current_day] = new_insert;
        return false;
    }
    if(arr_disjoint[root1]->rank > arr_disjoint[root2]->rank){  //1 > 2
        arr_disjoint[root2]->parent = root1;
        Insert *new_insert = SetUpInsert(root2, 0);
        arr_insert[current_day] = new_insert;
        return true;
    }
    else if(arr_disjoint[root1]->rank < arr_disjoint[root2]->rank){  //1 < 2
        arr_disjoint[root1]->parent = root2;
        Insert *new_insert = SetUpInsert(root1, 0);
        arr_insert[current_day] = new_insert;
        return true;
    }
    else{
        arr_disjoint[root2]->parent = root1;  //一樣大的話2插1
        arr_disjoint[root1]->rank += 1;
        Insert *new_insert = SetUpInsert(root2, root1);
        arr_insert[current_day] = new_insert;
        return true;
    }
}

int Traverse(Node **arr_input, Boom **arr_head, DisjointSet **arr_disjoint, int *arr_ans, Insert **arr_insert, bool *arr_set, bool boomING, int num_shop, int total_day, int current_day, int first_b){
    current_day++;
    while(current_day <= total_day && arr_input[current_day]->instruction != 'b'){
        if(arr_input[current_day]->instruction == 'm'){
            int shop1 = arr_input[current_day]->first;  //i
            int shop2 = arr_input[current_day]->second;  //j
            MakeSet(shop1, arr_disjoint, arr_set);
            MakeSet(shop2, arr_disjoint, arr_set);
            if(Union(shop1, shop2, arr_disjoint, arr_insert, current_day)){
                num_shop--;
            }
        }
        else if(arr_input[current_day]->instruction == 'q'){
            arr_ans[current_day] = num_shop; 
        }

        // if boom day
        if(arr_head[current_day] != NULL){
            boomING = true;
            Boom *list_boom_day = arr_head[current_day];
            while(list_boom_day){
                num_shop = Traverse(arr_input, arr_head, arr_disjoint, arr_ans, arr_insert, arr_set, boomING, num_shop, total_day, list_boom_day->day, first_b);
                list_boom_day = list_boom_day->next;
            }
        }
        current_day++;
    }
    //fix it
    if(boomING == true && current_day != first_b){
        current_day--;
        while(arr_input[current_day]->instruction != 'b'){
            if(arr_input[current_day]->instruction == 'm' && arr_insert[current_day]->root_insert != 0){
                int cut_root = arr_insert[current_day]->root_insert;
                arr_disjoint[cut_root]->parent = cut_root;
                num_shop++;
            }
            if(arr_input[current_day]->instruction == 'm' && arr_insert[current_day]->root_rank_var != 0){
                int rank_root = arr_insert[current_day]->root_rank_var;
                arr_disjoint[rank_root]->rank -= 1;
            }
            current_day--;
        }
    }
    return num_shop;
}

int main(void){
    int N, M;
    scanf("%d", &N);
    scanf("%d", &M);

    char instruction[6];
    int first, second;
    int first_b;
    bool if_first_b = true;
    Node *arr_input[M+1]; 
    memset(arr_input, 0, sizeof(arr_input));

    Node *start_node = SetUpNode('s', 0, 0);   //start: (0, 0)
    arr_input[0] = start_node;  // the zero day
    for(int i = 1; i <= M; i++){
        scanf("%s", instruction);
        if(instruction[0] == 'm'){  //merge: (i, j)
            scanf("%d", &first);
            scanf("%d", &second);
        }
        if(instruction[0] == 'b' && if_first_b){
            first_b = i;
            if_first_b = false;
        }
        if(instruction[0] == 'b'){  //boom: (i, -1)
            scanf("%d", &first);
            second = -1;
        }
        if(instruction[0] == 'q'){   //query: (-2, -2)
            first = -2;
            second = -2;
        }
        Node *newNode = SetUpNode(instruction[0], first, second);
        arr_input[i] = newNode;
    }
    ///////////////////////store inputs into arr_input[M]//////////////////////////////

    Boom *arr_boom[M+1];
    Boom *head[M+1];
    memset(arr_boom, 0, sizeof(arr_boom));
    memset(head, 0, sizeof(head));
    int back_day, current_day;
    for(int i = 0; i <= M; i++){
        if(arr_input[i]->instruction == 'b'){  //boom
            current_day = i;
            back_day = arr_input[i]->first;
            while(arr_input[back_day]->instruction == 'b'){  //still boom
                back_day = arr_input[back_day]->first;
            }   
            
            Boom *new_Boom = SetUpBoom(current_day);
            if(arr_boom[back_day] != NULL){
                arr_boom[back_day]->next = new_Boom;
                arr_boom[back_day] = new_Boom;
            }
            else{
                head[back_day] = new_Boom;
                arr_boom[back_day] = new_Boom;
            } 
        }
    }
    ///////////////////////create commanding table//////////////////////////////

    //tell if the shop is already set
    bool set[N+1];
    for(int i = 0; i <= N; i++){
        set[i] = false;
    }

    DisjointSet *arr_disjoint[N+1];
    Insert *arr_insert[M+1];
    int arr_ans[M+1];
    memset(arr_disjoint, 0, sizeof(arr_disjoint));
    memset(arr_ans, 0, sizeof(arr_ans));
    memset(arr_insert, 0, sizeof(arr_insert));
    int num_shop = N;
    bool boomING = false;
    int random = Traverse(arr_input, head, arr_disjoint, arr_ans, arr_insert, set, boomING, num_shop, M, -1, first_b);
    int tmp = 0;
    while(tmp <= M){
        if(arr_ans[tmp] > 0){
            printf("%d\n", arr_ans[tmp]);
        }
        tmp++;
    }
    return 0;
    ////
}
