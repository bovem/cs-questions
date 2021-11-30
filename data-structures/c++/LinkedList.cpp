#include <iostream>

using namespace std;

class Node{
    public:
        int value;
        Node *next = NULL;

        Node() = default;
        Node(int value){
            this->value = value;
        }
};

class LinkedList{
    public:
        Node head;

        LinkedList() = default;
        LinkedList(Node head){
            this->head = head;
        }

        void append(int value){
            Node temp;
            temp.next = &(this->head);
            while(temp.next != NULL){
                temp = *(temp.next);
            }
            Node newNode = Node(value);
            temp.next = &newNode;
        }

        void show(){
            Node temp;
            temp.next = &(this->head);
            while(temp.next != NULL){
                temp = *(temp.next);
                cout<<temp.value<<endl;
            }
        }

        void remove(int value){

        }

};

int main(){
    Node n = Node(6);
    LinkedList ll = LinkedList(n);
    Node j = Node(7);
    Node k = Node(8);
    ll.head.next = &j;
    (ll.head.next)->next = &k;
    ll.append(89);
    //cout<<(ll.head.next)->value<<endl;
    ll.show();
    return 0;
}