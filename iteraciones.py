temperaturas = [
    [   # Ciudad Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 45}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 21}
        ]
    ],
    [   # Puyo 2
        [   # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 44},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 39}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 43},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 42},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 58},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 40}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 44},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 49},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 47},
            {"day": "Domingo", "temp": 40}
        ]
    ],
    [   # Cuenca 3
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]

ciudades = ["Quito 1", "Puyo 2", "Cuenca 3"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
