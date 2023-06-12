import time
from datetime import datetime
from tools import *
from args import create_args

args = create_args()
print(args, args.flow, args.timeout)

if args.flow == "harvest":
    if args.timeout < 60:
        raise ValueError(
            f"Timeout sa fie minim 60, iar tu ai introdus {args.timeout}"
        )
    harvest(args.timeout)
elif args.flow == "exchange":
    exchange(args.target, args.amount)

