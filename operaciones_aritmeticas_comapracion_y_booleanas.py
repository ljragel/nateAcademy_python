

apetece_helado=input("¿Te apetece heleado?(SI/NO)").upper()
tiene_dinero=input("¿Tienes dinero para pagar el helado?(SI/NO)").upper()

if apetece_helado=="SI" and tiene_dinero== "SI":
    print("tome su helado que ha pedido")
elif apetece_helado=="SI" and tiene_dinero=="NO":
    print("puedes irte por donde has venido perdazo de gorron")
elif apetece_helado=="NO":
    print("nose que haces aqui entonces pedazo de tono")