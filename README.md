# Machine Learning Web App Bike Rentals

## Instruções de Instalação para Windows

<b>1.</b> Certifique-se de ter o Python instalado em sua máquina. Você pode baixar a última versão do Python em https://www.python.org/downloads/.


<b>2.</b> Abra o terminal e navegue até o diretório onde o arquivo app.py está localizado.


<b>3.</b> Crie um ambiente virtual para o projeto usando o seguinte comando no terminal:

    python -m venv myenv

<b>4.</b> Ative o ambiente virtual usando o seguinte comando:

    myenv\Scripts\activate
  

<b>5.</b> Instale as dependências necessárias usando o seguinte comando:

    pip install flask urllib3 python-dotenv
  

<b>6.</b> Defina as variáveis de ambiente 'AZURE_ENDPOINT_URL' e 'AZURE_API_KEY' no arquivo ".env"

    echo "AZURE_ENDPOINT_URL=https://example.com/api" >> .env
    echo "AZURE_API_KEY=abc123!@#" >> .env


<b>7.</b> Inicie o aplicativo com o seguinte comando:

    python app.py
  

<b>8.</b> Abra um navegador da web e navegue até http://localhost:5000/ para testar o aplicativo.
