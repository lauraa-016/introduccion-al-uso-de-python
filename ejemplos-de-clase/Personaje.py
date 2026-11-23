class Personaje:
    def __init__(self, vida: int, ataque: int):
        if vida < 0 or ataque < 0:
            raise ValueError("La vida y el ataque no pueden ser negativos.")
        self.vida = vida
        self.ataque = ataque

    def recibir_dano(self, cantidad: int):
        self.vida = max(0, self.vida - cantidad)

    def atacar(self, objetivo: Personaje):
        objetivo.recibir_dano(self.ataque)

class Guerrero(Personaje):
    def atacar(self, objetivo: Personaje):
        objetivo.recibir_dano(self.ataque * 2)

class Mago(Personaje):
    def __init__(self, vida: int, ataque: int, mana: int):
        super().__init__(vida, ataque)
        if mana < 0:
            raise ValueError("El mana no puede ser negativo.")
        self.mana = mana

    def atacar(self, objetivo: Personaje):
        # El mago usa magia si tiene al menos 5 de mana; si no, hace un ataque normal.
        if self.mana >= 5:
            objetivo.recibir_dano(self.ataque * 3)
            self.mana -= 5
        else:
            objetivo.recibir_dano(self.ataque)


goku = Guerrero(vida=100, ataque=20)
ryu = Mago(vida=80, ataque=30, mana=10)

goku.atacar(ryu)
ryu.atacar(goku)
print(f"Goku - Vida: {goku.vida}, Ataque: {goku.ataque}")
print(f"Ryu - Vida: {ryu.vida}, Ataque: {ryu.ataque}")