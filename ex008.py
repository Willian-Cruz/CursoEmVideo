#Escreva um programa que leia um valor em metros e converta para Km, Hm, Dam, Dm, Cm, Mm.
metros = float(input("Valor em metros: "))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print("O valor de {} metros equivale a: \n{}km, \n{}hm, \n{}dam, \n{}dm, \n{}cm, \n{}mm".format(metros, km, hm, dam, dm, cm, mm))