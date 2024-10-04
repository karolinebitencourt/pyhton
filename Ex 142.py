class Pet:


    def __init__(self):
        self._nome=''
        self._idade=0
        self._peso=0

    def get_nome(self):
        return self._nome

    def set_nome(self,name):
        if isinstance(name, str) and name!='':
            self._nome = name
        else:
            print('Nome inválido')

    def get_idade(self):
        return self._idade

    def set_idade(self,age):
        if isinstance(age,int) and age!=0:
            self._idade = age

        else:
            print('Idade inválida!')

    def get_peso(self):
        return self._peso

    def set_peso(self,weight):
        if isinstance(weight, float) and weight > 0:
            self._peso = weight
        else:
            print('Peso inválido!')

    def exibir_info(self):

        print('='*5,'INFORMAÇÕES DO MEU PET','='*5)
        print(f'Nome: {meu_pet.get_nome()}')
        print(f'Idade: {meu_pet.get_idade()}')
        print(f'Peso: {meu_pet.get_peso()}')
        print('-'*35)




meu_pet=Pet()
meu_pet.set_nome(input('Digite o nome do animal >>> '))
meu_pet.set_peso(9.5)
meu_pet.set_idade(5)
meu_pet.exibir_info()

