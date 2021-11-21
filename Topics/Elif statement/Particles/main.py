spin, charge = input(), input()
particle = ''
the_class = ''
if spin == '1':
    particle = 'Photon'
    the_class = 'Boson'
elif spin == '1/2':
    if charge == '-1/3':
        particle = 'Strange'
        the_class = 'Quark'
    elif charge == '2/3':
        particle = 'Charm'
        the_class = 'Quark'
    elif charge == '-1':
        particle = 'Electron'
        the_class = 'Lepton'
    elif charge == '0':
        particle = 'Neutrino'
        the_class = 'Lepton'
else:
    particle = 'Unknown'
    the_class = 'Unknown'

print(particle, the_class)
