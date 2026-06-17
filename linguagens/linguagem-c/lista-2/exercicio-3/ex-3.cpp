// Online C++ compiler to run C++ program online
#include <iostream>

    int main() {
    float altura;
    float genero;
    float pesoideal;
    
    std::cout <<"genero (1 para homem/2 para mulher):";
    std::cin >> genero;
    std::cout << "insira a sua altura";
    std::cin >> altura;
    if (genero == 1) {
        pesoideal=72,7 * altura - 58; 
    } 
    else if(genero == 2) {
       pesoideal=62,1 * altura - 44,7;
    }
    std::cout <<"seu peso ideal é:" << pesoideal << std::endl;
    return 0;
}
