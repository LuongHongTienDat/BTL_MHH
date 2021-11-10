#include <iostream>
#include <vector>
#include <exception>
#include <utility>
#include <string>

using namespace std;

void exp(const int &x)
{
    if (x < 0 || x > 10)
        throw "Exception: The number of patients must be from 0 to 10!!!";
}
void problem_1()
{
    cout << "Format: {x.wait, y.inside, z.done}\nInput the number of patients in place \"wait\" : ";
    int x;
    cin>>x;
 /*   cout<<"Input the number of patients in place \"inside\" : ";
    int y;
    cin>>y;
    cout<<"Input the number of patients in place \"done\" : ";
    int z;
    cin>>z; */
    vector<pair<string, int>> marking_N;
    marking_N.push_back({"wait", x});
    marking_N.push_back({"inside", 0});
    marking_N.push_back({"done", 0});
    string str="";
    for(int i = 0 ; i < 2*x + 1 ; ++i){
        cout << "Firing sequence: [" << str << "]\nMarking: [";
        for (int i = 0; i < 3; i++){
            if (i != 2) cout << marking_N[i].first << "." << marking_N[i].second << ", ";
            else cout << marking_N[i].first << "." << marking_N[i].second << "]\n\n";
        }
        if (i % 2 == 0){
            if(i==0)str+="start";
            else str+=",start";
            marking_N[0].second--;
            marking_N[1].second++;
        }
        else{
            str+=",change";
            marking_N[1].second--;
            marking_N[2].second++;
        }
    }
}
void problem_4()
{
    cout << "Format: {x.wait, 0.inside, 0.done, 1.free, 0.busy, 0.docu}\nInput the number of patients x: ";
    int n;
    try
    {
        cin >> n;
        exp(n);
    }
    catch (const char* mess)
    {
        cout << mess << '\n';
        return;
    }
    vector<pair<string, int>> marking_N;
    marking_N.push_back({"wait", n});
    marking_N.push_back({"inside", 0});
    marking_N.push_back({"done", 0});
    marking_N.push_back({"free", 1});
    marking_N.push_back({"busy", 0});
    marking_N.push_back({"docu", 0});
    string str = "";

    for (int i = 0; i < n * 3 + 1; i++)
    {
        cout << "Firing sequence: [" << str << "]\nMarking: [";
        for (int i = 0; i < 6; i++)
            if (i != 5) cout << marking_N[i].first << "." << marking_N[i].second << ", ";
            else cout << marking_N[i].first << "." << marking_N[i].second << "]\n\n";

        if (!(i % 3))
        {
            marking_N[0].second--;
            marking_N[3].second--;
            marking_N[1].second++;
            marking_N[4].second++;
        }

        else if (i % 3 == 1)
        {
            marking_N[1].second--;
            marking_N[4].second--;
            marking_N[2].second++;
            marking_N[5].second++;
        }

        else
        {
            marking_N[5].second--;
            marking_N[3].second++;
        }

        str += str.empty()? "start" : (i % 3 == 0)? ",start" : (i % 3 == 1)? ",change" : ",end";
    }
}

int main()
{
    problem_1();
    return 0;
}