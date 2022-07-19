#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct node{
  int city;
  struct node *next;
} Node;

Node *SetUpNode(int c) {
  Node *newNode = malloc(sizeof(Node));
  newNode->city = c;
  newNode->next = NULL;
  return newNode;
}

typedef struct graph {
  int nodes_amount;
  Node **adjLists;
} Graph;

Graph *SetUpGraph(int num_nodes) {
    Graph *graph = malloc(sizeof(Graph));
    graph->nodes_amount = num_nodes;
    graph->adjLists = malloc(num_nodes * sizeof(Node *));

    for (int i = 0; i < num_nodes; i++)
        graph->adjLists[i] = NULL;

    return graph;
}

void BuildRoad(Graph *graph, int c1, int c2) {
    Node *newNode = SetUpNode(c2);
    newNode->next = graph->adjLists[c1-1];
    graph->adjLists[c1-1] = newNode;

    newNode = SetUpNode(c1);
    newNode->next = graph->adjLists[c2-1];
    graph->adjLists[c2-1] = newNode;
}

// fill the answers "from R to S" on query_arr 
bool query_SR_ans(int resort, Graph *the_graph, int current, bool *visited, bool *sr_path){
    sr_path[current-1] = true;
    
    if (visited[current-1]){return false;}
    visited[current-1] = true;

    if (current == resort){return true;}

    Node *tra_node = the_graph->adjLists[current-1]; // tra_node : (1)city (2)next
    while(tra_node){
        if (query_SR_ans(resort, the_graph, tra_node->city, visited, sr_path)){
            return true;
        }
        tra_node = tra_node->next;
    }
    sr_path[current-1] = false;
    return false;
}

void query_SRother_ans(int sr_path_node, int current, Graph *the_graph, int *query_arr ){
    Node *tra_adj_node = the_graph->adjLists[current];

    while(tra_adj_node){
        if(query_arr[(tra_adj_node->city)-1] != 0){ //already in the SR path
            tra_adj_node = tra_adj_node->next;
            continue;
        }
        
        //other 
        query_arr[(tra_adj_node->city)-1] = sr_path_node;
        query_SRother_ans(sr_path_node, (tra_adj_node->city)-1, the_graph, query_arr);
        tra_adj_node = tra_adj_node->next;
    }
}

int main(void) {
    int N;
    int Q;
    int S;
    int R;
    scanf("%d", &N);
    scanf("%d", &Q);
    scanf("%d", &S);
    scanf("%d", &R);

    Graph *graph = SetUpGraph(N);    
    for (int i = 0; i < N-1; i++){
        int c1, c2;
        scanf("%d", &c1);
        scanf("%d", &c2);
        BuildRoad(graph, c1, c2);   
    }
    
    int query_arr[N];
    memset(query_arr, 0, sizeof(query_arr));

    bool visited_arr[N];
    bool sr_path[N];
    memset(visited_arr, 0, sizeof(visited_arr));
    memset(sr_path, 0, sizeof(sr_path));

    // the answer would be all R(or S) if S == R
    int query;
    if(S == R){
        for(int i = 0; i < N; i++){
            query_arr[i] = R;
        }
        for(int i = 0; i < Q; i++){
            scanf("%d", &query);
            printf("%d\n", query_arr[query-1]);
        }
    }
    else{
        // fill up the answer
        if(query_SR_ans(R, graph, S, visited_arr, sr_path)){
            for (int i = 0; i < N; i++){
                if(sr_path[i] == true){
                    query_arr[i] = i+1;
                }
            }
            for(int i = 0; i < N; i++){
                if(query_arr[i] != 0){
                    query_SRother_ans(i+1, i, graph , query_arr);
                }
            }
        }
        for (int i = 0; i < Q; i++){
            scanf("%d", &query);
            printf("%d\n", query_arr[query-1]);
        }
    }
    return 0;
}