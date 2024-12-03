# Singleton

## Categoria
Padrão Criacional

## Objetivo
O padrão Singleton garante que uma classe tenha apenas uma instância e fornece um ponto global de acesso a ela. Esse padrão é útil para situações em que é necessário um controle centralizado de recursos, como configurações globais ou conexões com banco de dados.

## Funcionamento
O Singleton utiliza uma instância estática compartilhada entre todos os usuários da classe. Ele impede que novas instâncias sejam criadas e fornece acesso à instância única através de um método ou propriedade global.

## Aplicação
- Gerenciamento de configurações globais.
- Loggers centralizados para monitoramento do sistema.
- Controle de conexões com bancos de dados ou servidores.
- Gerenciamento de cache ou filas de mensagens.

## Pontos Fortes
- **Controle único**: Garante que apenas uma instância da classe exista em todo o sistema.
- **Economia de recursos**: Evita a criação de múltiplas instâncias desnecessárias.
- **Fácil acesso**: Proporciona um ponto global para acessar a instância.

## Pontos Fracos
- **Acoplamento global**: O uso excessivo do Singleton pode levar a dependências globais, dificultando a manutenção e os testes do sistema.
- **Dificuldade em testes unitários**: Simular diferentes instâncias em ambientes de teste pode ser desafiador.
- **Potencial gargalo**: Em sistemas multithread, a sincronização da instância única pode causar problemas de desempenho.

## Utilização em APIs e Frameworks
O Singleton é amplamente utilizado em bibliotecas e APIs de diversas linguagens de programação:
- **Python**: O módulo `logging` utiliza Singleton para gerenciar logs globais de forma eficiente.
- **Java**: A classe `Runtime` implementa Singleton para gerenciar o ambiente de execução da JVM.
- **C#**: O `HttpClient` do .NET é usado como Singleton para reutilizar conexões e evitar sobrecarga de recursos.

## Conclusão
O Singleton é um padrão ótimo, mas precisa ser usado com cuidado. Ele é ideal para cenários específicos, como gerenciar configurações ou conexões, mas não deve ser aplicado indiscriminadamente. Em projetos complexos, o abuso do Singleton pode dificultar a manutenção e a evolução do código.


## Sobre os Códigos

No projeto, criei dois exemplos para demonstrar a diferença entre um programa **sem usar o Singleton** e outro **com o Singleton**.

- **`sem_singleton.py`**: Mostra o problema de criar várias instâncias independentes, o que pode causar inconsistências nos dados.
- **`singleton.py`**: Resolve o problema garantindo que apenas uma instância da classe seja usada, compartilhando os mesmos dados.

Execute os dois códigos para entender como o Singleton funciona na prática:

### Sem Singleton
```bash
python sem_singleton.py

### Com Singleton
```bash
python singleton.py


