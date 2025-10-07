#include <iostream>
using namespace std;


// enum dùng để định nghĩa ra một kiểu dữ liệu mới và tạo ra một danh sách các giá trị
// được cung cấp của kiểu dữ liệu đó
// các giá trị này có dạng là các hàng số nguyên


// Định nghĩa enum
enum color {RED, BLUE, YELLOW, GREEN} a, b, c;
enum {MAXVALUE = 1000, MINVALUE = 1};

int main(){
    int x = MAXVALUE;
    cout << x;
    
}