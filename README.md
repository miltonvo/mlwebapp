# Machine Learning Web App

## Instruções de Instalação

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixar a última versão do Python em https://www.python.org/downloads/.

2. Abra o terminal e navegue até o diretório onde o arquivo app.py está localizado.

3. Crie um ambiente virtual para o projeto usando o seguinte comando no terminal:

python -m venv myenv

4. Ative o ambiente virtual usando o seguinte comando:

myenv\Scripts\activate

5. Instale as dependências necessárias usando o seguinte comando:

pip install flask urllib3

6. Defina as variáveis de ambiente 'AZURE_ENDPOINT_URL' e 'AZURE_API_KEY' com os valores apropriados para o serviço que você está chamando em seu código. Você pode definir essas variáveis no terminal usando o seguinte comando:

set AZURE_ENDPOINT_URL=<valor>
  
set AZURE_API_KEY=<valor>

7. Inicie o aplicativo com o seguinte comando:

python3 app.py

8. Abra um navegador da web e navegue até http://localhost:5000/ para testar o aplicativo.
