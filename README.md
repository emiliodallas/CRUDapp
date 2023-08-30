## CRUD - Hilab

Este código foi escrito em Python 3.10 para solucionar o exercício 1. Siga as etapas abaixo para executá-lo:

1. Para rodar o codigo, é possivel clocar o respositorio com 
    ```
    git clone https://github.com/emiliodallas/CRUDapp
    ```

2. Em seguida, e necessario adicionar um arquivo `.env` dentro da pasta _flaskServer_ com as credenciais no seguinte modelo:
    ```
    dbname = 'nome_db'
    user='nome_usuario'
    password='senha_usuario'
    host ='host'
    port = 'porta'
    ```

    Caso esteja utilizando um container novo do postgreSQL, pode-se usar as credenciais padrao. Caso esteja utilizando um que ja foi configurado, utilize essas credenciais.

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


Outra maneira é puxando diretamente as imagens do DockerHub. Para isso, basta clonar o respositorio e ir até o diretório _images_:

    cd images

E simplesmente digitar:

    
    docker compose up -d
    

Assim, ele irá puxar as imagens diretamente do DockerHub e iniciar os containers. É necessário também abrir a URL no navegador:


    http://0.0.0.0:8501

