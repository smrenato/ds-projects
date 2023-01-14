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

![image](https://img.shields.io/static/v1?label=DVC&message=data%20version%20control&color=orange&style=flat-square)
![image](https://img.shields.io/static/v1?label=Poetry&message=v1.3.2&color=orange&style=flat-square)
![image](https://img.shields.io/static/v1?label=mkdocs&message=material&color=orange&style=flat-square)
