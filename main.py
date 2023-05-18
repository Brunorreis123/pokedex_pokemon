from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Criando a Janela
janela = Tk()
janela.title('Pokedex Pokémon')
janela.geometry('550x510')

# Cores
co0 = "#444466"  # Preto
co1 = "#feffff"  # Branco
co2 = "#6f9fbd"  # Azul
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#ef5350"  # Vermelha

# criando o frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat', bg='#7CFC00')
frame_pokemon.grid(row=1, column=0)

# JANELA DE CADA POKEMON

# Nome Pokemon Pikachu
poke_nome_pikachu = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER,
                          font=('Fixedsys 20'), bg='#7CFC00', fg=co0)
poke_nome_pikachu.place(x=12, y=15)

# Tipo Pokemon Pikachu
poke_tipo_pikachu = Label(frame_pokemon, text='Elétrico', relief='flat', anchor=CENTER,
                          font=('Ivy 10 bold'), bg='#7CFC00', fg=co0)
poke_tipo_pikachu.place(x=12, y=50)

# Id Pokemon Pikachu
poke_id_pikachu = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10'), bg='#7CFC00', fg=co0)
poke_id_pikachu.place(x=12, y=75)

# Carregando a imagem do Pikachu em formato PNG
imagem_pokemon_pikachu = Image.open('images/pikachu.png')
imagem_pokemon_pikachu = imagem_pokemon_pikachu.resize((238, 238))
imagem_pokemon_pikachu = ImageTk.PhotoImage(imagem_pokemon_pikachu)

# Exibindo a imagem do Pikachu no frame
poke_imagem_pikachu = Label(frame_pokemon, image=imagem_pokemon_pikachu, relief='flat', bg='#7CFC00')
poke_imagem_pikachu.place(x=60, y=50)

poke_tipo_pikachu.lift()

# Status pokemon
poke_status_pikachu = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_status_pikachu.place(x=15, y=300)

# Hp Pikachu
poke_hp_pikachu = Label(janela, text='HP: 100', relief='flat', anchor=CENTER,
                        font=('Verdana 10'), bg=co1, fg=co4)
poke_hp_pikachu.place(x=15, y=350)

# Ataque Pikachu
poke_ataque_pikachu = Label(janela, text='Ataque: 300', relief='flat', anchor=CENTER,
                            font=('Verdana 10'), bg=co1, fg=co4)
poke_ataque_pikachu.place(x=15, y=380)

# Defesa Pikachu
poke_defesa_pikachu = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER,
                            font=('Verdana 10'), bg=co1, fg=co4)
poke_defesa_pikachu.place(x=15, y=410)

# Velocidade Pikachu
poke_velocidade_pikachu = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER,
                                font=('Verdana 10'), bg=co1, fg=co4)
poke_velocidade_pikachu.place(x=15, y=440)

# total Pikachu
poke_total_pikachu = Label(janela, text='Total: 1200', relief='flat', anchor=CENTER,
                           font=('Verdana 10'), bg=co1, fg=co4)
poke_total_pikachu.place(x=15, y=470)

# Habilidades 1 Pikachu
poke_habilidade_pikachu1 = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1,
                                 fg=co0)
poke_habilidade_pikachu1.place(x=210, y=300)

# Habilidades 2 Pikachu
poke_habilidade_pikachu2 = Label(janela, text='Choque do Trovão', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                 bg=co1, fg=co4)
poke_habilidade_pikachu2.place(x=210, y=350)

# Habilidades 3 Pikachu
poke_habilidade_pikachu3 = Label(janela, text='Calda de Ferro', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                 bg=co1, fg=co4)
poke_habilidade_pikachu3.place(x=210, y=380)

# Habilidades 4 Pikachu
poke_habilidade_pikachu4 = Label(janela, text='Investida Trovão', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                 bg=co1, fg=co4)
poke_habilidade_pikachu4.place(x=210, y=410)

# criando o frame Bulbasaur
frame_pokemon_bulbasaur = Frame(janela, width=550, height=290, relief='flat', bg='#9932CC')
frame_pokemon_bulbasaur.grid(row=1, column=0)

# Nome Pokemon Bulbasaur
poke_nome_bulbasaur = Label(frame_pokemon_bulbasaur, text='Bulbasaur', relief='flat', anchor=CENTER,
                            font=('Fixedsys 20'), bg='#7CFC00', fg=co0)
poke_nome_bulbasaur.place(x=12, y=15)

