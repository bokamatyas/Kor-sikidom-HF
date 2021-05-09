import math
from typing import List


def kör_kalkulkál(sugár: float) -> List:
    kerület = sugár * 2 * math.pi
    terület = math.pow(sugár, 2) * math.pi
    if sugár <= 0:
        print('=====================================')
        print('A sugár értéke nem lehet 0 vagy negatív szám!')
        exit()
    return [round(kerület, 3), round(terület, 3)]


print('Kör terület-kerület számító program')
print('=====================================')


def main() -> None:
    sugár = float(input('Kérem a kör sugarát cm-ben: '))
    eredmény = kör_kalkulkál(sugár)
    print('=====================================')
    print(f'A kör kerülete/területe: {eredmény}')


if __name__ == '__main__':
    main()
