import xlwings as xw
import numpy as np
import pandas as pd
from Correlaciones.Model.funciones import rs
from Correlaciones.Model.funciones import Bo
from Correlaciones.Model.funciones import Pb

# Definir variables
# Definir hojas
SHEET_SUMARIO = "Sumario"

# Definir nombres de columnas
VARIABLES = "Variables"
VALORES = "Valores"

# Valores para escribir desde el MS Excel Rs
COL_VALORES1,COL_VALORES2,COL_VALORES3,COL_VALORES4,COL_VALORES5\
    = "col_valores1","col_valores2","col_valores3","col_valores4","col_valores5"
RES_RS1,RES_RS2,RES_RS3,RES_RS4,RES_RS5 \
    = 'res_rs1','res_rs2','res_rs3','res_rs4','res_rs5'

# Valores para escribir desde el MS Excel Bo
COL_BO1,COL_BO2,COL_BO3,COL_BO4,COL_BO5\
    = "col_bo1","col_bo2","col_bo3","col_bo4","col_bo5"
RES_BO1,RES_BO2,RES_BO3,RES_BO4,RES_BO5 \
    = 'res_bo1','res_bo2','res_bo3','res_bo4','res_bo5'

# Valores para escribir desde el MS Excel Pb
COL_PB1,COL_PB2,COL_PB3,COL_PB4,COL_PB5\
    = "col_pb1","col_pb2","col_pb3","col_pb4","col_pb5"
RES_PB1,RES_PB2,RES_PB3,RES_PB4,RES_PB5 \
    = 'res_pb1','res_pb2','res_pb3','res_pb4','res_pb5'

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SHEET_SUMARIO]
    # Llamar valores de la correlacion RS
    parametros1 = sheet[COL_VALORES1].options(np.array, transpose=True).value
    sheet[RES_RS1].value = rs(*parametros1)
    parametros2 = sheet[COL_VALORES2].options(np.array, transpose=True).value
    sheet[RES_RS2].value = rs(*parametros2)
    parametros3 = sheet[COL_VALORES3].options(np.array, transpose=True).value
    sheet[RES_RS3].value = rs(*parametros3)
    parametros4 = sheet[COL_VALORES4].options(np.array, transpose=True).value
    sheet[RES_RS4].value = rs(*parametros4)
    parametros5 = sheet[COL_VALORES5].options(np.array, transpose=True).value
    sheet[RES_RS5].value = rs(*parametros5)

    # Llamar valores de la correlacion Bo
    parametros_bo1 = sheet[COL_BO1].options(np.array, transpose=True).value
    sheet[RES_BO1].value = Bo(*parametros_bo1)
    parametros_bo2 = sheet[COL_BO2].options(np.array, transpose=True).value
    sheet[RES_BO2].value = Bo(*parametros_bo2)
    parametros_bo3 = sheet[COL_BO3].options(np.array, transpose=True).value
    sheet[RES_BO3].value = Bo(*parametros_bo3)
    parametros_bo4 = sheet[COL_BO4].options(np.array, transpose=True).value
    sheet[RES_BO4].value = Bo(*parametros_bo4)
    parametros_bo5 = sheet[COL_BO5].options(np.array, transpose=True).value
    sheet[RES_BO5].value = Bo(*parametros_bo5)

    # Llamar valores de la correlacion Bo
    parametros_pb1 = sheet[COL_PB1].options(np.array, transpose=True).value
    sheet[RES_PB1].value = Pb(*parametros_pb1)
    parametros_pb2 = sheet[COL_PB2].options(np.array, transpose=True).value
    sheet[RES_PB2].value = Pb(*parametros_pb2)
    parametros_pb3 = sheet[COL_PB3].options(np.array, transpose=True).value
    sheet[RES_PB3].value = Pb(*parametros_pb3)
    parametros_pb4 = sheet[COL_PB4].options(np.array, transpose=True).value
    sheet[RES_PB4].value = Pb(*parametros_pb4)
    parametros_pb5 = sheet[COL_PB5].options(np.array, transpose=True).value
    sheet[RES_PB5].value = Pb(*parametros_pb5)


if __name__ == "__main__":
    xw.Book("Frontend.xlsm").set_mock_caller()
    main()
