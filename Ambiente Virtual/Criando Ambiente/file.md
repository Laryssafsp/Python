Um **ambiente virtual** é um espaço isolado dentro do seu sistema, onde você
pode instalar e gerenciar pacotes (ou dependências) de software de maneira
independente.

**Isolamento de projetos**: Cada projeto terá seus próprios
pacotes e bibliotecas, sem que afetem outros projetos.

**Reprodutibilidade**: garantem que ao compartilhar um projet
com outras pessoas, as mesmas versões de pacotes serão
utilizados.

**Prevenção de conflitos no Sistema Global**: instalações de
pacotes diretamente no sistema, pode acabar alterando o
funcionamento de outros programas que dependem desses
pacotes.

---

**Pacotes**: Conjuntos de código reutilizáveis que fornecem funcionalidades
específicas. No contexto do Python, pacotes são instalados via ferramentas
como pip e podem ser bibliotecas para realizar tarefas como requisições
HTTP, manipulação de dados, etc.

**Dependências**: São os pacotes que um projeto necessita para funcionar.
Quando um projeto usa um pacote externo, ele se torna uma dependência
desse projeto. Essas dependências devem ser gerenciadas para garantir que
a versão correta seja utilizada no momento correto.

**Pip**: Ferramenta padrão do Python para instalar pacotes. Com o pip, você pode instalar
qualquer biblioteca disponível no PyPI (Python Package Index), que é o repositório
oficial de pacotes para Python.

 Se o pip.exe estiver bloqueado, tente usar o pip via Python: `python -m pip install pandas`

**Venv**: Ferramenta nativa do Python para criar ambientes virtuais. Com o venv, você
pode configurar facilmente um ambiente isolado dentro do seu projeto. Ela faz parte da
instalação padrão do Python, o que facilita seu uso em diferentes sistemas operacionais

# **Passo a Passo: Configuração de Ambiente Virtual e requirements.txt**


## **1. Criar um Ambiente Virtual**

Um ambiente virtual é uma ferramenta que ajuda a manter as dependências do projeto isoladas do sistema global, garantindo que as versões de pacotes não conflitem entre projetos.

### **1.1 Instalar o virtualenv (se necessário)**
Se o virtualenv não estiver instalado, você pode instalá-lo com o seguinte comando:

```bash
pip install virtualenv
```

### **1.2 Criar o Ambiente Virtual**

No diretório do seu projeto, execute o seguinte comando para criar um novo ambiente virtual chamado `venv`:

```bash
python -m venv venv
```

Isso criará um diretório chamado `venv` no seu projeto, que conterá o ambiente isolado.

### **1.3 Ativar o Ambiente Virtual**

- **No Windows:** Para ativar o ambiente virtual no Windows, execute o comando abaixo no terminal (no diretório do seu projeto):

```bash
.\venv\Scripts\activate
```

- **No macOS/Linux:** No macOS ou Linux, execute:

```bash
source venv/bin/activate
```

- **No Gitbash:** Na linha de comando do GItBash, execute:

```bash
source venv/Scripts/activate
```

Após ativar, você verá que o nome do ambiente virtual aparece no prompt (por exemplo, (venv)).

## **2. Gerar o Arquivo requirements.txt**

O arquivo requirements.txt lista todas as dependências do seu projeto, e pode ser usado para instalar esses pacotes em outros ambientes.

**2.1 Instalar Dependências Necessárias**

Com o ambiente virtual ativado, você pode instalar os pacotes que o seu projeto precisa. Por exemplo, se você precisar do pandas e seaborn:

Dentro no notebook Python, com o kernel configurado para o ambiente virtual, execute em uma célula:

```ipynb
%pip install pandas
```

Faça isto para todas bibliotecas que quer instalar.


### **2.2. Gerar o Arquivo requirements.txt**

Para gerar o arquivo requirements.txt com todas as dependências do seu ambiente virtual, execute:

```ipynb
%pip freeze > requirements.txt
```

Isso criará um arquivo requirements.txt no diretório do projeto com todas as bibliotecas instaladas no ambiente virtual.


## **3. Usar requirements.txt em um Projeto Já Existente**

