
#include <iostream>

int main() {
    int numero;
    int potencia;
    int resultado = 1;
    int i = 1;
   
    std::cout << "escreva um numero: ";
    std::cin >> numero;
    std::cout << "escreva uma potencia: ";
    std::cin >> potencia;
    
    
while (i <= potencia) {
    resultado = resultado * numero ;
    i++;
    
}
    std::cout << "seu resultado é " << resultado;
    return 0;
}
