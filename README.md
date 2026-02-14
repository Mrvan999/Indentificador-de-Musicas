Este script foi desenvolvido para solucionar um problema comum após a recuperação de dados com ferramentas como o PhotoRec. Quando arquivos são recuperados de discos corrompidos, eles perdem seus nomes originais e metadados de sistema, restando apenas códigos alfanuméricos aleatórios.

Para arquivos de música, este script utiliza a tecnologia de reconhecimento do Shazam para ouvir o arquivo, identificar o artista e a música, e renomear o arquivo automaticamente com o nome correto.

🚀 Como Funciona
Escaneamento: O script acessa a pasta definida (ex: recup_dir.1) e lista todos os arquivos com extensão .mp3.

Identificação: Cada arquivo é enviado silenciosamente para a API do Shazam através da biblioteca shazamio.

Sanitização: O script remove caracteres especiais que o Windows não permite em nomes de arquivos (como \ / * ? : < > |).

Renomeação: Se a música for identificada, o arquivo é renomeado para o formato: Artista - Título da Música.mp3.

Prevenção: O script verifica se o arquivo já existe ou se já está com o nome correto para evitar erros ou duplicatas.

🛠️ Requisitos
Antes de rodar o script, você precisará de:

Python 3.7+ instalado.

FFmpeg: O script depende do ffmpeg para processar os arquivos de áudio. Certifique-se de que o ffmpeg.exe está na mesma pasta do script ou configurado no PATH do seu sistema.

Bibliotecas Python:

Bash
pip install shazamio asyncio
⚙️ Configuração
No arquivo RecuperadorCaseiroFoda.py, altere a variável PASTA para o caminho onde estão os seus arquivos recuperados:

Python
PASTA = r"C:\Caminho\Para\Seus\Arquivos\Recuperados"
📝 Notas de Uso
Taxa de Sucesso: A identificação depende da música existir no banco de dados do Shazam e do arquivo não estar corrompido.

Velocidade: Existe um pequeno intervalo (sleep) entre as análises para evitar bloqueios por excesso de requisições na API.

Erro de Permissão: Certifique-se de que a pasta de destino não está configurada como "Somente Leitura" e que você tem permissões de administrador.
