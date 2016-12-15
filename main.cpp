#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>
using namespace std;

mutex m1,m2;
int x;

void threadFunction1()
{
    m2.lock();
    for( int i = 0; i < 1000003; ++i ) {
        x++;
    m2.unlock();
    }
}

void threadFunction2() {
    m1.lock();
    for (int i = 0; i < 1000000; ++i)
        if ((x % 2 == 0)) {
            std::cout << "x = " << x << std::endl;
        }
        m1.unlock();
}


int main()
{
    std::thread t1(threadFunction1);
    std::thread t2(threadFunction2);
    t1.join();
    t2.join();
    return 0;
}