# Tipo Pokemon Bulbasaur
poke_tipo_bulbasaur = Label(frame_pokemon_bulbasaur, text='Planta/Veneno', relief='flat', anchor=CENTER,
                            font=('Ivy 10 bold'), bg='#7CFC00', fg=co0)
poke_tipo_bulbasaur.place(x=12, y=50)

# Id Pokemon Bulbasaur
poke_id_bulbasaur = Label(frame_pokemon_bulbasaur, text='#001', relief='flat', anchor=CENTER,
                          font=('Ivy 10'), bg='#7CFC00', fg=co0)
poke_id_bulbasaur.place(x=12, y=75)

# Carregando a imagem do Bulbasaur em formato PNG
imagem_pokemon_bulbasaur = Image.open('images/bulbasaur.png')
imagem_pokemon_bulbasaur = imagem_pokemon_bulbasaur.resize((238, 238))
imagem_pokemon_bulbasaur = ImageTk.PhotoImage(imagem_pokemon_bulbasaur)

# Exibindo a imagem do Bulbasaur no frame
poke_imagem_bulbasaur = Label(frame_pokemon, image=imagem_pokemon_bulbasaur, relief='flat', bg='#7CFC00')
poke_imagem_bulbasaur.place(x=60, y=50)

poke_tipo_bulbasaur.lift()

# Status pokemon Bulbasaur
poke_status_bulbasaur = Label(janela, text='Status', relief='flat', anchor=CENTER,
                              font=('Verdana 20'), bg=co1, fg=co0)
poke_status_bulbasaur.place(x=15, y=300)

# Hp Bulbasaur
poke_hp_bulbasaur = Label(janela, text='HP: 100', relief='flat', anchor=CENTER,
                          font=('Verdana 10'), bg=co1, fg=co4)
poke_hp_bulbasaur.place(x=15, y=350)

# Ataque Bulbasaur
poke_ataque_bulbasaur = Label(janela, text='Ataque: 300', relief='flat', anchor=CENTER,
                              font=('Verdana 10'), bg=co1, fg=co4)
poke_ataque_bulbasaur.place(x=15, y=380)

# Defesa Bulbasaur
poke_defesa_bulbasaur = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER,
                              font=('Verdana 10'), bg=co1, fg=co4)
poke_defesa_bulbasaur.place(x=15, y=410)

# Velocidade Bulbasaur
poke_velocidade_bulbasaur = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER,
                                  font=('Verdana 10'), bg=co1, fg=co4)
poke_velocidade_bulbasaur.place(x=15, y=440)

# Total Bulbasaur
poke_total_bulbasaur = Label(janela, text='Total: 1200', relief='flat', anchor=CENTER,
                             font=('Verdana 10'), bg=co1, fg=co4)
poke_total_bulbasaur.place(x=15, y=470)

# Habilidades 1 Bulbasaur
poke_habilidade_bulbasaur1 = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'),
                                   bg=co1, fg=co0)
poke_habilidade_bulbasaur1.place(x=210, y=300)

# Habilidades 2 Bulbasaur
poke_habilidade_bulbasaur2 = Label(janela, text='Chicote de Vinha', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                   bg=co1, fg=co4)
poke_habilidade_bulbasaur2.place(x=210, y=350)

# Habilidades 3 Bulbasaur
poke_habilidade_bulbasaur3 = Label(janela, text='Raio Solar', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1,
                                   fg=co4)
poke_habilidade_bulbasaur3.place(x=210, y=380)

# Habilidades 4 Bulbasaur
poke_habilidade_bulbasaur4 = Label(janela, text='Semente Sanguessuga', relief='flat', anchor=CENTER,
                                   font=('Verdana 10'), bg=co1, fg=co4)
poke_habilidade_bulbasaur4.place(x=210, y=410)

# criando o frame Charmander
frame_pokemon_charmander = Frame(janela, width=550, height=290, relief='flat', bg='#9932CC')
frame_pokemon_charmander.grid(row=1, column=0)

# Nome Pokemon Charmander
poke_nome_charmander = Label(frame_pokemon_charmander, text='Charmander', relief='flat', anchor=CENTER,
                             font=('Fixedsys 20'), bg='#7CFC00', fg=co0)
poke_nome_charmander.place(x=12, y=15)

# Tipo Pokemon Charmander
poke_tipo_charmander = Label(frame_pokemon_charmander, text='Fogo', relief='flat', anchor=CENTER,
                             font=('Ivy 10 bold'), bg='#7CFC00', fg=co0)
