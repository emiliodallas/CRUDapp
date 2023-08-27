## CRUD - Hilab

Este código foi escrito em Python 3.10 para solucionar o exercício 1. Siga as etapas abaixo para executá-lo:

1. Para rodar o codigo, é possivel clonar o repositório e rodar, primeiro fazendo build
    ```
    docker compose build
    ```

2. E depois subindo o container com:
    ```
    docker compose up -d
    ```


Foi utilizado o banco de dados PostgreSQL puxando diretamente sua imagem do DockerHub. As configuracoes padrões utilizadas foram:

- Nome do banco de dados: `postgres`
- Usuário: `postgres`
- Senha: `mysecretpassword`
- Host: `postgres`


3. Como estamos rodando o container em modo _detached_ é necessario abrir algum navegador e digitar a URL:

    ```    
    http://0.0.0.0:8501
    ```

Este comando irá abrir uma interface utilizando Streamlit para adicionar, ler, atualizar ou deletar entradas no banco de dados.


Outra maneira é puxando diretamente as imagens do DockerHub. Para isso, basta ir até o diretório _images_:

```cd images```

E simplesmente digitar:

```docker compose up -d```

Sendo necessário também abrir a URL no navegador:

```http://0.0.0.0:8501```
