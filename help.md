```python
parser = ArgumentParser()

# Make arguments not run together
group = parser.add_mutually_exclusive_group()

# Describe header
parser.usage = "Positional args and optional flags"

parser.add_argument("echo", help="Just prints the given string", type=str, default="Yemi", nargs="?")

# Optional CLI flag
group.add_argument("-v", "--verbose", help="Provides a verbose desc", action="store_true")
group.add_argument("-s", "--silence", help="Silence the output", action="store_true")
args: Namespace = parser.parse_args()

if args.verbose:
    print(f"Hello, my name is {args.echo}")
elif args.silence:
    print("Output silenced!")
else:
    print(f"{args.echo}")
```

banner
big
block
bubble
circle
digital
emboss
emboss2
future
ivrit
lean
letter
mini
mnemonic
pagga
script
shadow
slant
small
smblock
smbraille
smscript
smshadow
smslant
standard
term
wideterm
