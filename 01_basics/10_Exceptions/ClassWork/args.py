import argparse

def create_args():
    parser = argparse.ArgumentParser(
    prog="BTC_calculator",
    description="un program care acumuleaza date destre bitcoin."
    )
    parser.add_argument(
         'flow', 
         type=str, 
         choices=['harvest', 'exchange'], 
         help = "Alege ceva din alea doua", 
    )
    parser.add_argument(
         '--timeout', 
         type=int, 
         default=60, 
         help = "Timeout pentru refresh la date, minim 60.", 
    )
    parser.add_argument(
         '--target', 
         type=str, 
         choices=['USD', 'BTC'], 
         help = "Converteste USD in BTC la peret curent si invers.", 
    )
    parser.add_argument(
         '--amount', 
         type=float, 
         help = "Cantitatea de BTC sau USD de convertit", 
    )
    return parser.parse_args()