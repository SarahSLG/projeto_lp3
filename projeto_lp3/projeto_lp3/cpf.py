from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("510.242.307-08"))
print(cpf.validate("51024230708"))

cpfs = [
    "510.242.307-08",
    "51024230708"
    "354435"
]

print(cpf.validate_list(cpfs))