poke_tipo_charmander.place(x=12, y=50)

# Id Pokemon Charmander
poke_id_charmander = Label(frame_pokemon_charmander, text='#004', relief='flat', anchor=CENTER, font=('Ivy 10'),
                           bg='#7CFC00', fg=co0)
poke_id_charmander.place(x=12, y=75)

# Carregando a imagem do Charmander em formato PNG
imagem_pokemon_charmander = Image.open('images/charmander.png')
imagem_pokemon_charmander = imagem_pokemon_charmander.resize((238, 238))
imagem_pokemon_charmander = ImageTk.PhotoImage(imagem_pokemon_charmander)

# Exibindo a imagem do Charmander no frame
poke_imagem_charmander = Label(frame_pokemon, image=imagem_pokemon_charmander, relief='flat', bg='#7CFC00')
poke_imagem_charmander.place(x=60, y=50)

poke_tipo_charmander.lift()

# Status pokemon Charmander
poke_status_charmander = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_status_charmander.place(x=15, y=300)

# Hp Charmander
poke_hp_charmander = Label(janela, text='HP: 100', relief='flat', anchor=CENTER,
                           font=('Verdana 10'), bg=co1, fg=co4)
poke_hp_charmander.place(x=15, y=350)

# Ataque Charmander
poke_ataque_charmander = Label(janela, text='Ataque: 300', relief='flat', anchor=CENTER,
                               font=('Verdana 10'), bg=co1, fg=co4)
poke_ataque_charmander.place(x=15, y=380)

# Defesa Charmander
poke_defesa_charmander = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER,
                               font=('Verdana 10'), bg=co1, fg=co4)
poke_defesa_charmander.place(x=15, y=410)

# Velocidade Charmander
poke_velocidade_charmander = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER,
                                   font=('Verdana 10'), bg=co1, fg=co4)
poke_velocidade_charmander.place(x=15, y=440)

# Total Charmander
poke_total_charmander = Label(janela, text='Total: 1200', relief='flat', anchor=CENTER,
                              font=('Verdana 10'), bg=co1, fg=co4)
poke_total_charmander.place(x=15, y=470)

# Habilidades 1 Charmander
poke_habilidade_charmander1 = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'),
                                    bg=co1, fg=co0)
poke_habilidade_charmander1.place(x=210, y=300)

# Habilidades 2 Charmander
poke_habilidade_charmander2 = Label(janela, text='Lança-chamas', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                    bg=co1, fg=co4)
poke_habilidade_charmander2.place(x=210, y=350)

# Habilidades 3 Charmander
poke_habilidade_charmander3 = Label(janela, text='Garra de Metal', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                    bg=co1, fg=co4)
poke_habilidade_charmander3.place(x=210, y=380)

# Habilidades 4 Charmander
poke_habilidade_charmander4 = Label(janela, text='Giro de Fogo', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                    bg=co1, fg=co4)
poke_habilidade_charmander4.place(x=210, y=410)

# criando o frame Dragonite
frame_pokemon_dragonite = Frame(janela, width=550, height=290, relief='flat', bg='#9932CC')
frame_pokemon_dragonite.grid(row=1, column=0)

# Nome Pokemon Dragonite
poke_nome_dragonite = Label(frame_pokemon_dragonite, text='Dragonite', relief='flat', anchor=CENTER,
                            font=('Fixedsys 20'), bg='#7CFC00', fg=co0)
poke_nome_dragonite.place(x=12, y=15)

# Tipo Pokemon Dragonite
poke_tipo_dragonite = Label(frame_pokemon_dragonite, text='Dragão/Voador', relief='flat', anchor=CENTER,
                            font=('Ivy 10 bold'), bg='#7CFC00', fg=co0)
poke_tipo_dragonite.place(x=12, y=50)

# Id Pokemon Dragonite
poke_id_dragonite = Label(frame_pokemon_dragonite, text='#149', relief='flat', anchor=CENTER,
                          font=('Ivy 10'), bg='#7CFC00', fg=co0)
poke_id_dragonite.place(x=12, y=75)

# Carregando a imagem do Dragonite em formato PNG
imagem_pokemon_dragonite = Image.open('images/dragonite.png')
imagem_pokemon_dragonite = imagem_pokemon_dragonite.resize((238, 238))
imagem_pokemon_dragonite = ImageTk.PhotoImage(imagem_pokemon_dragonite)

