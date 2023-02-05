#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;
struct point{
    float x;
    float y;
};
float dis(point a,point b){
    return sqrt((b.x-a.x)*(b.x-a.x)+(b.y-a.y)*(b.y-a.y));
}

int main(){
    point a,b,c;
    cin>>a.x>>a.y>>b.x>>b.y>>c.x>>c.y;
    float l;l=(dis(a,b)+dis(b,c)+dis(a,c));
    printf("%.2f",l);
    

    return 0;
}
