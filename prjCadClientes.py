# Vinculando recursos ao projeto ------------------------------------
from tkinter import *
from tkinter import ttk #-> Para uso das grids
import sqlite3          #-> Definindo o driver do database


# Declarando frames -------------------------------------------------
root = Tk()

# Declarando classes ------------------------------------------------
class Funcs(): #-> não precisa do __init__ já que esta função não cria, será chamada pela Application()
     def limpa_tela(self):     #-> Função limpar dados dos objetos de entrada
          self.codigo_entry.delete(0, END)
          self.nome_entry.delete(0, END)
          self.telefone_entry.delete(0, END)
          self.cidade_entry.delete(0, END)
     def conecta_bd(self):     #-> Função conexão com o banco de dados SQLite3
          self.conn = sqlite3.connect("clientes.db")
          self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
      #-> Função para desconectar o banco de dados SQLite3
     def desconecta_bd(self):  #-> Função desconectar o banco de dados SQLite3
          self.conn.close(); print("Desconectando do banco de dados")
      #-> Função para criar o banco de dados SQLite3
     def monta_tabelas(self):  #-> Função criar as tabelas do sistema
            self.conecta_bd()
            #-> Criando as tabelas
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes(
                    cod INTEGER PRIMARY KEY,
                    nome_cliente CHAR(40) NOT NULL,
                    telefone INTEGER(20),
                    cidade CHAR(40)
                );
            """)
            self.conn.commit();print("Banco de dados criado.")
            self.desconecta_bd()
            self.select_lista()
            self.limpa_tela()
     def variaveis(self):      #-> Função disponibiliza variáveis registro cliente evitando redundância da código
          self.codigo = self.codigo_entry.get()
          self.nome = self.nome_entry.get()
          self.telefone = self.telefone_entry.get()
          self.cidade = self.cidade_entry.get()        
     def add_cliente(self):    #-> Função inserção de cliente
          #-> chama as variáveis para o INSERT
          self.variaveis()
          #-> conexão e inserção dos dados
          self.conecta_bd()
          self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
                VALUES (?,?,?); """, (self.nome, self.telefone, self.cidade))
          self.conn.commit()
          #-> revisando a tela: limpa os campos entry e faz releitura dos dados para GRID
          self.select_lista()
          self.limpa_tela()
          self.desconecta_bd()
     def select_lista(self):   #-> Função preencher dados cadastrados na GRID Cliente
            self.listacli.delete(*self.listacli.get_children())
            self.conecta_bd()
            lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
                ORDER BY nome_cliente ASC; """)
            for i in lista:
                self.listacli.insert("", END, values=i)
            self.desconecta_bd()
     def OnDoubleClick(self, event):  #-> Função seleção de registro via duplo click na GRID - note o 'event'...
          self.limpa_tela()
          self.listacli.selection()

          for n in self.listacli.selection():
               col1, col2, col3, col4 = self.listacli.item(n,'values')
               self.codigo_entry.insert(END, col1)
               self.nome_entry.insert(END, col2)
               self.telefone_entry.insert(END, col3)
               self.cidade_entry.insert(END, col4)
     def deleta_cliente(self): #-> Função para excluir um registro de cliente
            
            self.variaveis()
            self.conecta_bd()
            self.cursor.execute(""" DELETE FROM clientes WHERE cod=? """, [self.codigo])
            self.conn.commit()

            self.desconecta_bd()
            self.limpa_tela()
            self.select_lista()
     def altera_cliente(self): #-> Função para altear um registro de cliente
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
                            WHERE cod = ? """, (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()



class Application(Funcs): #-> note que esta classe pode usar a class Funcs
    #-> Ativando LOOP do código
    def __init__(self):       #-> ATENÇÃO na ordenação das chamadas, deve seguir as prioridade das funções
        self.root = root #-> Criando uma equivalência pois o 'root' está fora da class.
        self.tela()            # chama função tela
        self.frames_da_tela()  # chama função frames
        self.widgets_frame1()  # chama função botões
        self.lista_frame2()    # chama componentes contidos no frame_2
        self.monta_tabelas()   # cria tebalas caso não exista
        self.select_lista()    # preenche a GRID com registros dos clientes
        self.Menus()           # implementa os menus
        root.mainloop()
    def tela(self):           #-> Definições para a tela
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#000080') #-> NavyBlue
        self.root.geometry("700x500")
        self.root.resizable(True, True) #-> se reponsiva : Quando 'False' a tela fica travada.
        self.root.maxsize(width= 900,height=700)
        self.root.minsize(width= 500, height=400)
    def frames_da_tela(self): #-> Função para os frames
        self.frame_1 = Frame(self.root, bd=4, bg='#4682B4', highlightbackground='#2596be', 
                             highlightthickness=3) #-> SteelBlue - DarkSlateBlue
        # pack > mais básico, menos opções / grid > divide a tela em coordenadas  / place > possibilita a responsividade
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        # aqui foi usado percentual para posições, escala de 0 a 1 onde 0 é todo a esquerda e 1 todo a direita.
        self.frame_2 = Frame(self.root, bd=4, bg='#4682B4', highlightbackground='#2596be', 
                             highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self): #-> Função para criação dos widgets
            # Criação do botão limpar
            self.bt_limpar = Button(self.frame_1, text="Limpar", bd=3, bg='#483D8B', fg='white'
                                    , font=('verdana', 8, 'bold'), command=self.limpa_tela) #-> DarkSlateBlue 
            self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
            # Criação do botão buscar
            self.bt_buscar= Button(self.frame_1, text="Buscar", bd=3, bg='#483D8B', fg='white', font=('verdana', 8, 'bold'))
            self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
            # Criação do botão Novo
            self.bt_novo= Button(self.frame_1, text="Novo", bd=3, bg='#483D8B', fg='white'
                                 , font=('verdana', 8, 'bold'), command=self.add_cliente)
            self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
            # Criação do botão Alterar
            self.bt_alterar= Button(self.frame_1, text="Alterar", bd=3, bg='#483D8B', fg='white'
                                    , font=('verdana', 8, 'bold'), command=self.altera_cliente)
            self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
            # Criação do botão Apagar
            self.bt_apagar= Button(self.frame_1, text="Apagar", bd=3, bg='#483D8B', fg='white'
                                   , font=('verdana', 8, 'bold'), command=self.deleta_cliente)
            self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

            #-> Criação das labels e entradas do código
            self.lb_codigo = Label(self.frame_1, text="Código", bg='#4682B4', fg='black')
            self.lb_codigo.place(relx=0.05 ,rely=0.05)
            self.codigo_entry = Entry(self.frame_1, bg='#B0E0E6', fg='black') #-> PowderBlue
            self.codigo_entry.place(relx=0.05, rely=0.15, relwidth= 0.08)
    
            #-> Criação das labels e entradas do nome
            self.lb_nome = Label(self.frame_1, text="Nome", bg='#4682B4', fg='black')
            self.lb_nome.place(relx=0.05 ,rely=0.35)
            self.nome_entry = Entry(self.frame_1, bg='#B0E0E6', fg='black')
            self.nome_entry.place(relx=0.05, rely=0.45, relwidth= 0.8)    

            #-> Criação das labels e entradas do telefone
            self.lb_telefone = Label(self.frame_1, text="Telefone", bg='#4682B4', fg='black')
            self.lb_telefone.place(relx=0.05 ,rely=0.6)
            self.telefone_entry = Entry(self.frame_1, bg='#B0E0E6', fg='black')
            self.telefone_entry.place(relx=0.05, rely=0.7, relwidth= 0.18)

            #-> Criação das labels e entradas do Cidade
            self.lb_cidade = Label(self.frame_1, text="Cidade", bg='#4682B4', fg='black')
            self.lb_cidade.place(relx=0.5 ,rely=0.6)
            self.cidade_entry = Entry(self.frame_1, bg='#B0E0E6', fg='black')
            self.cidade_entry.place(relx=0.5, rely=0.7, relwidth= 0.35)
    def lista_frame2(self):   #-> Função para implementação no frame_2
         self.listacli = ttk.Treeview(self.frame_2, height=3, columns=("col1", "col2", "col3", "col4"))
         #-> Definindo as colunas
         self.listacli.heading("#0", text="") #-> esta coluna mesmo não usual, deve ser declarada...
         self.listacli.heading("#1", text="Código")
         self.listacli.heading("#2", text="Nome")
         self.listacli.heading("#3", text="Telefone")
         self.listacli.heading("#4", text="Cidade")
         #-> Definindo largura das colunas
         self.listacli.column("#0", width=1)
         self.listacli.column("#1", width=50)
         self.listacli.column("#2", width=200)
         self.listacli.column("#3", width=125)
         self.listacli.column("#4", width=125)
         #-> Posiciona o GRID
         self.listacli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
         #-> Implementando uma scroolbar na GRID 
         self.scroollista = Scrollbar(self.frame_2, orient='vertical')
         self.listacli.configure(yscroll=self.scroollista.set) #-> atribui o scrool ao GRID
         self.scroollista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
         self.listacli.bind("<Double-1>", self.OnDoubleClick)    
    def Menus(self): #-> Função cria menus
         menubar = Menu(self.root)
         self.root.config(menu=menubar)
         filemenu = Menu(menubar)
         filemenu2 = Menu(menubar)
         #-> Função dentro da função Menu, mas pode ser usada fora para reaproveitar o codigo
         def Quit(): self.root.destroy()

         menubar.add_cascade(label="Opções", menu= filemenu)
         menubar.add_cascade(label="Sobre", menu= filemenu2)

         filemenu.add_command(label="Limpa Cliente", command=self.limpa_tela)
         filemenu.add_command(label="Sair", command=Quit)



# Retorno LOOP do código --------------------------------------------
Application()