# Exibindo a imagem do Dragonite no frame
poke_imagem_dragonite = Label(frame_pokemon, image=imagem_pokemon_dragonite, relief='flat', bg='#7CFC00')
poke_imagem_dragonite.place(x=60, y=50)

poke_tipo_dragonite.lift()

# Status pokemon Dragonite
poke_status_dragonite = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_status_dragonite.place(x=15, y=300)

# Hp Dragonite
poke_hp_dragonite = Label(janela, text='HP: 100', relief='flat', anchor=CENTER,
                          font=('Verdana 10'), bg=co1, fg=co4)
poke_hp_dragonite.place(x=15, y=350)

# Ataque Dragonite
poke_ataque_dragonite = Label(janela, text='Ataque: 300', relief='flat', anchor=CENTER,
                              font=('Verdana 10'), bg=co1, fg=co4)
poke_ataque_dragonite.place(x=15, y=380)

# Defesa Dragonite
poke_defesa_dragonite = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER,
                              font=('Verdana 10'), bg=co1, fg=co4)
poke_defesa_dragonite.place(x=15, y=410)

# Velocidade Dragonite
poke_velocidade_dragonite = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER,
                                  font=('Verdana 10'), bg=co1, fg=co4)
poke_velocidade_dragonite.place(x=15, y=440)

# Total Dragonite
poke_total_dragonite = Label(janela, text='Total: 1200', relief='flat', anchor=CENTER,
                             font=('Verdana 10'), bg=co1, fg=co4)
poke_total_dragonite.place(x=15, y=470)

# Habilidades 1 Dragonite
poke_habilidade_dragonite1 = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'),
                                   bg=co1, fg=co0)
poke_habilidade_dragonite1.place(x=210, y=300)

# Habilidades 2 Dragonite
poke_habilidade_dragonite2 = Label(janela, text='Hiper Raio', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1,
                                   fg=co4)
poke_habilidade_dragonite2.place(x=210, y=350)

# Habilidades 3 Dragonite
poke_habilidade_dragonite3 = Label(janela, text='Vento Cortante', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                   bg=co1, fg=co4)
poke_habilidade_dragonite3.place(x=210, y=380)

# Habilidades 4 Dragonite
poke_habilidade_dragonite4 = Label(janela, text='Hiper Raio de Gelo', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                   bg=co1, fg=co4)
poke_habilidade_dragonite4.place(x=210, y=410)

# criando o frame Gengar
frame_pokemon_gengar = Frame(janela, width=550, height=290, relief='flat', bg='#9932CC')
frame_pokemon_gengar.grid(row=1, column=0)

# Nome Pokemon Gengar
poke_nome_gengar = Label(frame_pokemon_gengar, text='Gengar', relief='flat', anchor=CENTER,
                         font=('Fixedsys 20'), bg='#9932CC', fg=co0)
poke_nome_gengar.place(x=12, y=15)

# Tipo Pokemon Gengar
poke_tipo_gengar = Label(frame_pokemon_gengar, text='Fantasma/Venenoso', relief='flat', anchor=CENTER,
                         font=('Ivy 10 bold'), bg='#9932CC', fg=co0)
poke_tipo_gengar.place(x=12, y=50)

# Id Pokemon Gengar
poke_id_gengar = Label(frame_pokemon_gengar, text='#094', relief='flat', anchor=CENTER,
                       font=('Ivy 10'), bg='#9932CC', fg=co0)
poke_id_gengar.place(x=12, y=75)

# Carregando a imagem do Gengar em formato PNG
imagem_pokemon_gengar = Image.open('images/gengar.png')
imagem_pokemon_gengar = imagem_pokemon_gengar.resize((238, 238))
imagem_pokemon_gengar = ImageTk.PhotoImage(imagem_pokemon_gengar)

# Exibindo a imagem do Gengar no frame
poke_imagem_gengar = Label(frame_pokemon_gengar, image=imagem_pokemon_gengar, relief='flat', bg='#7CFC00')
poke_imagem_gengar.place(x=60, y=50)

poke_tipo_gengar.lift()

# Status pokemon Gengar
poke_status_gengar = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_status_gengar.place(x=15, y=300)

# Hp Gengar
poke_hp_gengar = Label(janela, text='HP: 100', relief='flat', anchor=CENTER,
                       font=('Verdana 10'), bg=co1, fg=co4)
