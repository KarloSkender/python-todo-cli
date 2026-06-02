

def main():
 tasks=[]
 done=[]
 menu=[("1.Add Task"),("2.Show Tasks"),("3.Mark Tasks as doned"),("4.Exit")]
 while True:
   for i in range(0,4):
     print(menu[i])
   choose=input("Odaberite broj koji zelite: ")
   if choose=="1":
     tasks.append(input("Unesite zadatak na listu: "))
     continue
   if choose=="2":
      print("Ovo su tvoji zadaci: ")
      for i in range(len(tasks)):
       print(f"{i+1}. {tasks[i]}")
       print()
      continue
   if choose=="3":
     if len(tasks)==0:
       print("Nemozete nista rijesiti kada je lista prazna!")
       continue
     for i in range(len(tasks)):
       print(f"{i+1}. {tasks[i]}")
     print()
     i=input("Unesi broj stvari koju si obavio : ")
     if not i.isdigit():
       print("Unijeli ste nesto sto nije broj,pokusajte opet")
       continue
     i=int(i)
     
     
     if i>len(tasks) or i <1:
       print("Unesite broj koji vidite na listi!!!")
       continue
     done.append(tasks[i-1])
     tasks.remove(tasks[i-1])
   if choose=="4":
     break
     
   
   
 
if __name__ == "__main__":
    main()