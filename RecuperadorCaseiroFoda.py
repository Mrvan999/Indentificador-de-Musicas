import os
import asyncio
import re
from shazamio import Shazam

caminho_script = os.path.dirname(os.path.abspath(__file__))
if caminho_script not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + caminho_script

PASTA = r"C:\Users\Pichau\Documents\Backup de musica do ely\recup_dir.1"

def limpar_nome_arquivo(nome):
    return re.sub(r'[\\/*?:"<>|]', "", nome)

async def identificar_musica(caminho, shazam_instance):
    try:
        out = await shazam_instance.recognize_song(caminho)
        
        if "track" in out:
            track = out["track"]
            artista = track.get("subtitle", "Artista Desconhecido")
            titulo = track.get("title", "Titulo Desconhecido")
            return artista, titulo
    except Exception as e:
        print(f"Erro ao processar '{os.path.basename(caminho)}': {e}")
        if "ffmpeg" in str(e).lower():
            print("!!! Parece que o ffmpeg.exe não foi encontrado ou está corrompido.")
    
    return None, None

async def main():
    if not os.path.exists(PASTA):
        print(f"ERRO: A pasta '{PASTA}' não foi encontrada.")
        return

    print("Iniciando Shazam...")
    shazam = Shazam()
    
    arquivos = [f for f in os.listdir(PASTA) if f.lower().endswith(".mp3")]
    total = len(arquivos)
    
    print(f"Encontrados {total} arquivos MP3.")
    print("-" * 40)

    for i, arquivo in enumerate(arquivos, 1):
        caminho_original = os.path.join(PASTA, arquivo)
        
        print(f"[{i}/{total}] Analisando: {arquivo}")
        
        artista, titulo = await identificar_musica(caminho_original, shazam)

        if artista and titulo:

            nome_arquivo_limpo = f"{limpar_nome_arquivo(artista)} - {limpar_nome_arquivo(titulo)}.mp3"

            if nome_arquivo_limpo == arquivo:
                print(" -> Nome já está correto.")
            else:
                novo_caminho = os.path.join(PASTA, nome_arquivo_limpo)

                if os.path.exists(novo_caminho):
                    print(f" -> AVISO: '{nome_arquivo_limpo}' já existe. Pulando.")
                else:
                    try:
                        os.rename(caminho_original, novo_caminho)
                        print(f" -> SUCESSO: Renomeado para '{nome_arquivo_limpo}'")
                    except OSError as e:
                        print(f" -> ERRO DE PERMISSÃO: {e}")
        else:
            print(" -> Não identificado.")
        
        await asyncio.sleep(0.5) 

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário.")