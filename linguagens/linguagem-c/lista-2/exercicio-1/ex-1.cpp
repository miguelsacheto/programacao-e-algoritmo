#include <iostream>
int main() {
    int numero;
    int soma = 0;
    std::cout << "insira um numero inteiro:";
    std::cin >> numero;
    bool(true);
    int i=1;

    while(i <= numero) {
        if (i % 2 != 0){
            
            soma = soma + i;
    
        
    }
    
    i++;
    }
    std::cout << "A soma dos impares eh: " << soma << std::endl;
    
    return 0;
}
