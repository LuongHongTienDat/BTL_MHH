#include <iostream>
#include <vector>
#include <exception>
#include <utility>
#include <string>
#include <map>


using namespace std;


class Place{
public:
    string name;
    int tokenNumber;
    Place():name(""),tokenNumber(0){}
    Place(string na, int to):name(na),tokenNumber(to){}
};

class Transition{
public:
    vector<Place*> inputplace;
    vector<Place*> outputplace;

    Transition(): inputplace({}),outputplace({}) {}
    Transition(vector<Place*> inputplace,vector<Place*> outputplace){
        this->outputplace=outputplace;
        this->inputplace=inputplace;
    }
    bool fire(){
        int numberOfInput= inputplace.size(), numberOfOutput=outputplace.size();
        for (int i=0;i<numberOfInput;i++){
            if (inputplace[i]->tokenNumber<1) return false;
        }
        for (int i=0;i<numberOfInput;i++){
            inputplace[i]->tokenNumber--;
        }
        for (int i=0;i<numberOfOutput;i++){
            outputplace[i]->tokenNumber++;
        }
        return true;
    }
};

class PetriNet{
public:
    map<string,Transition*> transMap;
    vector <Place*> placeSet;
    PetriNet(){
        transMap={};
        placeSet={};
    }

    void printCurrentMarking(){
        int numberOfPlace=placeSet.size();
        cout<<"[";
        for (int i=0;i<numberOfPlace;i++){
            if (i==0){
                cout<<placeSet[i]->name<<"."<<placeSet[i]->tokenNumber;
            }
            else cout<<", "<<placeSet[i]->name<<"."<<placeSet[i]->tokenNumber;
        }
        cout<<"]\n";
    }
};

int main()
{
    // Khoi tao Petri Net:
    Place free("Free",0),busy("Busy",0),docu("Docu",0);

    Transition start({&free},{&busy});
    Transition change({&busy},{&docu});
    Transition end({&docu},{&free});

    PetriNet    SpecialistNet= PetriNet();
    SpecialistNet.transMap.insert(pair<string,Transition*>("start",&start));
    SpecialistNet.transMap.insert(pair<string,Transition*>("change",&change));
    SpecialistNet.transMap.insert(pair<string,Transition*>("end",&end));
    SpecialistNet.placeSet={&free,&busy,&docu};

    //////////////////////
    cout << "Format: {x.free, y.busy, z.docu}\n";
    int x,y,z;
    cout<<" Enter x: "; cin>>x;
    cout<<" Enter y: "; cin>>y;
    cout<<" Enter z: "; cin>>z;
    free.tokenNumber=x;
    busy.tokenNumber=y;
    docu.tokenNumber=z;

    string cmd;
    cout<<endl<<"Enter transition that you want to fire OR enter \"END\" to exit:\n";
    cin>>cmd;


    while (cmd!="END"){
        if (cmd!="start" && cmd!="change" && cmd!="end"){
            cout<<cmd<<" is not a transition"<<endl;
        }
        else {
            if (SpecialistNet.transMap[cmd]->fire()){
                cout<<"Marking obtained after firing:\n";
                SpecialistNet.printCurrentMarking();
            }
            else {
                cout<<cmd<<" is not currently enabled"<<endl;
            }
        }
        cout<<endl<<"Enter transition that you want to fire OR enter \"END\" to exit:\n";
        cin>>cmd;
    }
    return 0;
}
