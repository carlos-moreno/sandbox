arquivos = ['xpto_20240105_001_Z01.txt', 'xptz_20240105_001_Z01.txt', 'xxts_20240105_001_Z02.txt', 'xxts_20240105_001_Z03.csv']

sublistas = {}

for arquivo in arquivos:
    zona = arquivo.split('_')[-1].split('.')[0]
    sublistas.setdefault(zona, []).append(arquivo)

print(sublistas)