import ast
import os
path = str(os.environ['USERPROFILE'])
folder = str(path+"/Desktop/Pre-entrega 2/Usuarios.txt")
print(folder)

global datos
global usuarios

class clientes:
  def __init__(self,nombre="",email="",password=""):
    self.nombre_ = nombre
    self.email_ = email
    self.password_ = password
  def agregar_cliente(self,nombre,email,password):
    self.nombre_ = nombre
    self.email_ = email
    self.password_ = password
  def obtener_cliente(self):
    datos ={"nombre":self.nombre_, "email":self.email_, "password":self.password_}
    return datos
  def __str__(self):
    return "nombre "+str(self.nombre_)+" email "+str(self.email_)+" password "+str(self.password_)
  def mensaje_bienvenida(self):
    return "Sea Bienvenido "+str(self.nombre_)+" a esta pagina."

usuarios={}
def nuevo_cliente():
  nombre=input("Ingrese su nombre: ")
  email=input("Ingrese su Email: ")
  password=input("Ingrese su password: ")
  dic_usuario={"nombre":nombre,"email":email,"password":password}
  if(dic_usuario["nombre"].__len__() > 0 and dic_usuario["email"].__len__() > 0 and dic_usuario["password"].__len__() > 0 ):
    cliente=clientes()
    cliente.agregar_cliente(nombre,email,password)
    usuarios[cliente] = cliente.obtener_cliente()
    print(str(cliente.__str__())+"Fue creado con Exito. ")
  else:
    print("Faltan datos por ingresa. ")

def login():
  email=input("Ingrese su Email: ")
  password=input("Ingrese su password: ")
  for var_user in usuarios:
    if(email==usuarios[var_user]["email"]):
      if(password==usuarios[var_user]["password"]):
        print("Bienvenido "+str(usuarios[var_user]["nombre"]))

nuevo_cliente()
login()

folder_read = open(folder, 'r')
usuarios = folder_read.read()
usuarios = ast.literal_eval(usuarios)
folder_read.close()
print(usuarios)