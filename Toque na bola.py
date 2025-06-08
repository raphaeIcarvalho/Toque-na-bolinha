import time

inicio = time.time()

print("Seja bem-vindo ao nosso primeiro projeto baseado em Python!")

atraso = time.sleep(3)

print("Os autores deste projeto são: Raphael da Silva & Felipe Leal.")

atraso = time.sleep(3)

print("Este projeto é um pequeno jogo individual para testar a sua atenção.")

atraso = time.sleep(3)

print("O objetivo do jogo é simples: toque na bola que aparecer na tela o mais rápido posível.")

atraso = time.sleep(3)

print("Vamos começar com apenas uma pergunta pessoal.")

atraso = time.sleep(3)

nome = input("Qual é o seu nome?")

print(f"Prazer em conchecer-lhe, {nome}!")

atraso = time.sleep(3)

print("O jogo começará em:")

def contagemregressiva(t):
    while t:
        mins, segs = divmod(t, 60)
        temporizador = f'{mins:02d}:{segs:02d}'
        print(temporizador, end='\r')
        time.sleep(1)
        t -= 1
        
contagemregressiva(3)

import tkinter as tk
from tkinter import ttk
import random
import math

def iniciar_progresso():
    progress.start()
    
    for i in range(101):
        time.sleep(0.05)
        progress['value'] = i
        root.update_idletasks()
    progress.stop()
    
root = tk.Tk()
root.title("Tela de Carregamento")

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

frase = tk.Label(root, text="Carregando..", font=("Arial", 16))
frase.pack(pady=10)

def iniciar_jogo():
    root.destroy()
    
root.after(10, iniciar_progresso)
root.after(101 * 50 + 100, iniciar_jogo)

root.mainloop()

raio = 25
cursor_raio = 5

def criar_bolinha():
    x = random.randint(raio, 500 - raio)
    y = random.randint(raio, 400 - raio)
    return canvas.create_oval(
        x - raio, y - raio,
        x + raio, y + raio,
        fill="white", outline="black"
    )

def mover_bolinha():
    x = random.randint(raio, 500 - raio)
    y = random.randint(raio, 400 - raio)
    canvas.coords(
        bolinha,
        x - raio, y - raio,
        x + raio, y + raio
    )
    
def mover_cursor(event):
    x, y = event.x, event.y
    canvas.coords(cursor, x - cursor_raio, y - cursor_raio, x + cursor_raio, y + cursor_raio)
    
    coords = canvas.coords(bolinha)
    cx = (coords[0] + coords[2]) / 2
    cy = (coords[1] + coords[3]) / 2
    dist = math.hypot(x - cx, y - cy)
    
    if dist <= raio:
        mover_bolinha()
        
        global score
        score += 1
        print(f"Quantidade de vezes que você tocou na bola: {score}")
score = 0

root = tk.Tk()
root.title("Toque na bola")
root.geometry("600x500")
root.configure(bg="white")

canvas = tk.Canvas(root, width=500, height=400, bg="green", highlightthickness=4, highlightbackground="gray")
canvas.pack(pady=10)
canvas.config(cursor="none")

bolinha = criar_bolinha()
cursor = canvas.create_oval(0, 0, 0, 0, fill="black")

canvas.bind("<Motion>", mover_cursor)

root.mainloop()

        
