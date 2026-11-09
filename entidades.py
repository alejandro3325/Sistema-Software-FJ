from abc import ABC, abstractmethod

class Entidad(ABC):
  def __init__(self, identificador):
    #aca se guarda el identificador
    
    @abstractmethod
    def mostra_informacion(self):
      pass
