from datetime import datetime
from datetime import timedelta


class Parameters:

    def __init__(self):
        """ Constructor """
        # self.main_title = "Pronóstico de temperatura del aire a 2 metros"
        # self.main_description = """Este es el pronóstico de la temperatura del aire basado en los datos del IDEAM. """
        self.form_title_lbl = "Parametros"
        self.form_subtitle1_lbl = f""
        self.form_subtitle2_lbl = f"Temporalidad del análisis"
        self.processing_lbl = "Procesando datos...."
        self.subtitle_lbl = "A continuación los resultados..."

        date_format = "%Y/%m/%d"
        self.default_selection = "-- Seleccione un valor --"

        # Elementos seleccionables
        self.station_l1_lbl = "Departamento"
        self.station_l2_lbl = "Municipio"
        self.station_l3_lbl = "Estación"
        self.default_hour_val = datetime.now()
        self.default_hour_val = self.default_hour_val.replace(hour=23, minute=59, second=59)
        # self.hour_step = 60 * 60
        self.init_date_lbl = "Fecha Inicial"
        self.end_date_lbl = "Fecha Final"
        self.init_date_val = datetime.strptime("2023/08/01", date_format)
        #self.ending_date_val = self.init_date_val + timedelta(days=31)
        delta_d = (self.default_hour_val - self.init_date_val).days
        self.ending_date_val = self.init_date_val + timedelta(days=delta_d)

        self.default_init_date_val = datetime.strptime("2022/07/01", date_format)
        self.default_ending_date_val = self.ending_date_val

        # Tooltip de ayuda
        self.form_init_tooltip = "Inicio de los valores de medición a evaluar"
        self.form_end_tooltip = "Inicio de los valores de medición a evaluar"
        self.station_l1_tooltip = "Departamento dónde se encuentra localizada la estación de monitoreo"
        self.station_l2_tooltip = "Municipio dónde se encuentra localizada la estación de monitoreo"
        self.station_l3_tooltip = "Estación de monitoreo"
        self.hour_tooltip = "Hora de toma del dato a evaluar"

        # Para el análisis
        self.min_instances = 14
        self.x_label = "Time [h]"
        self.y_label = "Temperature °C"
        self.y_error_label = "Error"
