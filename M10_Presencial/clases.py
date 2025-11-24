class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


def time_to_int(time):
    """Convierte un objeto Time a segundos."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    """Convierte segundos a un objeto Time correctamente formateado."""
    time = Time()
    time.hour = seconds // 3600
    seconds = seconds % 3600
    time.minute = seconds // 60
    time.second = seconds % 60
    return time


def add_time(time, hours, minutes, seconds):
    """Suma horas, minutos y segundos y devuelve un nuevo Time."""
    total_seconds = time_to_int(time)
    extra = hours * 3600 + minutes * 60 + seconds
    return int_to_time(total_seconds + extra)


def increment_time(time, seconds):
    """Incrementa un Time sin crear uno nuevo."""
    total = time_to_int(time) + seconds
    new = int_to_time(total)
    time.hour = new.hour
    time.minute = new.minute
    time.second = new.second


# ================================
# PRUEBAS
# ================================
if __name__ == "__main__":
    print("=== TEST 1: Crear hora ===")
    mi_hora = Time(14, 30, 15)
    print(mi_hora)

    print("\n=== TEST 2: add_time ===")
    nueva = add_time(mi_hora, 1, 40, 50)
    print(nueva)

    print("\n=== TEST 3: increment_time ===")
    increment_time(mi_hora, 5000)
    print(mi_hora)
