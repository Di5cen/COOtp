#include<iostream>
#include<string.h>
#include<cpr/cpr.h>

using namespace std ;



class Departement
{
    private:
    int numero;
    float prix_departement;
    
    public:
    Departement()
    {
        numero = 1;
        prix_departement = 2;
    }

    void Afficher()
    {
        cout << "le numero est:"<< numero << " "<< "prix est:" << prix_departement << endl;
    }


};


int main()
{
    Departement d1;
    d1.Afficher();
    cpr::Response r = cpr::Get(cpr::Url{"http://127.0.0.1:8000/departement/1/"});
    if (r.status_code == 200) {
        cout << "HTTP 请求成功！" << endl;
        cout << "响应内容：" << r.text << endl;
    } else {
        cerr << "HTTP 请求失败。错误码：" << r.status_code << endl;
        cerr << "错误信息：" << r.error.message << endl;
    }

    return 0;
}
