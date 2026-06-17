#include <iostream>
using namespace std;

int main() {
    int limite;
    
    // Validação da entrada (garante que está entre 50 e 100)
    do {
        cout << "Digite um numero limite entre 50 e 100: ";
        cin >> limite;
    } while (limite < 50 || limite > 100);
    
    int termo1 = 0, termo2 = 1, proximoTermo = 0;
    
    cout << "Sequencia de Fibonacci ate " << limite << ":\n";
    
    // Exibe o primeiro termo se ele respeitar o limite
    cout << termo1 << " ";
    
    // Gera e exibe os próximos termos enquanto não passarem do limite
    proximoTermo = termo1 + termo2;
    while (proximoTermo <= limite) {
        cout << proximoTermo << " ";
        termo1 = termo2;
        termo2 = proximoTermo;
        proximoTermo = termo1 + termo2;
    }
    cout << endl;
    
    return 0;
}
