#include <iostream>
using namespace std;
// union (nghĩa là hợp) là kiểu dữ liệu đặc biệt cho phép nhiều biến chia sẻ cùng một vùng nhớ.
// Nói cách khác:
// Trong một union, tất cả các thành viên dùng chung cùng một ô nhớ, nên tại một thời điểm chỉ có thể lưu trữ một giá trị duy nhất.

union Data {
    int i;
    float f;
    char c;
};

int main(){
    Data x;
    x.i = 10; // gán x.i = 10
    x.f = 2.1; // gán típ x.f = 2.1 -> đè lên vùng nhớ của x.i dấn đến giá trị x.i bị xáo trộn 
    cout << x.i << endl;
    cout << x.f << endl;
    x.i = 100;
    cout << x.i << endl; // ngược lại
    cout << x.f << endl;
    cout << typeid(x.i).name() << endl; // i
    cout << typeid(x.f).name() << endl; // f
    cout << typeid(x).name() << endl; // 4Data
    cout << endl;
}