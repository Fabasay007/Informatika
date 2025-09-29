#include <iostream>
#include <cmath>
using namespace std;
#define PI 3.14159265
int main() {
    double par = 90;
    float x;
    float y;
    float R;
    float S;
    cin >> x ;
    cin >> y;
    R = sqrt(pow(x,2)+ pow(y,2))/pow(2,log2(x));
    S = x* tan(par* PI /180);
    cout<< R,S;
    int C = max(R,S);
    cout<< C;



}