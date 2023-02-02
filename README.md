# 💡 Sobre

**Template para projetos de datascience. O projeto utiliza o Poetry para gerenciamento do ambiente virtual e das dependências do Python, o DVC para gerenciar as versões dos datasets, e mkdocs para a documentação do projeto e deploy automatico no github pages, usando o actions**

&nbsp;
# Veja mais na [pagina do projeto](https://smrenato.github.io/ds-projects/)

<img style="width:30px; height:30px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" />
          
### Branchs
* **Template** em branco
* **docs** documentação
* **main** projeto

&nbsp;

# ⚙️ Como usar

### 📃 requisistos

- **Poetry** >= 1.3.2

&nbsp;

### 💻 Instalando as bibliotecas

- **Clone este repositório**
- **Dentro da pasta do projeto:**

```bash

   # Apenas se vc preferir o .venv no diretorio
   $ poetry config virtualenvs.create true

   #
   $ poetry install
   $ poetry shell # ativar o .venv

```

### 🗃 Usando o DVC

- **OS dados podem ser adicionados manualmente, ou por meio do DVC**
- Mais em [DVC user guide](https://dvc.org/doc/user-guide/overview)

```sh
    # configure seu repositorio de dados
    $ mkdir data
    $ dvc init

```

# 🧰 Recursos

- Documentação com mkdocs e pulblicação com github pages
- Gerenciamento de dados com DVC

&nbsp;

# 💻 Tecnologias

![image](https://img.shields.io/badge/Python-3.10-9146F?style=for-the-badge&logo=python&logoColor=white&labelColor=46f)
![image](https://img.shields.io/badge/DVC-2.41-9146F?style=for-the-badge&logo=dvc&logoColor=white&labelColor=13ADC7)
![image](https://img.shields.io/badge/Poetry-1.3.2-9146F?style=for-the-badge&logo=poetry&logoColor=white&labelColor=60A5FA)
![image](https://img.shields.io/badge/Dynaconf-3.1.11-9146F?style=for-the-badge&logo=.env&logoColor=white&labelColor=60A5FA)
![image](https://img.shields.io/badge/Mkdocs-9.0.3-9146F?style=for-the-badge&logo=read-the-docs&logoColor=white&labelColor=000000)
![image](https://img.shields.io/badge/Ipykernel-6.20.2-9146F?style=for-the-badge&logo=jupyter&logoColor=white&labelColor=F37626)
![image](https://img.shields.io/badge/Scikitlearn-1.2.0-9146F?style=for-the-badge&logo=scikitlearn&logoColor=white&labelColor=F7931E)
![image](https://img.shields.io/badge/TensorFlow-2.11.0-9146F?style=for-the-badge&logo=tensorflow&logoColor=white&labelColor=FF6F00)