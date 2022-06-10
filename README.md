<h1 align="center">
    <img alt="Alura Pizza" src=".github/logo.svg" width="75px" />
</h1>

<h4 align="center">
  🚀 Django React: construindo uma aplicação de ponta a ponta
</h4>


<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalação">Instalação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#telas">Telas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#exemplo">Exemplo</a>
</p>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Django](https://www.djangoproject.com/)
- [Django-Rest-Framework](https://www.django-rest-framework.org/)
- [React](https://reactjs.org)
- [Cloudinary](https://cloudinary.com/)

## 💻 Projeto
**Curso da Alura no qual foi abordado: criação de uma API com Django Rest Framework com deploy no Heroku, site em React com deploy na Vercel. E hospedagem de arquivos no S3 (Eu usei o Cloudinary)**

## Instalação
### Pré requisitos
Ter instalado:
- [Python](https://www.python.org/downloads/)
- [Node](https://nodejs.org/en/download/)
- [Yarn](https://classic.yarnpkg.com/en/docs/install/)


### Clonar projeto
#### No terminal, rodar
```sh
git clone https://github.com/andre23arruda/alura-pizza
```

### Backend
#### No terminal, rodar:
```sh
# Entrar na pasta dos arquivos do backend
cd backend

# Renomear env_example.py para env.py
cp setup/env_example.py setup/env.py
# ADICIONE OS VALORES CORRETOS

# Criar um ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
. activate.sh
# ou
. venv/Scripts/activate # windows
. venv/bin/activate # linux

# Instalar os pacotes necessários
pip install -r requirements.txt

# Executar as migrações
python manage.py migrate

# Carregar dados
python manage.py loaddata dishes

# Criar super usuário
. create_su.sh

# Rodar backend
. run.sh
```

### Web
#### No terminal, rodar
```sh
# Entrar na pasta dos arquivos
cd web

# Renomear .env_example para .env
cp .env_example .env
# ADICIONE OS VALORES CORRETOS

# Instalar os pacotes necessários
yarn install

# Rodar
yarn dev
```

<div align="center">
    <img alt="Screen 1" title="Screen 1" src=".github/web_1.png?raw=true" width="400px" />
</div>
<p align="center">Screen 1</p>
<hr>



## Exemplo
<a href="https://andrearruda-alura-pizza.vercel.app/" target="_blank">Visitar</a>