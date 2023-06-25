# librerias a usar
import xlwings as xw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Correlaciones.Model.funciones import Rs
from Correlaciones.Model.funciones import Bo
from Correlaciones.Model.funciones import Pb
from Correlaciones.Model.funciones import Uo

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

# Valores para escribir desde el MS Excel Pb
COL_UO1,COL_UO2,COL_UO3,COL_UO4,COL_UO5\
    = "col_uo1","col_uo2","col_uo3","col_uo4","col_uo5"
RES_UO1,RES_UO2,RES_UO3,RES_UO4,RES_UO5 \
    = 'res_uo1','res_uo2','res_uo3','res_uo4','res_uo5'

# Valores P, Rs, Bo, Pb, Uo para graficar
VAL_P = "valores_presion"
VAL_RS = "valores_solubilidad"
VAL_BO = "valores_bo"
VAL_PB = "valores_pb"
VAL_UO = "valores_uo"

# Funcion main
def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[SHEET_SUMARIO]
    # Llamar valores de la correlacion RS
    parametros1 = sheet[COL_VALORES1].options(np.array, transpose=True).value
    sheet[RES_RS1].value = Rs(*parametros1)
    parametros2 = sheet[COL_VALORES2].options(np.array, transpose=True).value
    sheet[RES_RS2].value = Rs(*parametros2)
    parametros3 = sheet[COL_VALORES3].options(np.array, transpose=True).value
    sheet[RES_RS3].value = Rs(*parametros3)
    parametros4 = sheet[COL_VALORES4].options(np.array, transpose=True).value
    sheet[RES_RS4].value = Rs(*parametros4)
    parametros5 = sheet[COL_VALORES5].options(np.array, transpose=True).value
    sheet[RES_RS5].value = Rs(*parametros5)

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

    # Llamar valores de la correlacion Uo
    parametros_uo1 = sheet[COL_UO1].options(np.array, transpose=True).value
    sheet[RES_UO1].value = Uo(*parametros_uo1)
    parametros_uo2 = sheet[COL_UO2].options(np.array, transpose=True).value
    sheet[RES_UO2].value = Uo(*parametros_uo2)
    parametros_uo3 = sheet[COL_UO3].options(np.array, transpose=True).value
    sheet[RES_UO3].value = Uo(*parametros_uo3)
    parametros_uo4 = sheet[COL_UO4].options(np.array, transpose=True).value
    sheet[RES_UO4].value = Uo(*parametros_uo4)
    parametros_uo5 = sheet[COL_UO5].options(np.array, transpose=True).value
    sheet[RES_UO5].value = Uo(*parametros_uo5)

    #Crear graficos de acuerdo a la presion
    presion = sheet[VAL_P].options(np.array).value
    p = presion.tolist()
    solubilidad = sheet[VAL_RS].options(np.array).value
    s = solubilidad.tolist()
    factor = sheet[VAL_BO].options(np.array).value
    f = factor.tolist()
    burbuja = sheet[VAL_PB].options(np.array).value
    b = burbuja.tolist()
    viscosidad = sheet[VAL_UO].options(np.array).value
    v = viscosidad.tolist()

    #Crear dataframes para las graficas con seaborn
    df1 = pd.DataFrame({"x":s,"y":p})
    df2 = pd.DataFrame({"x": f, "y": p})
    df3 = pd.DataFrame({"x":s , "y":b})
    df4 = pd.DataFrame({"x": v, "y": p})

    # P vs Rs
    fig1 = plt.figure(figsize=(10, 7))
    ax = sns.lineplot(df1, x = "x", y = "y", color="orange",markers=True)
    plt.xlabel("Solubilidad")
    plt.ylabel("Presion")
    plt.suptitle("P vs Rs")
    sheet.pictures.add(fig1, name="P vs Rs", update=True, left=sheet.range("A16").left,
                       top=sheet.range("A16").top, height=310, width = 395)

    # P vs Bo
    fig2 = plt.figure(figsize=(10, 7))
    ax = sns.lineplot(df2, x="x", y="y", color="blue")
    plt.xlabel("Factor volumetrico")
    plt.ylabel("Presion")
    plt.suptitle("P vs Bo")
    sheet.pictures.add(fig2, name="P vs Bo", update=True, left=sheet.range("J16").left,
                       top=sheet.range("J16").top, height=310, width = 395)

    # Rs vs Pb
    fig3 = plt.figure(figsize=(10, 7))
    ax = sns.lineplot(df3, x="x", y="y",color="red")
    plt.xlabel("Solubilidad")
    plt.ylabel("Presion de Burbuja")
    plt.suptitle("Pb vs Rs")
    sheet.pictures.add(fig3, name="Pb vs Rs", update=True, left=sheet.range("A48").left,
                       top=sheet.range("A48").top, height=310, width = 395)

    # P vs Uo
    fig4 = plt.figure(figsize=(10, 7))
    ax = sns.lineplot(df4, x="x", y="y",color="green")
    plt.xlabel("Viscosidad")
    plt.ylabel("Presion")
    plt.suptitle("P vs Uo")
    sheet.pictures.add(fig4, name="P vs Uo", update=True, left=sheet.range("J48").left,
                       top=sheet.range("J48").top, height=310, width = 395)


if __name__ == "__main__":
    xw.Book("Frontend.xlsm").set_mock_caller()
    main()
