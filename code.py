class Titanic():
    def __init__(self):
        self.analise_classe_social = {'ticket_especial_morto':0, 'ticket_especial_vivo':0, 'ticket_caro_morto':0, 'ticket_caro_vivo':0, 'ticket_medio_morto':0, 'ticket_medio_vivo':0, 'ticket_barato_morto':0, 'ticket_barato_vivo':0 }
        self.analise_sexo = {'homem_vivo':0, 'homem_morto':0, 'mulher_vivo':0, 'mulher_morto':0, 'total_vivo':0, 'total_morto':0}
        self.analise_idade = {  'crianca_vivo':0, 'crianca_morto':0, 'adulto_vivo':0, 'adulto_morto':0, 'idoso_vivo':0, 'idoso_morto':0,'indeterminado_vivo':0, 'indeterminado_morto':0}
        self.total_morto = 0
        self.total_vivo = 0
        self.load()
        
    def load(self):        
        arq=open('train.csv','r')
        linha=arq.readline()
        linha=arq.readline()
        while linha != '':
            meta_dado = linha[:-1].split(',') 
            #vivo[0] ou morto[1] 1, #classe social[0,1,2,3] 2, #name1 3, #name 2 4, # sexo 5, #idade 6
            self.metricas_sexo(meta_dado)
            #self.metricas_idade(meta_dado)
            self.metricas_classe_social(meta_dado)
            linha=arq.readline()
        
        return None

    def metricas_sexo(self,lista):
        #morto Vivo
        if(lista[1]=='0'):
            self.total_morto=self.total_morto+1
            if(lista[5]=='male'):
                self.analise_sexo['homem_morto']=self.analise_sexo['homem_morto']+1
            else:
                self.analise_sexo['mulher_morto']=self.analise_sexo['mulher_morto']+1
        elif (lista[1]=='1'):
            self.total_vivo=self.total_vivo+1
            if(lista[5]=='male'):
                self.analise_sexo['homem_vivo']=self.analise_sexo['homem_vivo']+1
            else:
                self.analise_sexo['mulher_vivo']=self.analise_sexo['mulher_vivo']+1
        else:
            print('erro')        
            input()
        return None

    def metricas_idade(self,lista):
        # indetermidado, criança até 15, adulto 16 até 69, idoso 70 pra cima.
        print(lista[6])
        idade=float(lista[6])

        if(int(lista[1])=='0'):            
            if(lista[6]==''):
                self.analise_idade['indeterminado_morto'] = self.analise_idade['indeterminado_morto'] + 1
            elif(idade<16):
                self.analise_idade['crianca_morto'] = self.analise_idade['crianca_morto'] + 1       
            elif(idade<70):
                self.analise_idade['adulto_morto'] = self.analise_idade['adulto_morto'] + 1
            else:
                self.analise_idade['idoso_morto'] = self.analise_idade['idoso_morto'] + 1                                  
        else:
            if(lista[6]==''):
                self.analise_idade['indeterminado_vivo'] = self.analise_idade['indeterminado_vivo'] + 1
            elif(idade<16):
                self.analise_idade['crianca_vivo'] = self.analise_idade['crianca_morto'] + 1       
            elif(idade<70):
                self.analise_idade['adulto_vivo'] = self.analise_idade['adulto_vivo'] + 1
            else:
                self.analise_idade['idoso_vivo'] = self.analise_idade['idoso_vivo'] + 1                                  
        return None

    def metricas_classe_social(self,lista):
        classe=int(lista[2])
        if lista[1]=='0':
            if classe==3:
                self.analise_classe_social['ticket_especial_morto'] = self.analise_classe_social['ticket_especial_morto']+1
            elif classe==2:
                self.analise_classe_social['ticket_caro_morto'] = self.analise_classe_social['ticket_caro_morto']+1
            elif classe==1:
                self.analise_classe_social['ticket_medio_morto'] =self.analise_classe_social['ticket_medio_morto']+1
            else:
                self.analise_classe_social['ticket_barato_morto'] = self.analise_classe_social['ticket_barato_morto']+1
        elif lista[1]=='1':
            if classe==3:
                self.analise_classe_social['ticket_especial_vivo'] = self.analise_classe_social['ticket_especial_vivo']+1
            elif classe==2:
                self.analise_classe_social['ticket_caro_vivo'] = self.analise_classe_social['ticket_caro_vivo']+1
            elif classe==1:
                self.analise_classe_social['ticket_medio_vivo'] =self.analise_classe_social['ticket_medio_vivo']+1
            else:
                self.analise_classe_social['ticket_barato_vivo']=self.analise_classe_social['ticket_barato_vivo']+1
        else:
            print(lista)
            input()        
        return None


    def dado_homem_estar_vivo(self):
        registro=self.analise_sexo
        total = registro['total_morto'] + registro['total_vivo']
        prob_viver = registro['total_vivo'] / total                                                 #P(a)        
        prob_homem = (registro['homem_vivo'] + registro['homem_morto'])/total                       #P(b)        
        prob_homem_vivo = registro['homem_vivo'] / (registro['homem_vivo']+registro['mulher_vivo']) #P(b|a)
        p_a, p_b, p_ba = prob_viver, prob_homem, prob_homem_vivo
        return (p_ba * p_a)/p_b

    def dado_homem_estar_morto(self):
        registro=self.analise_sexo
        total = registro['total_morto'] + registro['total_vivo']
        prob_morreu_homem = registro['homem_morto']/registro['total_morto']
        prob_morrer       = registro['total_morto']/total
        prob_homem        = (registro['homem_vivo'] + registro['homem_morto'])/total  
        p_a, p_b, p_ba = prob_morrer,prob_homem,prob_morreu_homem
        return (p_ba * p_a)/p_b

    def dado_mulher_estar_vivo(self):
        return None     
    
    def dado_mulher_estar_morto(self):
        return None


t = Titanic()
print(t.total_vivo+t.total_morto)
print(t.analise_idade)


print('Analise de classe social')
count=0
for elem in t.analise_classe_social:
    print(elem)
    print(t.analise_classe_social[elem])
    count=count+t.analise_classe_social[elem]
print(count)    
