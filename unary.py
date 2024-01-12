_input = input()

def unary(text):

    texte_initial=""

    #s'assurer que chaque ascii est à 7 bits
    for i in text:
        texte_initial+=str(bin(ord(i)))[2:].zfill(7)

    digit_de_liste=texte_initial[0]#variable de passe-passe entre 0 et 1
   
    liste_definitif=[digit_de_liste]#liste pour tous les textes temporaires
    q=0#variable pour conter le nombre de digits dans un texte temporaire
    
    unary=[]#liste de séquence 0 pour le texte unaire
    for j in range(1,len(texte_initial)):
        #si le digit n'est plus le même qu'avant 
        #créer un nouveau texte temporaire
        if texte_initial[j]!=digit_de_liste:
            digit_de_liste=texte_initial[j]
            q=0

        q+=1#pour conter le nombre de séquence 

        #un texte temporaire pour une séquence
        texte_temporaire=digit_de_liste*q

        #pour éviter les répétitions avant d'arriver à la dernière forme
        if liste_definitif[-1] in texte_temporaire:
            liste_definitif.pop()
            liste_definitif.append(texte_temporaire)

        else:
            liste_definitif.append(texte_temporaire)

    for text in liste_definitif:
        if text[0]=='0':
            unary.append("00 "+'0'*len(text))
        else:
            unary.append("0 "+'0'*len(text))
    
    textunary=" ".join(unary)#convertir la liste unaire en texte unaire
    return textunary

print(unary(_input))
