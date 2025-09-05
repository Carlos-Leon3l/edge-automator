# Microsoft Rewards Automator

Um projeto de automação em Python para otimizar a coleta de pontos no programa Microsoft Rewards através de buscas automáticas no Bing.

> ### ⚠️ ALERTA IMPORTANTE ⚠️
>
> Este projeto está **em desenvolvimento** e deve ser utilizado **apenas para fins educacionais e de teste**.
>
> A automação de tarefas para acumular pontos **viola os Termos de Serviço do Microsoft Rewards**. O uso deste script pode resultar na suspensão da sua pontuação ou no **banimento permanente da sua Conta Microsoft**.
>
> **NÃO UTILIZE SUA CONTA PRINCIPAL!** Crie e utilize uma conta Microsoft secundária, que não esteja vinculada a serviços importantes (como LinkedIn, Outlook, Xbox, etc.), para realizar seus testes. O autor não se responsabiliza por qualquer perda ou dano causado pelo uso deste software.

---

### Motivação

A ideia desse projeto nasceu de algo que estava se tornando cansativo: A necessidade de buscar palavra por palavra, todos os dias, apenas para acumular pontos no Microsoft Rewards e tedioso, um processo muito manual e lento.

Foi então que surgiu a "Se uma tarefa é repetitiva e cansativa, por que não automatizá-la?".

Este projeto é a resposta. Ele transforma um processo monótono em uma solução de um clique, servindo como um estudo prático e divertido sobre o Selenium para controlar navegadores, a importância de gerenciar perfis para uma automação segura e a simplicidade do Tkinter para criar interfaces funcionais. É a jornada de transformar um problema pessoal em uma solução automatizada.

### Estrutura dos Arquivos

O projeto é composto pelos seguintes arquivos principais:

* **`ui.py`**: Ponto de entrada da aplicação. Este arquivo cria a interface gráfica (GUI) utilizando a biblioteca `Tkinter`, permitindo que o usuário insira a quantidade de buscas desejada e inicie o processo.
* **`main.py`**: O coração da automação. Contém a função `inicializa_automator` que controla o Selenium, configura o navegador Microsoft Edge para usar um perfil específico, gera palavras aleatórias com a biblioteca `Faker` e executa o loop de buscas.
* **`requirements.txt`**: Lista todas as bibliotecas Python necessárias para que o projeto funcione. Facilita a instalação das dependências em um novo ambiente.
* **`.env`** (precisa ser criado): Arquivo de configuração local onde você armazenará os caminhos para o perfil do seu navegador, mantendo seus dados pessoais fora do código-fonte.
* **`.env.example`**: Modelo para o arquivo de configuração. Este arquivo serve como um gabarito para a criação do arquivo `.env`, demonstrando quais variáveis de ambiente são necessárias para a execução do projeto e em qual formato elas devem ser declaradas.


### Como Executar (Tutorial de Instalação)

Siga os passos abaixo para configurar e rodar o projeto em sua máquina local.

#### Passo 1: Clonar o Repositório

```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
```

#### Passo 2: Criar e Ativar um Ambiente Virtual (`venv`)

É uma boa prática isolar as dependências do projeto.

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

#### Passo 3: Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas listadas no `requirements.txt`.

```bash
pip install -r requirements.txt
```

#### Passo 4: Encontrar os Caminhos do Perfil do Microsoft Edge

Para que o script funcione sem interferir no seu navegador principal, ele precisa rodar em um perfil separado (recomenda-se criar um novo perfil no Edge apenas para isso).

1.  Abra o Microsoft Edge.
2.  Digite `edge://version/` na barra de endereços e pressione Enter.
3.  Você verá uma página com várias informações. Localize a linha **"Caminho do perfil"**.
4.  O caminho será algo como: `C:\Users\SeuUsuario\AppData\Local\Microsoft\Edge\User Data\Profile 2`

Deste caminho, você precisa de duas partes:
* **O diretório de dados do usuário**: `C:\Users\SeuUsuario\AppData\Local\Microsoft\Edge\User Data`
* **O diretório do perfil**: `Profile 2` (pode ser `Default` para o perfil principal).

#### Passo 5: Criar e Configurar o arquivo `.env`

1.  Na pasta raiz do seu projeto, crie um novo arquivo e nomeie-o exatamente como `.env`.
2.  Abra este arquivo e adicione as duas variáveis de ambiente com os caminhos que você encontrou no passo anterior.


#### Passo 6: Executar o Automatizador

Finalmente, execute o arquivo da interface gráfica para iniciar o programa.

```bash
python ui.py
```

Uma janela se abrirá. Escolha o número de buscas, clique em "Inicializar", e o processo começará.

### Status do Projeto

O projeto é funcional, mas está em sua fase inicial. Melhorias futuras planejadas incluem:
- [ ] Tornar as pausas entre as ações mais aleatórias para simular melhor o comportamento humano.
- [ ] Otimizar o uso de abas do navegador.
- [ ] Melhorar a seleção de palavras para garantir maior variedade a cada execução.
- [ ] Adicionar um tratamento de erros mais robusto.