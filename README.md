## CRUD - Hilab

Este código foi escrito em Python 3.10 para solucionar o exercício 1. Siga as etapas abaixo para executá-lo:

1. Para rodar o codigo, e possivel clonar o repositorio e rodar, primeiro fazendo build
    ```
    docker compose build
    ```

2. E depois subindo o container com:
    ```
    docker compose up -d
    ```


Foi utilizado o banco de dados PostgreSQL puxando diretamente sua imagem do DockerHub. As configuracoes padroes utilizadas foram:

- Nome do banco de dados: `postgres`
- Usuário: `postgres`
- Senha: `mysecretpassword`
- Host: `postgres`


3. Como estamos rodando o container em modo _detached_ e necessario abrir algum navegador e digitar a URL:

    ```    
    http://0.0.0.0:8501
    ```

Este comando irá abrir uma interface utilizando Streamlit para adicionar, ler, atualizar ou deletar entradas no banco de dados.