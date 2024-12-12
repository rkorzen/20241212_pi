import argparse

parser = argparse.ArgumentParser(description="Obliczenia inzynierskie - parametry belki")

parser.add_argument("width", type=float, help="Szerokość belki (w cm)")
parser.add_argument("height", type=float, help="Wysokość belki (w cm)")
parser.add_argument("length", type=float, help="Długość belki (w cm)")


args = parser.parse_args()

volume = args.width * args.height * args.length

print(f"Objetosc: {volume} cm^3")
