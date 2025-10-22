#include <iostream>  
#include <vector>

void more( const int* arrA, int t, int size){
  std::vector<int> B;
  for(int i = 0; i < size; ++i) {  
    if (arrA[i]>t){
      B.push_back(arrA[i]);
    }

  }
  for (int val: B) {
    std::cout<<val<<' ';

  }
}

int main() {  
    
    int t;
    const int size = 10;  
    int A[size];  
    std::cout << "Введите " << size << " целых чисел:\n"; 
    std::cin>>t;

    for(int i = 0; i < size; ++i) {  
        std::cin >> A[i]; 
       
    }  
    more(A,t,size);
    return 0;  
}






    
