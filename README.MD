
    <h1>Script de log de processos</h1>
    <p>Este script usa o módulo <code>psutil</code> do Python para obter informações sobre os processos em execução em seu sistema e o módulo <code>time</code> para controlar o intervalo de tempo entre as capturas. As informações são escritas em um arquivo de log chamado "process_log.txt".</p>
    <h2>Como usar</h2>
    <p>Para usar este script, você precisa ter o Python instalado em sua máquina e os módulos <code>psutil</code> e <code>time</code> devem estar disponíveis. Se você não tiver os módulos instalados, pode instalá-los usando o gerenciador de pacotes do Python, o pip, executando o seguinte comando no terminal ou prompt de comando:</p>
    <pre>
      <code class="whitespace-pre">pip install psutil time</code>
    </pre>
    <p>Em seguida, salve o código abaixo como um arquivo Python (por exemplo, <code>process_log.py</code>) e execute-o usando o interpretador Python:</p>
    <pre>
      <code class="whitespace-pre">
