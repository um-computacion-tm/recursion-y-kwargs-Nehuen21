import unittest

database = {
    "persona1":{
        "Nombre1":"Facu",
        "Nombre2": "Thomas",
        "Apellido1": "Lucero",
        "Apellido2": "Corvaland", 
     },
    "persona2": {
        "Nombre1": "Lautaro",
        "Nombre2": "Fernando",
        "Apellido1": "Sgalla",
     },
    "persona3": {
        "Nombre1": "Nehuen",
        "Apellido2": "Donozo",
        "Apellido1": "Marquez",  
    },
    "persona4": {
        "Nombre1": "Alejo",
        "Nombre2": "nahim",
        "Apellido1": "Tapia",     
    },
    "persona5": {
        "Nombre1": "Nazareno",
        "Nombre2": "Emiliano",
        "Apellido1": "Aguilera",   
    }
}


def buscar_datos(*args, **kwargs):
    for key , value in kwargs.items():
        existencia = True
        for n, a in value.items():
            if a not in args:
                existencia = False
        if existencia:
            return key
    return "La persona no se encuentra en la base de datos"




class TestKwargs(unittest.TestCase):

    def test_yo(self):
        resultado = buscar_datos("Nehuen", "Donozo", "Marquez",**database)
        self.assertEqual(resultado,"persona3")

    def test_no_existencia_la_persona(self):
        resultado = buscar_datos("Lionel", "Andres", "Messi", **database)
        self.assertEqual(resultado,"La persona no se encuentar en la base de datos")
    
    def test_persona_1(self):
        resultado = buscar_datos("Facu", "Thomas","Lucero","Corvaland",**database)
        self.assertEqual(resultado,"persona1")

    def test_persona_2(self):
        resultado = buscar_datos("Lautaro", "Fernando", "Sgalla", **database)
        self.assertEqual(resultado,"persona2")


    def test_persona_4(self):
        resultado = buscar_datos("Alejo", "nahim","Tapia",**database)
        self.assertEqual(resultado,"persona4")

    def test_persona5(self):
        resultado = buscar_datos("Nazareno", "Emiliano","Aguilera",**database)
        self.assertEqual(resultado,"persona5")

   
unittest.main()

