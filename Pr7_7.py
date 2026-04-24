x=int(input('Unesi prirodan broj:'))
if x<0: 
    raise Exception('Unesen je broj manji od 0.') #ukliko je unesen broj manji od 0, podići će se iznimka 