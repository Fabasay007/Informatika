#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>

bool startsWithOne(int number) {
  return (number / 10 == 0 && number == 1) || (number >= 10 && number < 20);
}

void tog(const std::set<int>A,const std::set<int>B){
  std::set<int> together;
  std::set_intersection(A.begin(), A.end(), B.begin(), B.end(), 
  std::inserter(together, together.begin()));

for (const int &value : together) {
  if (startsWithOne(value)){
    std::cout << value << " ";
  }
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


  