Se você já tem um projeto existente e um arquivo requirements.txt, você pode configurar um ambiente virtual e instalar todas as dependências que o projeto necessita.

### **3.1 Criar e Ativar o Ambiente Virtual (se ainda não o fez)**

Siga os mesmos passos mencionados no Passo 1 para criar e ativar o ambiente virtual.

### **3.2 Instalar as Dependências Usando requirements.txt**

Depois de ativar o ambiente virtual, basta executar o seguinte comando para instalar todas as dependências que estão listadas no arquivo requirements.txt:


```ipynb
%pip install -r requirements.txt
```

Isso irá ler o arquivo requirements.txt e instalar todas as bibliotecas e suas versões especificadas.


---
---


```
pip list = verificar itens existentes na instalação
```

--- 
## Criar um requirement pelo gitbash

- criar uma Virtual Env
```git
python -m venv venv
```

- ativar 
```git
source venv/Scripts/activate
```

- desativar 
```git
desactivate
```

- caso tenha problema com o ipekernel
``pip install ipykernel``

### criar um requirements.txt

``!pip freeze > requirements.txt``

### arquivos que não devem ser subidos do github
[Toptal gitignore](https://www.toptal.com/developers/gitignore)


### verificar os arquivos commitados
``git status`` 

### usando o requirements.txt existente
``!pip freeze -r requirements.txt``


---

# PYEnv 

[PyEnv](https://github.com/pyenv/pyenv): stalação e gerenciamento das versões do python

versões gloral = sistema operacional
versões locak = no projeto



#### 1. necessário criar variável de ambietes


|------------------------|---------------------------------------|
|PYENV                   | C:\Users\name_user\.pyenv\pyenv-win\  |
|PYENV_HOME              | C\Users\name_user\.pyenv\pyenv-win\   |
|PYENV ROOT              | C\Users\name_user\.pyenv\pyenv-wir\   |
|------------------------|---------------------------------------|

**PATH** precisa ser dois caminhos configurados e colocar nas primeiras linhas:
C:\Users\name_user\.pyenv\pyenv-win\bin
C:\Users\name_user\.pyenv\pyenv-win\shims


instalar alguma versão python: ``pyenv install x.xx.x``

versão instaladas: ``pyenv versions``

definir versão global = ``pyenv global x.xx.a``<br>
definir versão local = ``pyenv local x.xx.b``<br>

-- ele cria um arquivo .python-version do python

# Poetry

## remover todas as bibliotecas da maquina (antes da instalaçaõ do poetry)

``pip freeze | grep -v "^-e" | xargs pip unistrall -y``

- criar projeto Poetry dentro da pasta desejada - ele cria uma pasta
-- ele adiciona apenas as bibliotecas necessárias
`` poetry new nome_projeto``


# Ambos juntos

- poetry para cuidar dos ambientes virtuais
``petry config cirtualenvs.in-project true`

- dentro do repositório
`` poetry new nome_projeto``

entra no projeto e abre o vscode.

- verificar as versões do python disponível: ``pyenv versions``

- instalar a versão local do python: ``pyenv local x.xx.xx``, obs.: se voce tiver configurado a versão global, é requisito ser uma versão acima da global. Porém, seja necessario uma versão antiga: alterar o arquivo [pyproject.toml] para a versão do python anterior a versão que deseja.

- atribuir uma versão específica na criaçaõ de uma virtual env: ``poetry env use x.xx.xx``

- ATENÇÂO: para não ter o risco de subir a pasta env no github, criar o arquivo [.gitignore]

- ativar o isolamento de instalaçaõ do sistema operacional - usar o ambiente virtual: ``poetry shell``

- adicionar as bibliotecas: ``poetry add pandas``
- remover as bibliotecas: ``poetry remove pandas``

- rodar o arquivo .py ( esteja dentro da pasta do arquivo): `poetry run python.py`

- instalar todas as dependencias que tem no que deseja mexer:  `poetry install`
- quando puxa as dependencias de um projeto existente, ele daum aviso que o proprio projeto é uma dependencia, então, pode utilizar `poetry install --no-root `

-- instalação atualizações de dependencias: ` poetry update`
