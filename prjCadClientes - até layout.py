# Vinculando recursos ao projeto ------------------------------------
from tkinter import *
from tkinter import ttk #-> Para uso das grids


# Declarando frames -------------------------------------------------
root = Tk()

# Declarando classes ------------------------------------------------
class Funcs(): #-> não precisa do __init__ já que esta função não cria, será chamada pela Application()
     def limpa_tela(self):
          self.codigo_entry.delete(0, END)
          self.nome_entry.delete(0, END)
          self.telefone_entry.delete(0, END)
          self.cidade_entry.delete(0, END)
     

class Application(Funcs): #-> note que esta classe pode usar a class Funcs
    #-> Ativando LOOP do código
    def __init__(self):  #-> ATENÇÃO na ordenação das chamadas, deve seguir as prioridade das funções
        self.root = root #-> Criando uma equivalência pois o 'root' está fora da class.
        self.tela()            # chama função tela
        self.frames_da_tela()  # chama função frames
        self.widgets_frame1()  # chama função botões
        self.lista_frame2()    # chama componentes contidos no frame_2
        root.mainloop()
    #-> Definições para a tela
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#000080') #-> NavyBlue
        self.root.geometry("700x500")
        self.root.resizable(True, True) #-> se reponsiva : Quando 'False' a tela fica travada.
        self.root.maxsize(width= 900,height=700)
        self.root.minsize(width= 500, height=400)
    #-> Função para os frames
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#4682B4', highlightbackground='#2596be', 
                             highlightthickness=3) #-> SteelBlue - DarkSlateBlue
        # pack > mais básico, menos opções / grid > divide a tela em coordenadas  / place > possibilita a responsividade
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        # aqui foi usado percentual para posições, escala de 0 a 1 onde 0 é todo a esquerda e 1 todo a direita.
        self.frame_2 = Frame(self.root, bd=4, bg='#4682B4', highlightbackground='#2596be', 
                             highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    #-> Função para criação dos botões
    def widgets_frame1(self):
            # Criação do botão limpar
            self.bt_limpar = Button(self.frame_1, text="Limpar", bd=3, bg='#483D8B', fg='white'
                                    , font=('verdana', 8, 'bold'), command=self.limpa_tela) #-> DarkSlateBlue 
            self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
            # Criação do botão buscar
            self.bt_buscar= Button(self.frame_1, text="Buscar", bd=3, bg='#483D8B', fg='white', font=('verdana', 8, 'bold'))
            self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
            # Criação do botão Novo
            self.bt_novo= Button(self.frame_1, text="Novo", bd=3, bg='#483D8B', fg='white', font=('verdana', 8, 'bold'))
            self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
            # Criação do botão Alterar
            self.bt_alterar= Button(self.frame_1, text="Alterar", bd=3, bg='#483D8B', fg='white', font=('verdana', 8, 'bold'))
            self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
            # Criação do botão Apagar
            self.bt_apagar= Button(self.frame_1, text="Apagar", bd=3, bg='#483D8B', fg='white', font=('verdana', 8, 'bold'))
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
    #-> Função para implementação no frame_2
    def lista_frame2(self):
         
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


# Retorno LOOP do código --------------------------------------------
Application()