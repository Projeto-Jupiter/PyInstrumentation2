QV = [0,0]

def QV_change_status(qv,i):
    change_status = input("Mudar status da Válvula? Responder com True or False \n")

    if change_status == "True":
        qv = not qv
        if qv:
            print("QV%d ativada" %(i+1))
        elif not qv:
            print("QV%d desativada" %(i+1))
    return int(qv)
    

try:
    print("Iniciar")
   
    while True:

        for i in range(len(QV)):
            print("QV%d" %(i+1))
            QV[i]=QV_change_status(QV[i],i)
            print("\n")


except KeyboardInterrupt:
    print("\nFim")
    print(QV)
