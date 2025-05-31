from gtts import gTTS
import os

# Texto da apresentação com tom mais amigável
texto = """
Olá, tudo bem? Eu sou Dione Nascimento! 
Atualmente, estou mergulhando no universo do Python e cada vez mais apaixonado pelo que posso aprender e aplicar. 
Sou estudante de Engenharia de Produção e trabalho com confiabilidade mecânica, mas tenho uma paixão enorme por tecnologia, automação e inovação.

No meu LinkedIn, compartilho ideias, dicas e tudo o que estou aprendendo, e adoraria contar com você por lá. Se você também é apaixonado por tecnologia ou busca melhorar a sua carreira na área de manutenção, vamos nos conectar! 

Ah, e não esqueça de conferir o meu canal no YouTube, o "Portal da Manutenção", onde trago conteúdos sobre produtividade, engenharia e muito mais!

Vamos crescer juntos nessa jornada. Me acompanhe nas minhas redes sociais, tenho certeza que podemos aprender muito um com o outro. 
Te espero por lá!
"""

# Configuração do TTS
tts = gTTS(texto, lang='pt', slow=False)

# Salvar o áudio em um arquivo
audio_file = "apresentacao_amigavel.mp3"
tts.save(audio_file)

# Reproduzir o arquivo de áudio
os.system(f"start {audio_file}")  # Windows

print("Áudio de apresentação gerado com sucesso!")
