# Flask Container Docker
Exemplo de aplicação de uma API em Flask em um container Docker.

## Rodando o Contêiner Flask

Siga as instruções abaixo para rodar o contêiner Flask localmente:

1. Certifique-se de ter o Docker instalado em sua máquina. Você pode fazer o download do Docker em [https://www.docker.com/get-started](https://www.docker.com/get-started).

2. Abra o terminal ou prompt de comando e navegue até o diretório onde você baixou/clonou este repositório.

3. Construa a imagem Docker a partir do Dockerfile utilizando o seguinte comando:

   ```shell
   docker build -t nome_da_imagem .

4. Após a conclusão da construção da imagem, execute o seguinte comando para rodar o contêiner:

    ```shell
    docker run -p 5000:5000 --name nome_do_container nome_da_imagem
   ```
Certifique-se de substituir "nome_do_container" pelo nome que deseja atribuir ao contêiner em execução e "nome_da_imagem" pelo nome da imagem Docker que você definiu no passo anterior.

5. O contêiner Flask agora está sendo executado no seu localhost na porta 5000.

6. Abra o seu navegador web e acesse http://localhost:5000 para ver a aplicação Flask em ação.

## Imagem pelo Docker Hub

Link Docker Hub: https://hub.docker.com/r/datacassio/flask_container_docker

1. Execute o seguinte comando para baixar a imagem do Docker Hub:
   ```shell
     docker pull datacassio/flask_container_docker
     ```

2. Após o término do download da imagem, execute o seguinte comando para iniciar o contêiner:
   ```shell
   docker run -p 5000:5000 datacassio/flask_container_docker
   ```
3. O contêiner Flask agora está sendo executado no seu localhost na porta 5000.

4. Abra o seu navegador web e acesse http://localhost:5000 para ver a aplicação Flask em ação.

Pronto! Agora você pode experimentar a aplicação Flask rodando no seu localhost. Divirta-se!