poke_hp_gengar.place(x=15, y=350)

# Ataque Gengar
poke_ataque_gengar = Label(janela, text='Ataque: 300', relief='flat', anchor=CENTER,
                           font=('Verdana 10'), bg=co1, fg=co4)
poke_ataque_gengar.place(x=15, y=380)

# Defesa Gengar
poke_defesa_gengar = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER,
                           font=('Verdana 10'), bg=co1, fg=co4)
poke_defesa_gengar.place(x=15, y=410)

# Velocidade Gengar
poke_velocidade_gengar = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER,
                               font=('Verdana 10'), bg=co1, fg=co4)
poke_velocidade_gengar.place(x=15, y=440)

# Total Gengar
poke_total_gengar = Label(janela, text='Total: 1200', relief='flat', anchor=CENTER,
                          font=('Verdana 10'), bg=co1, fg=co4)
poke_total_gengar.place(x=15, y=470)

# Habilidades 1 Gengar
poke_habilidade_gengar1 = Label(janela, text='Habilidades', relief='flat', anchor=CENTER,
                                font=('Verdana 20'), bg=co1, fg=co0)
poke_habilidade_gengar1.place(x=210, y=300)

# Habilidades 2 Gengar
poke_habilidade_gengar2 = Label(janela, text='Hipnose', relief='flat', anchor=CENTER,
                                font=('Verdana 10'), bg=co1, fg=co4)
poke_habilidade_gengar2.place(x=210, y=350)

# Habilidades 3 Gengar
poke_habilidade_gengar3 = Label(janela, text='Bola Sombria', relief='flat', anchor=CENTER,
                                font=('Verdana 10'), bg=co1, fg=co4)
poke_habilidade_gengar3.place(x=210, y=380)

# Habilidades 4 Gengar
poke_habilidade_gengar4 = Label(janela, text='Soco Sombrio', relief='flat', anchor=CENTER,
                                font=('Verdana 10'), bg=co1, fg=co4)
poke_habilidade_gengar4.place(x=210, y=410)

# criando o frame Gyarados
frame_pokemon_gyarados = Frame(janela, width=550, height=290, relief='flat', bg='#4682B4')
frame_pokemon_gyarados.grid(row=1, column=0)

# Nome Pokemon Gyarados
poke_nome_gyarados = Label(frame_pokemon_gyarados, text='Gyarados', relief='flat', anchor=CENTER,
                           font=('Fixedsys 20'), bg='#4682B4', fg=co0)
poke_nome_gyarados.place(x=12, y=15)

# Tipo Pokemon Gyarados
poke_tipo_gyarados = Label(frame_pokemon_gyarados, text='Água/Voador', relief='flat', anchor=CENTER,
                           font=('Ivy 10 bold'), bg='#4682B4', fg=co0)
poke_tipo_gyarados.place(x=12, y=50)

# Id Pokemon Gyarados
poke_id_gyarados = Label(frame_pokemon_gyarados, text='#130', relief='flat', anchor=CENTER,
                         font=('Ivy 10'), bg='#4682B4', fg=co0)
poke_id_gyarados.place(x=12, y=75)

# Carregando a imagem do Gyarados em formato PNG
imagem_pokemon_gyarados = Image.open('images/gyarados.png')
imagem_pokemon_gyarados = imagem_pokemon_gyarados.resize((238, 238))
imagem_pokemon_gyarados = ImageTk.PhotoImage(imagem_pokemon_gyarados)

# Exibindo a imagem do Gyarados no frame
poke_imagem_gyarados = Label(frame_pokemon_gyarados, image=imagem_pokemon_gyarados, relief='flat', bg='#4682B4')
poke_imagem_gyarados.place(x=60, y=50)

poke_tipo_gyarados.lift()

# Status pokemon Gyarados
poke_status_gyarados = Label(janela, text='Status', relief='flat', anchor=CENTER,
                             font=('Verdana 20'), bg=co1, fg=co0)
poke_status_gyarados.place(x=15, y=300)

# Hp Gyarados
poke_hp_gyarados = Label(janela, text='HP: 100', relief='flat', anchor=CENTER,
                         font=('Verdana 10'), bg=co1, fg=co4)
poke_hp_gyarados.place(x=15, y=350)

# Ataque Gyarados
poke_ataque_gyarados = Label(janela, text='Ataque: 300', relief='flat', anchor=CENTER,
                             font=('Verdana 10'), bg=co1, fg=co4)
