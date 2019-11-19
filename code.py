class Titanic():
    def __init__(self):
        self.registro = self.load()

    def load(self):
        registro = {'homem_vivo':0, 'homem_morto':0, 'mulher_vivo':0, 'mulher_morto':0, 'total_vivo':0, 'total_morto':0}
        print(registro)
        arq=open('train.csv','r')
        linha=arq.readline()
        while linha != '':
            meta_dado = linha[:-1].split(',') #vivo ou morto 1,  # sexo 5
            registro = self.dados(meta_dado,registro)
            linha=arq.readline()
        print(registro)
        return registro 

    def dados(self,lista,registro):
        #morto Vivo
        if(lista[1]=='0'):
            registro['total_morto']=registro['total_morto']+1
            if(lista[5]=='male'):
                registro['homem_morto']=registro['homem_morto']+1
            else:
               registro['mulher_morto']=registro['mulher_morto']+1           
        else:
            registro['total_vivo']=registro['total_vivo']+1
            if(lista[5]=='male'):
                registro['homem_vivo']=registro['homem_vivo']+1
            else:
               registro['mulher_vivo']=registro['mulher_vivo']+1
        return registro

    def sendo_homem_vivo(self):
        registro=self.registro
        total = registro['total_morto'] + registro['total_vivo']
        prob_viver = registro['total_vivo'] / total
        prob_homem = (registro['homem_vivo'] + registro['homem_morto'])/total
        prob_homem_vivo = registro['homem_vivo'] / (registro['homem_vivo']+registro['mulher_vivo'])

        return (prob_homem_vivo * prob_homem)/prob_viver

t=Titanic()
print(t.registro)
print(t.sendo_homem_vivo())