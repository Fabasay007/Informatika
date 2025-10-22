#include <iostream>
#include <set>

bool startsWithOne(int number) {
  return (number / 10 == 0 && number == 1) || (number >= 10 && number < 20);
}

void tog(const std::set<int>A,const std::set<int>B){
  std::set<int> together;
  for (const int &value : A) {
    if (B.find(value) != B.end() && startsWithOne(value)) {
        together.insert(value);
    }
}
for (const int &value : together) {
    std::cout << value << " ";
}

}



int main() {
    std::set<int> A; 
    std::set<int> B; 
     
    int sizeA, sizeB;
    std::cin >> sizeA;

    for (int i = 0; i < sizeA; ++i) {
        int el;
        std::cin >> el;
        A.insert(el);
    }

    std::cin >> sizeB;

    for (int i = 0; i < sizeB; ++i) {
        int el;
        std::cin >> el;
        B.insert(el);
    }

  tog(A,B);

    return 0;
}


  