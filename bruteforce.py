import itertools, time

obj = input("Introduce la contraseña a buscar: ")

if len(obj) == 4:
    print("Búsqueda de contraseña iniciada...")
    print("Buscando....")
    carct = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.:-?¿!¡+*/%$#@'
    long_max = 4

    def g_comb(carct, long_max):
        for long in range(1, long_max + 1):
            for combi in itertools.product(carct, repeat=long):
                yield ''.join(combi)

    def b_contr(obj, carct, long_max): 
        tiempo_i = time.time()
        inte = 0

        for combi in g_comb(carct, long_max):
            inte += 1
            if combi == obj:
                tiempo_f = time.time()
                tiempo_e = tiempo_f - tiempo_i
                return combi, inte, tiempo_e

    contr_e, inte, tiempo = b_contr(obj, carct, long_max)

    print(f"Contraseña encontrada: {contr_e}")
    print(f"Número de intentos: {inte}")
    print(f"Tiempo de busqueda: {tiempo:.4f} segundos")
else:
    print("La contraseña debe tener 4 caracteres.")
