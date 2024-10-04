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
        print(f'Idade: {meu_pet.get_idade()} ano(s)')
        print(f'Peso: {meu_pet.get_peso()} kg(s)')
        print('-'*35)

    def menu(self):

        while True:
            print('=' * 15, 'CADASTRO DO PET', '=' * 15)
            print('1. Definir o nome do PET')
            print('2. Definir idade do PET')
            print('3. Definir o peso do PET')
            print('4. Exibir informações do PET')
            print('5. Sair')
            print('-' * 40)
            op = input('Selecione uma opçào >>> ')
            if op=='1':
                print('º'*40)
                meu_pet.set_nome(input('Nome do PET: '))

            elif op=='2':
                print('º'*40)
                meu_pet.set_idade(int(input('Idade do PET: ')))

            elif op=='3':
                print('º'*40)
                meu_pet.set_peso(float(input('Peso do PET: ')))

            elif op=='4':
                print('º'*40)
                meu_pet.exibir_info()

            elif op=='5': break





meu_pet=Pet()
meu_pet.menu()
print('='*40)
print('='*15,'ATÉ A PRÓXIMA','='*15)

