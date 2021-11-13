medida = float(input('Uma distancia em metros'))
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))
print('A medida de {}m corresponde a {}dam e {}hm e {}km'.format(medida, dam, hm, km))