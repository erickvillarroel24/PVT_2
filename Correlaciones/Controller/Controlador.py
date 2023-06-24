import xlwings as xw
import numpy as np
import pandas as pd
from Correlaciones.Model.funciones import rs2

# Definir variables
# Definir hojas
SHEET_SUMARIO = "Sumario"

# Definir nombres de columnas
VARIABLES = "Variables"
VALORES = "Valores"

# Valores para escribir desde el MS Excel
COL_VALORES = "col_valores"
RES_RS = 'res_rs'

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SHEET_SUMARIO]
    parametros = sheet[COL_VALORES].options(np.array, transpose=True).value
    sheet[RES_RS].value = rs2(*parametros)

    # Llamar valores de la correlacion


if __name__ == "__main__":
    xw.Book("Frontend.xlsm").set_mock_caller()
    main()
