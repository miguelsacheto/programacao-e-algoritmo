#include <iostream>
using namespace std;

int main() {
    int qtdPessoas;
    double altura, somaAlturas = 0;
    
    cout << "Digite a quantidade de pessoas: ";
    cin >> qtdPessoas;
    
    for (int i = 1; i <= qtdPessoas; i++) {
        cout << "Digite a altura da pessoa " << i << " (em metros): ";
        cin >> altura;
        somaAlturas += altura;
    }
    
    if (qtdPessoas > 0) {
        double media = somaAlturas / qtdPessoas;
        cout << "A altura media do grupo eh: " << media << " metros." << endl;
    } else {
        cout << "Nenhuma pessoa foi registrada." << endl;
    }
    
    return 0;
}
