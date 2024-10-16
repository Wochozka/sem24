#!/usr/bin/env python3

class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka
    
    def _vykresli(self):
        self._vycisti()
        print('----------------- Arena ----------------- \n')
        print('Bojovníci: \n')
        self._vypis_bojovnika(self._bojovnik_1)
        self._vypis_bojovnika(self._bojovnik_2)
    
    def _vycisti(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subprocess.call(['clear'])

    def _vypis_bojovnika(self, bojovnik):
        print(bojovnik)
        print(f'Zivot: {bojovnik.graficky_zivot()}')
        if isinstance(bojovnik, Mag):
            print(f'Mana: {bojovnik.graficka_mana()}')

    def _vypis_zpravu(self, zprava):
        print()
        print(zprava)
        import time as _time
        _time.sleep(0.5)
    
    def zapas(self):
        print('Vítejte v Areně!')
        print(f'Dnes se utkají {self._bojovnik_1} a {self._bojovnik_2}!')
        print('Zápas může začít...', end=' ')
        input()

        import random as _random
        if _random.randint(0,1):
            self._bojovnik_1, self._bojovnik_2 = self._bojovnik_2, self._bojovnik_1

        while self._bojovnik_1.nazivu and self._bojovnik_2.nazivu:
            self._bojovnik_1.utoc(self._bojovnik_2)
            self._vykresli()
            self._vypis_zpravu(self._bojovnik_2.get_zprava())
            if self._bojovnik_2.nazivu:
                self._bojovnik_2.utoc(self._bojovnik_1)
                self._vykresli()
                self._vypis_zpravu(self._bojovnik_1.get_zprava())

if __name__ == '__main__':
    from kostka import Kostka
    from bojovnik import Bojovnik
    from bojovnik import Mag
    k = Kostka(10)
    b1 = Bojovnik('Honza', 100, 20, 10, k)
    b2 = Mag('Jenik', 60, 18, 15, k, 40, 40)

    a = Arena(b1, b2, k)
    a.zapas()
