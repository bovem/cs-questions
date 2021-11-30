#include <iostream>

using namespace std;

class Node{
    public:
        int value;
        Node *next;

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

        }

        void show(){

        }

        void remove(int value){

        }

};

int main(){
    return 0;
}