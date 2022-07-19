#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>

//Struct node
typedef struct node{
	int size;
	long long seconds;  
	int random;  //priority(優先順序)
	long long summation;
	int reverse_label;
	int update_label;
	struct node *left;
	struct node *right;
}Node;

Node *CreateNode(long long seconds){
	Node *NewNode = (Node*)malloc(sizeof(Node)); 
	NewNode->size = 1;
	NewNode->seconds = seconds;
	NewNode->random = rand();
	NewNode->summation = seconds;
	NewNode->reverse_label = 0;
	NewNode->update_label = 0;
	NewNode->left = NULL;
	NewNode->right = NULL;
	return NewNode;
}

void UpdateUp(Node *root){ 
	if(root != NULL){
        root->size = 1;
        root->summation = root->seconds;
        if(root->left != NULL){
            Node *tmp1 = root->left;
            root->summation += tmp1->summation;
            root->size += tmp1->size;
        }
        if(root->right != NULL){
            Node *tmp2 = root->right;
            root->summation += tmp2->summation;
            root->size += tmp2->size;
        }
    }
}

void Split(Node *root, int k, Node **left, Node **right){
	if(root == NULL){
		*left = NULL;
		*right = NULL;
	}
	else{
		if((root->left)->size < k){
			*left = root;
			Split(root->right, k - (root->left)->size - 1, &((*left)->right), &(*right));
		}
		else{
			*right = root;
			Split(root->left, k, &(*left), &((*right)->left));		
		}
		UpdateUp(root);
	}
}

Node *Merge(Node *left, Node *right){
	if(left == NULL){
		return right;
	}
	if(right == NULL){
		return left; 
	}
	if(right->random < left->random){  //根據上面Split: a一定在b的左邊, 而若a的random(priority)>b的, 代表b一定為a的right child
		left->right = Merge(left->right, right);
		UpdateUp(left);
		return left;
	}
	else{ //根據上面Split: a一定在b的左邊, 而若a的random(priority)<b的, 代表a一定為b的left child
		right->left = Merge(left, right->left);
		UpdateUp(right);
		return right;
	}
}

void Insertion(Node **root, long long seconds, int k){
	Node *left = NULL;
	Node *right = NULL;
    Node *tmp = CreateNode(seconds);
	Split(*root, k, &left, &right);
	*root = Merge(Merge(left, tmp), right);
}

void Summation(int l, int r, Node **result){
	if(result != NULL){
        Node* left = NULL;
        Node* middle = NULL;
        Node* right = NULL;
        Split(*result, l - 1, &left, &right);
        Split(right, r - (l - 1), &middle, &right);
        printf("%lld", middle->summation);
        *result = Merge(Merge(left, middle), right);
    }
}

int main(void){
    int N,Q;
	int operation;
	int l,r;
	int position;
	long long seconds;
    Node *result = NULL;
    scanf("%d", &N);
    scanf("%d", &Q);

    for(int i = 0; i < N; i++){
		scanf("%lld", &seconds);
		Insertion(&result, seconds, i);
	}
    
	for(int i = 0; i < Q; i++){
		scanf("%d", &operation);
		if(operation == 1){  //insert seconds after position
			scanf("%d", &position);
			scanf("%lld", &seconds);
			Insertion(&result, seconds, position);
		}
		else if(operation == 6){
			scanf("%d", &l);
			scanf("%d", &r);
			Summation(l, r, &result);
			printf("\n");
		}
	}

    

	return 0;
}