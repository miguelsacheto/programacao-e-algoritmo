#include <iostream>
using namespace std;

int main() {
    double numero, soma = 0, multiplicacao = 1; 
    
    cout << "Digite numeros sucessivamente (o programa para quando a soma passar de 100):\n";
    
    while (soma <= 100) {
        cin >> numero;
        
        soma += numero;
        multiplicacao *= numero;
    }
    
    cout << "A soma total passou de 100 (Total: " << soma << ")." << endl;
    cout << "O resultado da multiplicacao de todos os numeros lidos eh: " << multiplicacao << endl;
    
    return 0;
}
