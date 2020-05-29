larg =  float(input("Qual a largura da parede? "))
alt = float(input("Qual a altura da parede? "))
area = larg * alt
tinta = area / 2
print("Sua parede tem {}m x {}m e a área equivale a {:.2f}m² \n"
      "Para pintar essa parede você precisará de {}l de tinta" .format(larg, alt, area, tinta))