poke_ataque_gyarados.place(x=15, y=380)

# Defesa Gyarados
poke_defesa_gyarados = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER,
                             font=('Verdana 10'), bg=co1, fg=co4)
poke_defesa_gyarados.place(x=15, y=410)

# Velocidade Gyarados
poke_velocidade_gyarados = Label(janela, text='Velocidade: 300', relief='flat', anchor=CENTER,
                                 font=('Verdana 10'), bg=co1, fg=co4)
poke_velocidade_gyarados.place(x=15, y=440)

# Total Gyarados
poke_total_gyarados = Label(janela, text='Total: 1200', relief='flat', anchor=CENTER,
                            font=('Verdana 10'), bg=co1, fg=co4)
poke_total_gyarados.place(x=15, y=470)

# Habilidades 1 Gyarados
poke_habilidade_gyarados1 = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1,
                                  fg=co0)
poke_habilidade_gyarados1.place(x=210, y=300)

# Habilidades 2 Gyarados
poke_habilidade_gyarados2 = Label(janela, text='Cauda de Ferro', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                  bg=co1, fg=co4)
poke_habilidade_gyarados2.place(x=210, y=350)

# Habilidades 3 Gyarados
poke_habilidade_gyarados3 = Label(janela, text='Hidro Bomba', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1,
                                  fg=co4)
poke_habilidade_gyarados3.place(x=210, y=380)

# Habilidades 4 Gyarados
poke_habilidade_gyarados4 = Label(janela, text='Raio de Gelo', relief='flat', anchor=CENTER, font=('Verdana 10'),
                                  bg=co1, fg=co4)
poke_habilidade_gyarados4.place(x=210, y=410)


# Criando botões para pokemons

# Botão Pikachu
def mostrar_pikachu():
    botao_pikachu = Image.open('images/cabeca-pikachu.png')
    botao_pikachu = botao_pikachu.resize((35, 35))
    botao_pikachu = ImageTk.PhotoImage(botao_pikachu)


pikachu_button = Button(janela, image=botao_pikachu, text='Pikachu', width=150, relief='raised',
                        overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg='#ADFF2F')
pikachu_button.place(x=375, y=10)

# Botão Bulbasaur
botao_bulbasaur = Image.open('images/cabeca-bulbasaur.png')
botao_bulbasaur = botao_bulbasaur.resize((35, 35))
botao_bulbasaur = ImageTk.PhotoImage(botao_bulbasaur)

bulbasaur_button = Button(janela, image=botao_bulbasaur, text='Bulbasaur', width=150, relief='raised',
                          overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg='#98FB98')
bulbasaur_button.place(x=375, y=55)

# Botão Charmander
botao_charmander = Image.open('images/cabeca-charmander.png')
botao_charmander = botao_charmander.resize((35, 35))
botao_charmander = ImageTk.PhotoImage(botao_charmander)

charmander_button = Button(janela, image=botao_charmander, text='Charmander', width=150, relief='raised',
                           overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg='#F4A460')
charmander_button.place(x=375, y=100)

# Botão Dragonite
botao_dragonite = Image.open('images/cabeca-dragonite.png')
botao_dragonite = botao_dragonite.resize((35, 35))
botao_dragonite = ImageTk.PhotoImage(botao_dragonite)

dragonite_button = Button(janela, image=botao_dragonite, text='Dragonite', width=150, relief='raised',
                          overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg='#F5DEB3')
dragonite_button.place(x=375, y=145)

# Botão Gengar
botao_gengar = Image.open('images/cabeca-gengar.png')
botao_gengar = botao_gengar.resize((35, 35))
botao_gengar = ImageTk.PhotoImage(botao_gengar)

gengar_button = Button(janela, image=botao_gengar, text='Gengar', width=150, relief='raised',
                       overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg='#BA55D3')
gengar_button.place(x=375, y=190)

# Botão Gyarados
botao_gyarados = Image.open('images/cabeca-gyarados.png')
botao_gyarados = botao_gyarados.resize((35, 35))
botao_gyarados = ImageTk.PhotoImage(botao_gyarados)

gyarados_button = Button(janela, image=botao_gyarados, text='Gyarados', width=150, relief='raised',
                         overrelief=RIDGE, compound=LEFT, padx=5, anchor=NW, font=('Verdana 12'), bg='#ADD8E6')
gyarados_button.place(x=375, y=235)

janela.mainloop()
