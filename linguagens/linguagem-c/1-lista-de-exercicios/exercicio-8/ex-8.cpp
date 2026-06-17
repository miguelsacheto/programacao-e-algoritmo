#include <iostream>
using namespace std;

int main() {
    int numeroLimite, somaPares = 0, somaImpares = 0;
    
    cout << "Digite um numero inteiro: ";
    cin >> numeroLimite;
    
    for (int i = 0; i <= numeroLimite; i++) {
        if (i % 2 == 0) {
            somaPares += i; // 0 entra aqui, mas não altera a soma
        } else {
            somaImpares += i;
        }
    }
    
    cout << "Soma dos numeros pares de 0 ate " << numeroLimite << ": " << somaPares << endl;
    cout << "Soma dos numeros impares de 0 ate " << numeroLimite << ": " << somaImpares << endl;
    
    return 0;
}
