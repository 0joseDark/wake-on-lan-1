import tkinter as tk
from tkinter import messagebox, Menu
from wakeonlan import send_magic_packet  # Função do módulo pywakeonlan
import datetime

# Função para enviar o pacote mágico e gravar no log
def enviar_pacote_wol(mac_address, ip_address):
    """
    Envia um pacote mágico (Wake-on-LAN) para o endereço MAC fornecido
    e registra os detalhes no ficheiro note.log.

    Args:
        mac_address (str): Endereço MAC do dispositivo a ser ligado.
        ip_address (str): Endereço IP de destino (opcional, usado para contexto no log).
    """
    try:
        # Enviar o pacote mágico
        send_magic_packet(mac_address)

        # Gravar no log
        registrar_log(mac_address, ip_address)
        messagebox.showinfo("Sucesso", "Pacote Wake-on-LAN enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao enviar o pacote mágico: {e}")

# Função para registrar os detalhes no log
def registrar_log(mac_address, ip_address):
    """
    Registra os detalhes do envio no ficheiro note.log.

    Args:
        mac_address (str): Endereço MAC do dispositivo.
        ip_address (str): Endereço IP do dispositivo (opcional).
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | MAC: {mac_address} | IP: {ip_address}\n"

    # Gravar no ficheiro note.log
    with open("note.log", "a") as log_file:
        log_file.write(log_entry)

    # Exibir no terminal
    print(log_entry)

# Função chamada pelo botão "Ligar PC Remoto"
def ligar_pc_remoto():
    """
    Obtém o endereço IP e MAC da entrada do usuário e chama a função
    para enviar o pacote Wake-on-LAN.
    """
    mac = entry_mac.get().strip()  # Remove espaços extras
    ip = entry_ip.get().strip()  # Remove espaços extras

    if not mac:
        messagebox.showwarning("Atenção", "Por favor, insira um endereço MAC válido.")
        return

    enviar_pacote_wol(mac, ip)  # Chama a função para enviar o pacote

# Função para sair da aplicação
def sair():
    """
    Fecha a janela principal da aplicação.
    """
    janela.destroy()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Wake-on-LAN")  # Título da janela
janela.geometry("400x250")  # Dimensão da janela

# Configuração do menu superior
menu_bar = Menu(janela)
menu_arquivo = Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Sair", command=sair)
menu_bar.add_cascade(label="Ficheiro", menu=menu_arquivo)
janela.config(menu=menu_bar)

# Rótulo e campo de entrada para o endereço IP
label_ip = tk.Label(janela, text="Endereço IP (opcional):")
label_ip.pack(pady=5)
entry_ip = tk.Entry(janela, width=30)
entry_ip.pack(pady=5)

# Rótulo e campo de entrada para o endereço MAC
label_mac = tk.Label(janela, text="Endereço MAC:")
label_mac.pack(pady=5)
entry_mac = tk.Entry(janela, width=30)
entry_mac.pack(pady=5)

# Botão para enviar o pacote Wake-on-LAN
botao_ligar = tk.Button(janela, text="Ligar PC Remoto", command=ligar_pc_remoto)
botao_ligar.pack(pady=10)

# Botão para sair da aplicação
botao_sair = tk.Button(janela, text="Sair", command=sair)
botao_sair.pack(pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
