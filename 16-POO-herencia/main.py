import clases

persona = clases.persona()
persona.setnombre("Miguel")
persona.setapellido("Rodriguez")
persona.setaltura("175cm")
persona.setedad("22 años")

print(f"La persona es: {persona.getnombre()} {persona.getapellido()}")
print(persona.hablar())