import tkinter as tk

def clicar():
    print("Play")


janela = tk.Tk()
janela.title("Moonox")
janela.geometry("1080x720")

botaoCentral = tk.Button(
    janela,
    text="▶",
    font=("Arial", 30),
    bg="black",
    fg="white",
    width=3,
    height=1,
    padx=0,
    pady=0
)

botaoCentral.place(relx=0.5, rely=0.92, anchor="center")


botaoDireita = tk.Button(
    janela,
    text="Play",
    command=clicar,
    font=("Arial", 16),
    bg="black",
    fg="white",
    width=5,
    height=1
)

botaoDireita.place(relx=0.57, rely=0.93, anchor="center")


botaoEsquerda = tk.Button(
    janela,
    text="Play",
    command=clicar,
    font=("Arial", 16),
    bg="black",
    fg="white",
    width=5,
    height=1
)

botaoEsquerda.place(relx=0.43, rely=0.93, anchor="center")



janela.mainloop()