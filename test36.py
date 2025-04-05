import matplotlib.pyplot as plt

notes = ['note 1','note 2','note 3','note 4','note 5']
math = [14,16,18,15,12]
Pc = [10,13,15,17,11]
Svt = [9,12,14,15,18]

plt.ylim(8,20)

plt.plot(notes,math, marker='o',label='math')  # plt.plot(axe y, axe x)
plt.plot(notes,Pc, marker='o',label='Pc')
plt.plot(notes,Svt, marker='o',label='Svt')
 # marker= : '.' = point , 'o' = circle , 'p' = Pentagon , 'x' = Cross , 'v' = Triangle Down , '^' = Triangle Up .......
plt.title(".")  #title 
plt.ylabel("notes")  # titre d'axe y
plt.xlabel("Values")  # titre d'axe x

plt.legend() # afficher le coulor de chaque metier
plt.grid()  # les ligne

for i in range(len(notes)):
    plt.text(notes[i], math[i], float(math[i]),color="black",rotation=0,fontsize=10, ha='left', va='center',bbox=dict(facecolor='white',alpha=0.4)) # plt.text(axe x , axe y,type(l'element voir)  )
    plt.text(notes[i], Pc[i], float(Pc[i]),color="black",rotation=0,fontsize=10, ha='left', va='center',bbox=dict(facecolor='white',alpha=0.4))
    plt.text(notes[i], Svt[i], float(Svt[i]),color="black",rotation=0,fontsize=10, ha='left', va='center',bbox=dict(facecolor='white',alpha=0.4))
            # color="red" : coulor du text ou nombre afficher
            # fontsize=00 : fontssize du text ou nombre afficher
            # ha='center' ou 'left' ou 'right' : Alignement horizontal de text ou nombre que ty affiche
            # ha='center' ou 'top' ou 'bottom' : Alignement vertical de text ou nombre que tu affiche
            # rotation=00 : Rotation du texte en degrés
            #bbox=dict(facecolor='white') .affiche un cadre un text ou nombre ,  white : background-color de cadre
            # bbox=dict(alpha=0.4) , alpha : opacity de cadre
            # plt.plot(marker='o') : affiche un point a la place vous precise .exemple du note
plt.show()


