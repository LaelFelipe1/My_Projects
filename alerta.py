import threading
import time
import json
import os
from plyer import notification
import pystray
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import messagebox

CONFIG_FILE = "config.json"

# =========================
# CONFIG
# =========================
def carregar_config():
    if not os.path.exists(CONFIG_FILE):
        return {"intervalo": 15, "rodando": True}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def salvar_config():
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

config = carregar_config()

# =========================
# ALERTA
# =========================
def enviar_alerta():
    notification.notify(
        title="***🚨ALERTA🚨***",
        message="Enviar mensagens para os alunos On-lines",
        timeout=15
    
    )

# =========================
# LOOP
# =========================
def loop_alerta():
    while True:
        if config["rodando"]:
            enviar_alerta()
            time.sleep(config["intervalo"] * 60)
        else:
            time.sleep(1)

# =========================
# GUI
# =========================
def salvar_config_gui():
    try:
        minutos = int(entry_intervalo.get())
        config["intervalo"] = minutos
        salvar_config()
        messagebox.showinfo("Sucesso", "Configuração salva!")
    except:
        messagebox.showerror("Erro", "Digite um número válido")

def alternar_status():
    config["rodando"] = not config["rodando"]
    salvar_config()
    atualizar_status()

def atualizar_status():
    status = "ATIVO" if config["rodando"] else "PAUSADO"
    label_status.config(text=f"Status: {status}")

def esconder_janela():
    root.withdraw()

def mostrar_janela(icon=None, item=None):
    root.after(0, root.deiconify)

# =========================
# BANDEJA
# =========================
def sair(icon, item):
    icon.stop()
    root.destroy()

def criar_icone():
    img = Image.new('RGB', (64, 64), color='white')
    draw = ImageDraw.Draw(img)
    draw.ellipse((16, 16, 48, 48), fill='red')
    return img

def criar_tray():
    icon = pystray.Icon("Alerta")
    icon.icon = criar_icone()
    icon.menu = pystray.Menu(
        pystray.MenuItem("Abrir", mostrar_janela),
        pystray.MenuItem("Sair", sair)
    )
    icon.run()

# =========================
# THREADS
# =========================
threading.Thread(target=loop_alerta, daemon=True).start()
threading.Thread(target=criar_tray, daemon=True).start()

# =========================
# INTERFACE
# =========================
root = tk.Tk()
root.title("Sistema de Alertas")

root.geometry("300x200")

label_status = tk.Label(root, text="")
label_status.pack(pady=10)

tk.Label(root, text="Intervalo (minutos):").pack()

entry_intervalo = tk.Entry(root)
entry_intervalo.insert(0, str(config["intervalo"]))
entry_intervalo.pack()

tk.Button(root, text="Salvar", command=salvar_config_gui).pack(pady=5)
tk.Button(root, text="Pausar / Ativar", command=alternar_status).pack(pady=5)
tk.Button(root, text="Minimizar para bandeja", command=esconder_janela).pack(pady=5)

atualizar_status()

root.mainloop()