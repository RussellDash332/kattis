// Ukkonen's suffix tree construction
// https://rosettacode.org/wiki/Talk:Ukkonen%E2%80%99s_suffix_tree_construction

#include <stdio.h> 
#include <string.h> 
#include <stdlib.h> 
#define MAX_CHAR 128
#define LIMIT 100002

struct SuffixTreeNode {
    struct SuffixTreeNode *children[MAX_CHAR];
    struct SuffixTreeNode *suffixLink;

    int start;
    int *end;
    int suffixIndex;
};

typedef struct SuffixTreeNode Node;

char text[LIMIT];
Node *root = NULL;
Node *lastNewNode = NULL;
Node *activeNode = NULL;

int activeEdge = -1;
int activeLength = 0;

int remainingSuffixCount = 0;
int leafEnd = -1;
int *rootEnd = NULL;
int *splitEnd = NULL;
int size = -1;

Node *newNode(int start, int *end) {
    Node *node = (Node*) malloc(sizeof(Node));
    for (int i = 0; i < MAX_CHAR; i++)
        node->children[i] = NULL;

    node->suffixLink = root;
    node->start = start;
    node->end = end;

    node->suffixIndex = -1;
    return node;
}

int edgeLength(Node *n) {
    if (n == root)
        return 0;
    return *(n->end) - (n->start) + 1;
}

int walkDown(Node *currNode) {
    if (activeLength >= edgeLength(currNode)) {
        activeEdge += edgeLength(currNode);
        activeLength -= edgeLength(currNode);
        activeNode = currNode;
        return 1;
    }
    return 0;
}

void extendSuffixTree(int pos) {
    leafEnd = pos;
    remainingSuffixCount++;
    lastNewNode = NULL;

    while (remainingSuffixCount > 0) {
        if (activeLength == 0)
            activeEdge = pos;

        if (activeNode->children[text[activeEdge]] == NULL) {
            activeNode->children[text[activeEdge]] = newNode(pos, &leafEnd);
            if (lastNewNode != NULL) {
                lastNewNode->suffixLink = activeNode;
                lastNewNode = NULL;
            }
        } else {
            Node *next = activeNode->children[text[activeEdge]];
            if (walkDown(next))
                continue;
            if (text[next->start + activeLength] == text[pos]) {
                if(lastNewNode != NULL && activeNode != root) {
                    lastNewNode->suffixLink = activeNode;
                    lastNewNode = NULL;
                }
                activeLength++;
                break;
            }

            splitEnd = (int*) malloc(sizeof(int));
            *splitEnd = next->start + activeLength - 1;

            Node *split = newNode(next->start, splitEnd);
            activeNode->children[text[activeEdge]] = split;
            
            split->children[text[pos]] = newNode(pos, &leafEnd); 
            next->start += activeLength; 
            split->children[text[next->start]] = next; 
            
            if (lastNewNode != NULL)
                lastNewNode->suffixLink = split;

            lastNewNode = split;
        }

        remainingSuffixCount--;
        if (activeNode == root && activeLength > 0) {
            activeLength--;
            activeEdge = pos - remainingSuffixCount + 1;
        } else if (activeNode != root) {
            activeNode = activeNode->suffixLink;
        }
    }
}

void setSuffixIndexByDFS(Node *n, int labelHeight) {
    if (n == NULL)
        return;
    int leaf = 1;
    for (int i = 0; i < MAX_CHAR; i++) {
        if (n->children[i] != NULL) {
            leaf = 0;
            setSuffixIndexByDFS(n->children[i], labelHeight + edgeLength(n->children[i]));
        }
    }
    if (leaf == 1) {
        n->suffixIndex = size - labelHeight;
    }
}

void freeSuffixTreeByPostOrder(Node *n) {
    if (n == NULL)
        return;
    for (int i = 0; i < MAX_CHAR; i++) {
        if (n->children[i] != NULL)
            freeSuffixTreeByPostOrder(n->children[i]);
    }
    
    if (n->suffixIndex == -1)
        free(n->end);
    free(n);
}

void buildSuffixTree() {
    size = strlen(text);
    rootEnd = (int*) malloc(sizeof(int));
    *rootEnd = - 1;

    root = newNode(-1, rootEnd);
    activeNode = root;
    for (int i = 0; i < size; i++)
        extendSuffixTree(i);
    int labelHeight = 0;
    setSuffixIndexByDFS(root, labelHeight);
}

void doTraversal(Node *n, int suffixArray[], int *idx) {
    if (n == NULL)
        return;
    int i = 0;
    if (n->suffixIndex == -1) {
        for (i = 0; i < MAX_CHAR; i++)
            if (n->children[i] != NULL)
                doTraversal(n->children[i], suffixArray, idx);
    } else if (n->suffixIndex > -1 && n->suffixIndex < size)
        suffixArray[(*idx)++] = n->suffixIndex;
}

void buildSuffixArray(int suffixArray[]) {
    for (int i = 0; i < size; i++)
        suffixArray[i] = -1;
    int idx = 0;
    doTraversal(root, suffixArray, &idx);
}

int main(int argc, char *argv[]) {
    int t, k;
    while (scanf("%[^\n]%*c", text) == 1) {
        strcat(text, ""); // char 1
        
        buildSuffixTree();
        size--;

        int suffixArray[strlen(text)];
        buildSuffixArray(suffixArray);

        if (scanf("%d", &t) == 1)
            t--;
        while (t--) {
            if (scanf("%d", &k) == 1)
            printf("%d ", suffixArray[k]);
        }
        if (scanf("%d\n", &k) == 1)
            printf("%d\n", suffixArray[k]);

        freeSuffixTreeByPostOrder(root);
    }
    return 0;
}