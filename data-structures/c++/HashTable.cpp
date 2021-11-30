#include <iostream>

using namespace std;

class Node{
    public:
        int value;
        int* next;

        Node();

        Node(int val){
            int value = val;
            int* next = NULL;
        }
};

class LinkedList{
    public:
        Node head;
    
        LinkedList(int val){
            Node head = Node(val);
        }
};

// class HashTable{

// };

int main(){
    LinkedList ll = LinkedList(3);
    return 0;
}