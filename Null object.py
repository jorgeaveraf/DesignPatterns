class Logger:
    def log(self, message: str):
        pass  # Esto es lo que hace el diario imaginario: ¡nada!


class ConsoleLogger(Logger):
    def log(self, message: str):
        # Esto es un diario real que anota en la consola.
        print(f"Logging to console: {message}")


class Application:
    def __init__(self, logger: Logger = None):
        # Si no hay un diario real, usamos el imaginario (Null Object).
        self._logger = logger if logger else Logger()

    def process(self):
        # Intentamos anotar que empezamos.
        self._logger.log("Processing started")
        print("Processing...")  # Hacemos algo.
        # Intentamos anotar que terminamos.
        self._logger.log("Processing finished")


# Ejemplo 1: Usando un diario real
app_with_logger = Application(ConsoleLogger())
app_with_logger.process()

# Ejemplo 2: Usando un diario imaginario
app_without_logger = Application()
app_without_logger.process()
