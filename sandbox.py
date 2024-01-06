arquivos = ['xpto_20240105_001_Z01.txt', 'xptz_20240105_001_Z01.txt', 'xxts_20240105_001_Z02.txt']

sublistas = {}

for arquivo in arquivos:
    zona = arquivo.split('_')[-1].split('.')[0]

    if zona in sublistas:
        sublistas[zona].append(arquivo)
    else:
        sublistas[zona] = [arquivo]

print(sublistas)