# Classe base Canal
class Canal:
    def __init__(self, tipo):
        self._tipo = tipo

    def exibir_mensagem(self):
        print(f"Tipo: {self._tipo}")
        self.mostrar_detalhes()

    def mostrar_detalhes(self):

        print("\nMensagem:")
        if self._tipo == "Texto":
            print("Data de envio: 21/05/2025")
        elif self._tipo == "Vídeo":
            print("Arquivo: apresentacao.mp4")
            print("Formato: .mp4")
            print("Duração: 4min23s")
        elif self._tipo == "Foto":
            print("Arquivo: foto_viagem.jpg")
            print("Formato: .jpg")
        elif self._tipo == "Arquivo":
            print("Arquivo: trabalho.pdf")
            print("Formato: .pdf")

# Classes dos canais HERDANDO de Canal
class WhatsApp(Canal):
    def exibir_mensagem(self):
        print("\n[WhatsApp]")
        super().exibir_mensagem()

class Telegram(Canal):
    def exibir_mensagem(self):
        print("\n[Telegram]")
        super().exibir_mensagem()

class NumeroTelefone(Canal):
    def exibir_mensagem(self):
        print("\n[Número de telefone]")
        super().exibir_mensagem()

class Facebook(Canal):
    def exibir_mensagem(self):
        print("\n[Facebook]")
        super().exibir_mensagem()

class Instagram(Canal):
    def exibir_mensagem(self):
        print("\n[Instagram]")
        super().exibir_mensagem()

class TelegramUsuario(Canal):
    def exibir_mensagem(self):
        print("\n[Telegram Usuário]")
        super().exibir_mensagem()

# Função principal
def iniciar_chatbot():
    print("Escolha o canal:")
    print("1 - WhatsApp")
    print("2 - Telegram")
    print("3 - Número de telefone")
    print("4 - Facebook")
    print("5 - Instagram")
    print("6 - Telegram - Usuário")

    canais = {
        "1": WhatsApp,
        "2": Telegram,
        "3": NumeroTelefone,
        "4": Facebook,
        "5": Instagram,
        "6": TelegramUsuario
    }

    canal_input = input("Digite o número do canal: ")
    canal_classe = canais.get(canal_input)

    if not canal_classe:
        print("Canal inválido.")
        return

    print("\nEscolha o tipo da mensagem:")
    print("1 - Texto")
    print("2 - Vídeo")
    print("3 - Foto")
    print("4 - Arquivo")

    tipos = {
        "1": "Texto",
        "2": "Vídeo",
        "3": "Foto",
        "4": "Arquivo"
    }

    tipo_input = input("Digite o número do tipo: ")
    tipo = tipos.get(tipo_input)

    if not tipo:
        print("Tipo inválido.")
        return

    # Criando o objeto da classe do canal
    canal = canal_classe(tipo)
    canal.exibir_mensagem()

# Executar o chatbot
iniciar_chatbot()
