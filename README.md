# API regional

## Este projeto foi feito com:

* [Python 3.11](https://www.python.org/)
* [Django 5.0](https://www.djangoproject.com/)
* [Django-Ninja](https://django-ninja.rest-framework.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Poetry
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone git@github.com:djwesleyborges/regioes-vs-estados-vs-cidades.git
cd regioes-vs-estados-vs-cidades
poetry shell
poetry install
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --email="admin@admin.org"
Acesse: http://localhost:8000/api/v1/docs
```