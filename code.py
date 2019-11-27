
class Titanic():
    def __init__(self):
        self.analise_classe_social = {'ticket_caro_morto':0, 'ticket_caro_vivo':0, 
        'ticket_medio_morto':0, 'ticket_medio_vivo':0, 'ticket_barato_morto':0, 'ticket_barato_vivo':0}
        self.analise_sexo = {'homem_vivo':0, 'homem_morto':0, 'mulher_vivo':0, 'mulher_morto':0}
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
        
    def metricas_classe_social(self,lista):
        classe=int(lista[2])
        if lista[1]=='0':
            if classe==3:
                self.analise_classe_social['ticket_caro_morto'] = self.analise_classe_social['ticket_caro_morto']+1
            elif classe==2:
                self.analise_classe_social['ticket_medio_morto'] =self.analise_classe_social['ticket_medio_morto']+1
            elif classe==1:
                self.analise_classe_social['ticket_barato_morto'] = self.analise_classe_social['ticket_barato_morto']+1
        elif lista[1]=='1':
            if classe==3:
                self.analise_classe_social['ticket_caro_vivo'] = self.analise_classe_social['ticket_caro_vivo']+1
            elif classe==2:
                self.analise_classe_social['ticket_medio_vivo'] =self.analise_classe_social['ticket_medio_vivo']+1
            elif classe==1:
                self.analise_classe_social['ticket_barato_vivo']=self.analise_classe_social['ticket_barato_vivo']+1
        else:
            print(lista)
            input()        
        return None


    def dado_homem_estar_vivo(self):
        registro=self.analise_sexo
        total = self.total_morto + self.total_vivo
        prob_viver = self.total_vivo  / total                                                       #P(a)        
        prob_homem = (registro['homem_vivo'] + registro['homem_morto'])/total                       #P(b)        
        prob_homem_vivo = registro['homem_vivo'] /  self.total_vivo                                 #P(b|a)
        p_a, p_b, p_ba = prob_viver, prob_homem, prob_homem_vivo
        return (p_ba * p_a)/p_b

    def dado_homem_estar_morto(self):
        registro=self.analise_sexo
        total = self.total_morto + self.total_vivo
        prob_morreu_homem = registro['homem_morto']/self.total_morto
        prob_morrer       = self.total_morto/total
        prob_homem        = (registro['homem_vivo'] + registro['homem_morto'])/total  
        p_a, p_b, p_ba = prob_morrer,prob_homem,prob_morreu_homem
        return (p_ba * p_a)/p_b

    def dado_mulher_estar_vivo(self):
        registro=self.analise_sexo
        total = self.total_morto + self.total_vivo
        prob_vivo_mulher = registro['mulher_vivo']/self.total_vivo
        prob_sobreviver = self.total_vivo/total
        prob_mulher = (registro['mulher_vivo'] + registro['mulher_morto'])/total
        p_a, p_b, p_ba = prob_sobreviver, prob_mulher, prob_vivo_mulher
        return (p_ba * p_a)/p_b
    
    def dado_mulher_estar_morto(self):
        registro=self.analise_sexo
        total = self.total_morto + self.total_vivo
        prob_morreu_mulher = registro['mulher_morto']/self.total_morto
        prob_morrer = self.total_morto/total
        prob_mulher = (registro['mulher_vivo'] + registro['mulher_morto'])/total
        p_a, p_b, p_ba = prob_morrer, prob_mulher, prob_morreu_mulher
        return (p_ba * p_a)/p_b

    def dado_caro_estar_vivo(self):
        registro = self.analise_classe_social
        total = self.total_morto + self.total_vivo
        prob_vivo_ticketcaro = registro['ticket_caro_vivo']/self.total_vivo
        prob_sobreviver = self.total_vivo/total
        prob_ticketcaro = (registro['ticket_caro_vivo'] + registro['ticket_caro_morto'])/total
        p_a, p_b, p_ba =prob_sobreviver,prob_ticketcaro,prob_vivo_ticketcaro
        return  (p_ba * p_a)/p_b#str(p_ba)+"*"+str(p_a)+'/'+str(p_b)    #

    def dado_caro_estar_morto(self):
        return 1-self.dado_caro_estar_vivo()

    def dado_medio_estar_vivo(self):
        registro = self.analise_classe_social
        total = self.total_morto + self.total_vivo
        prob_vivo_ticketmedio = registro['ticket_medio_vivo']/self.total_vivo
        prob_sobreviver = self.total_vivo/total
        prob_ticketmedio = (registro['ticket_medio_vivo'] + registro['ticket_medio_morto'])/total
        p_a, p_b, p_ba =prob_sobreviver,prob_ticketmedio,prob_vivo_ticketmedio
        return ((p_ba * p_a)/p_b)

    def dado_medio_estar_morto(self):
        return 1-self.dado_medio_estar_vivo()

    def dado_barato_estar_vivo(self):            
        registro = self.analise_classe_social
        total = self.total_morto + self.total_vivo
        prob_vivo_ticketbarato = registro['ticket_barato_vivo']/self.total_vivo
        prob_sobreviver = self.total_vivo/total
        prob_ticketbarato = (registro['ticket_barato_vivo'] + registro['ticket_barato_morto'])/total
        p_a, p_b, p_ba =prob_sobreviver,prob_ticketbarato,prob_vivo_ticketbarato
        return (p_ba * p_a)/p_b

    def dado_barato_estar_morto(self):       
        return 1-self.dado_barato_estar_vivo()

def menu():
    opcao=1
    t = Titanic()
    print(t.analise_classe_social)
    print(t.analise_sexo)
    while opcao==1 or opcao==2 :
        print (' 1-Analise por sexo \n 2-Analise por Classe social ')
        opcao = int(input('Digite a opcão desejada '))
        if opcao==1:
            print(t.analise_sexo)
            print('Dado que é homem qual a probabilidade de  NAO SOBREVIVER ao evento '+str(t.dado_homem_estar_morto()*100)+" %\n" )            
            print('Dado que é homem qual a probabilidade de SOBREVIVER ao evento '+str(t.dado_homem_estar_vivo()*100)+" %\n")
            print('Dado que é homem qual a probabilidade de  NAO SOBREVIVER ao evento '+str(t.dado_mulher_estar_morto()*100)+" %\n" )
            print('Dado que é MULHER qual a probabilidade de SOBREVIVER ao evento '+str(t.dado_mulher_estar_vivo()*100)+" %\n")
        elif opcao==2:
            print('Dado que seu ticket é CARO qual a prob de SOBREVIVER '+str(t.dado_caro_estar_vivo())+" %\n")
            print('Dado que seu ticket é CARO qual a prob de NAO SOBREVIVER ' +str(t.dado_caro_estar_morto()) +" %\n" )
            print('Dado que seu ticket é MEDIO qual a prob de SOBREVIVER '+str(t.dado_medio_estar_vivo())+" %\n")
            print('Dado que seu ticket é MEDIO qual a prob de NAO SOBREVIVER '+str(t.dado_medio_estar_morto())+" %\n")
            print('Dado que seu ticket é BARATO qual a prob de SOBREVIVER '+str(t.dado_barato_estar_vivo())+" %\n" )
            print('Dado que seu ticket é BARATO qual a prob de NAO SOBREVIVER '+str(t.dado_barato_estar_morto())+" %\n")         
            
        print('\n\n')

menu()