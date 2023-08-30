## CRUD - Hilab

Este código foi escrito em Python 3.10 para solucionar o exercício 1. Siga as etapas abaixo para executá-lo:

1. Para rodar o codigo, é possivel clonar o respositorio com 
    ```
    git clone https://github.com/emiliodallas/CRUDapp
    ```

2. Em seguida, é necessario adicionar um arquivo `.env` dentro da pasta _flaskServer_ com as credenciais no seguinte modelo:
    ```
    dbname = 'nome_db'
    user='nome_usuario'
    password='senha_usuario'
    host ='host'
    port = 'porta'
    ```

    Caso esteja utilizando um container novo do postgreSQL, pode-se usar as credenciais padrão. Caso esteja utilizando um que já foi configurado, utilize essas credenciais.

3. Para rodar os containers, use: 
    ```
    docker compose build
    ```

4. E depois subindo o container com:
    ```
    docker compose up -d
    ```

5. Como estamos rodando o container em modo _detached_ é necessario abrir algum navegador e digitar a URL:

    ```    
    http://0.0.0.0:8501
    ```

    Este comando irá abrir uma interface utilizando Streamlit para adicionar, ler, atualizar ou deletar entradas no banco de dados.


6. Outra maneira é puxando diretamente as imagens do DockerHub. Para isso, basta clonar o respositorio e ir até o diretório _images_:
    ```
    cd images
    ```
7. Aqui se faz necessária uma pequena configuração. Abra o arquivo docker-compose.yaml. No serviço `flaskserver` é necessário atualizar os parâmetros de ambiente. Isso é feito nas linhas:

    ```
    POSTGRES_USER: your-user
    POSTGRES_PASSWORD: your-password
    POSTGRES_HOST: your-host
    POSTGRES_DATABASE: your-database
    POSTGRES_PORT: your-port
    ```
    É necessário apenas alterar os parâmetros para configuração de conexão com o banco de dados (PostgreSQL). Podem ser utilizados os valores default, conforme documentação.

7. Entao, simplesmente digitar:

    ```
    docker compose up -d
    ```

    Assim, ele irá puxar as imagens diretamente do DockerHub e iniciar os containers. 

8. É necessário também abrir a URL no navegador:


    http://0.0.0.0:8501

