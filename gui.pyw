from tkinter import *
import numpy as np
root = Tk()

root.iconbitmap("icon.ico")
root.title("WMA-RCA PEIC")

root.resizable(0,0)
root.config(bg="ivory")

miFrame = Frame(root)
miFrame.pack(fill="both", expand="True")
miFrame.config(bg="ivory", bd=10, relief="groove", cursor="pencil")

input_Label = Label(miFrame, text="Input Data", fg="black", bg="ivory", font=("Times New Roman",20))
input_Label.grid(row=0, column=0, columnspan=2)

int_Asphalt = StringVar()
asphalt_Label = Label(miFrame, text="Optimal asphalt binder content determined for the WMA without RCA, % ", bg="ivory", font=("Times New Roman",16), )
asphalt_Label.grid(row=1, column=0, sticky="e", pady=5)
asphalt_cuadrotexto = Entry(miFrame, textvariable = int_Asphalt)
asphalt_cuadrotexto.grid(row=1, column=1)
asphalt_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

int_Additive = StringVar()
additive_Label = Label(miFrame, text="Chemical additive content by asphalt binder weight, % ", bg="ivory", font=("Times New Roman",16))
additive_Label.grid(row=2, column=0, sticky="e", pady=5)
additive_cuadrotexto = Entry(miFrame, textvariable = int_Additive)
additive_cuadrotexto.grid(row=2, column=1)
additive_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

int_WC = StringVar()
WC_Label = Label(miFrame, text="Average water content in aggregates (natural and RCA), % ", bg="ivory", font=("Times New Roman",16))
WC_Label.grid(row=3, column=0, sticky="e", pady=5)
WC_cuadrotexto = Entry(miFrame, textvariable = int_WC)
WC_cuadrotexto.grid(row=3, column=1)
WC_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

int_TR = StringVar()
TR_Label = Label(miFrame, text="Temperature reduction achieved by the chemical additive implemented, °C ", bg="ivory", font=("Times New Roman",16))
TR_Label.grid(row=4, column=0, sticky="e", pady=5)
TR_cuadrotexto = Entry(miFrame, textvariable = int_TR)
TR_cuadrotexto.grid(row=4, column=1)
TR_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

int_HD = StringVar()
HD_Label = Label(miFrame, text="Hauling distance of the RCA, km ", bg="ivory", font=("Times New Roman",16))
HD_Label.grid(row=5, column=0, sticky="e", pady=5)
HD_cuadrotexto = Entry(miFrame, textvariable = int_HD)
HD_cuadrotexto.grid(row=5, column=1)
HD_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

space1_Label = Label(miFrame, text="", fg="black", bg="ivory", font=("Times New Roman",20))
space1_Label.grid(row=6, column=0)

output_Label = Label(miFrame, text="Output Data", fg="black", bg="ivory", font=("Times New Roman",20))
output_Label.grid(row=7, column=0, columnspan=2)

print_optimal_RCA = StringVar()
optimal_RCA_Label = Label(miFrame, text="Optimal coarse RCA content, % ", bg="ivory", font=("Times New Roman",16))
optimal_RCA_Label.grid(row=8, column=0, sticky="e", pady=5)
optimal_RCA_cuadrotexto = Entry(miFrame, textvariable = print_optimal_RCA)
optimal_RCA_cuadrotexto.grid(row=8, column=1)
optimal_RCA_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

space2_Label = Label(miFrame, text="", fg="black", bg="ivory", font=("Times New Roman",4))
space2_Label.grid(row=9, column=0)

results_Label = Label(miFrame, text="The production of 1 ton of WMA (with the optimal coarse RCA content) generates: ", fg="black", bg="ivory", font=("Times New Roman",16))
results_Label.grid(row=10, column=0, columnspan=2)

space3_Label = Label(miFrame, text="", fg="black", bg="ivory", font=("Times New Roman",4))
space3_Label.grid(row=11, column=0)

print_optimal_OD = StringVar()
OD_Label = Label(miFrame, text="Ozone depletion, mg CFC-11eq ", bg="ivory", font=("Times New Roman",16))
OD_Label.grid(row=12, column=0, sticky="e")
OD_cuadrotexto = Entry(miFrame, textvariable = print_optimal_OD)
OD_cuadrotexto.grid(row=12, column=1)
OD_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

print_optimal_GW = StringVar()
GW_Label = Label(miFrame, text="Global warming, kg CO2eq ", bg="ivory", font=("Times New Roman",16))
GW_Label.grid(row=13, column=0, sticky="e")
GW_cuadrotexto = Entry(miFrame, textvariable = print_optimal_GW)
GW_cuadrotexto.grid(row=13, column=1)
GW_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

print_optimal_SM = StringVar()
SM_Label = Label(miFrame, text="Smog, kg O3eq ", bg="ivory", font=("Times New Roman",16))
SM_Label.grid(row=14, column=0, sticky="e")
SM_cuadrotexto = Entry(miFrame, textvariable = print_optimal_SM)
SM_cuadrotexto.grid(row=14, column=1)
SM_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

print_optimal_AC = StringVar()
AC_Label = Label(miFrame, text="Acidification, kg SO2eq ", bg="ivory", font=("Times New Roman",16))
AC_Label.grid(row=15, column=0, sticky="e")
AC_cuadrotexto = Entry(miFrame, textvariable = print_optimal_AC)
AC_cuadrotexto.grid(row=15, column=1)
AC_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

print_optimal_EU = StringVar()
EU_Label = Label(miFrame, text="Eutrophication, g Neq ", bg="ivory", font=("Times New Roman",16))
EU_Label.grid(row=16, column=0, sticky="e")
EU_cuadrotexto = Entry(miFrame, textvariable = print_optimal_EU)
EU_cuadrotexto.grid(row=16, column=1)
EU_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

print_optimal_CA = StringVar()
CA_Label = Label(miFrame, text="Carcinogenic, E-6 CTUh ", bg="ivory", font=("Times New Roman",16))
CA_Label.grid(row=17, column=0, sticky="e")
CA_cuadrotexto = Entry(miFrame, textvariable = print_optimal_CA)
CA_cuadrotexto.grid(row=17, column=1)
CA_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

print_optimal_NCA = StringVar()
NCA_Label = Label(miFrame, text="Non-carcinogenic, E-6 CTUh ", bg="ivory", font=("Times New Roman",16))
NCA_Label.grid(row=18, column=0, sticky="e")
NCA_cuadrotexto = Entry(miFrame, textvariable = print_optimal_NCA)
NCA_cuadrotexto.grid(row=18, column=1)
NCA_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

print_optimal_RE = StringVar()
RE_Label = Label(miFrame, text="Respiratory effects, g PM2.5eq ", bg="ivory", font=("Times New Roman",16))
RE_Label.grid(row=19, column=0, sticky="e")
RE_cuadrotexto = Entry(miFrame, textvariable = print_optimal_RE)
RE_cuadrotexto.grid(row=19, column=1)
RE_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

print_optimal_EC = StringVar()
EC_Label = Label(miFrame, text="Ecotoxicity, CTUe ", bg="ivory", font=("Times New Roman",16))
EC_Label.grid(row=20, column=0, sticky="e")
EC_cuadrotexto = Entry(miFrame, textvariable = print_optimal_EC)
EC_cuadrotexto.grid(row=20, column=1)
EC_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

print_optimal_FFD = StringVar()
FFD_Label = Label(miFrame, text="Fossil fuel depletion, MJ surplus ", bg="ivory", font=("Times New Roman",16))
FFD_Label.grid(row=21, column=0, sticky="e")
FFD_cuadrotexto = Entry(miFrame, textvariable = print_optimal_FFD)
FFD_cuadrotexto.grid(row=21, column=1)
FFD_cuadrotexto.config(fg="black", bg="snow", font=("Times New Roman",16), justify="center")

def develop_calculations():
  
    Asphalt = float(int_Asphalt.get())
    Additive = float(int_Additive.get())
    TR = float(int_TR.get())
    HD = float(int_HD.get())
    WC = float(int_WC.get())

    withouh_RCA_upper_OD = 2697.228 + 0.774*0 + 23.319*Asphalt - 21.736*TR + 641.481*WC - 0.119*0*WC
    withouh_RCA_upper_GW = 12662.294 + 2.031*0 + 161.460*Asphalt - 94.316*TR + 3029.878*WC - 1.511*Asphalt*TR
    withouh_RCA_upper_SM = 519.863 + 0.065*0 + 5.261*Asphalt- 3.948*TR + 0.0026*HD + 124.382*WC - 0.0803*TR*WC
    withouh_RCA_upper_AC = 80.892 + 0.0126*0 + 0.783*Asphalt - 0.648*TR + 19.056*WC
    withouh_RCA_upper_EU = 6981.723 + 0.923*0 + 63.749*Asphalt + 15.736*Additive - 55.685*TR + 0.033*HD + 1635.650*WC
    withouh_RCA_upper_CA = 92.896 + 0.025*0 + 1.390*Asphalt - 0.729*TR + 0.0007*HD + 21.624*WC - 0.0002*TR*0
    withouh_RCA_upper_NCA = 651.770 + 0.182*0 + 11.276*Asphalt - 5.200*TR + 152.767*WC
    withouh_RCA_upper_RE = 6173.798 + 1.731*0 + 54.894*Asphalt - 49.633*TR + 1464.828*WC - 0.269*0*WC
    withouh_RCA_upper_EC = 19661.179 + 4.182*0 + 281.626*Asphalt + 29.761*Additive - 149.652*TR + 0.178*HD + 4719.121*WC - 3.101*TR*WC
    withouh_RCA_upper_FFD = 24082.304 + 5.113*0 + 288.354*Asphalt - 193.543*TR + 5685.109*WC
    
    vector_lower_OD = np.zeros(46, dtype=float)
    vector_lower_GW = np.zeros(46, dtype=float)
    vector_lower_SM = np.zeros(46, dtype=float)
    vector_lower_AC = np.zeros(46, dtype=float)
    vector_lower_EU = np.zeros(46, dtype=float)
    vector_lower_CA = np.zeros(46, dtype=float)
    vector_lower_NCA = np.zeros(46, dtype=float)
    vector_lower_RE = np.zeros(46, dtype=float)
    vector_lower_EC = np.zeros(46, dtype=float)
    vector_lower_FFD = np.zeros(46, dtype=float)
    vector_RCA = np.arange(0, 46, 1) 
    vector_results = np.arange(0, 10, 1)

    for RCA in vector_RCA:
        vector_lower_OD[RCA] = 2692.550 + 0.703*RCA + 22.456*Asphalt - 21.779*TR + 640.759*WC - 0.144*RCA*WC
        vector_lower_GW[RCA] = 12613.387 + 1.893*RCA + 151.313*Asphalt - 96.088*TR + 3027.806*WC - 1.882*Asphalt*TR
        vector_lower_SM[RCA] = 519.074 + 0.060*RCA + 5.127*Asphalt- 3.964*TR + 0.0013*HD + 124.218*WC - 0.0863*TR*WC
        vector_lower_AC[RCA] = 80.678 + 0.0112*RCA + 0.742*Asphalt - 0.650*TR + 19.036*WC
        vector_lower_EU[RCA] = 6969.109 + 0.845*RCA + 61.421*Asphalt + 4.098*Additive - 55.801*TR + 0.009*HD + 1634.486*WC
        vector_lower_CA[RCA] = 92.657 + 0.022*RCA + 1.346*Asphalt - 0.733*TR + 0.0003*HD + 21.602*WC - 0.0003*TR*RCA
        vector_lower_NCA[RCA] = 650.539 + 0.174*RCA + 11.037*Asphalt - 5.212*TR + 152.647*WC
        vector_lower_RE[RCA] = 6163.092 + 1.570*RCA + 52.919*Asphalt - 49.732*TR + 1463.176*WC - 0.328*RCA*WC
        vector_lower_EC[RCA] = 19628.665 + 4.004*RCA + 276.295*Asphalt + 3.102*Additive - 150.305*TR + 0.124*HD + 4712.591*WC - 3.340*TR*WC
        vector_lower_FFD[RCA] = 24039.748 + 4.838*RCA + 280.097*Asphalt - 193.956*TR + 5680.980*WC

    OD = 0
    while OD < 45:
        if vector_lower_OD[OD] <= withouh_RCA_upper_OD:
            OD = OD + 1
        else:
            break
    vector_results[0] = OD

    GW = 0
    while GW < 45:
        if vector_lower_GW[GW] <= withouh_RCA_upper_GW:
            GW = GW + 1
        else:
            break
    vector_results[1] = GW

    SM = 0
    while SM < 45:
        if vector_lower_SM[SM] <= withouh_RCA_upper_SM:
            SM = SM + 1
        else:
            break
    vector_results[2] = SM

    AC = 0
    while AC < 45:
        if vector_lower_AC[AC] <= withouh_RCA_upper_AC:
            AC = AC + 1
        else:
            break
    vector_results[3] = AC

    EU = 0
    while EU < 45:
        if vector_lower_EU[EU] <= withouh_RCA_upper_EU:
            EU = EU + 1
        else:
            break
    vector_results[4] = EU

    CA = 0
    while CA < 45:
        if vector_lower_CA[CA] <= withouh_RCA_upper_CA:
            CA = CA + 1
        else:
            break
    vector_results[5] = CA

    NCA = 0
    while NCA < 45:
        if vector_lower_NCA[NCA] <= withouh_RCA_upper_NCA:
            NCA = NCA + 1
        else:
            break
    vector_results[6] = NCA

    RE = 0
    while RE < 45:
        if vector_lower_RE[RE] <= withouh_RCA_upper_RE:
            RE = RE + 1
        else:
            break
    vector_results[7] = RE

    EC = 0
    while EC < 45:
        if vector_lower_EC[EC] <= withouh_RCA_upper_EC:
            EC = EC + 1
        else:
            break
    vector_results[8] = EC

    FFD = 0
    while FFD < 45:
        if vector_lower_FFD[FFD] <= withouh_RCA_upper_FFD:
            FFD = FFD + 1
        else:
            break
    vector_results[9] = FFD

    optimal_RCA = np.amin(vector_results)
    optimal_OD = 2695 + 0.738*optimal_RCA + 22.89*Asphalt - 21.76*TR + 641.1*WC - 0.132*optimal_RCA*WC
    optimal_GW = 12640 + 1.962*optimal_RCA + 156.4*Asphalt - 95.2*TR + 3029*WC - 1.697*Asphalt*TR
    optimal_SM = 519.5 + 0.0626*optimal_RCA + 5.195*Asphalt - 3.957*TR + 0.0019*HD + 124.3*WC - 0.0833*TR*WC
    optimal_AC = 80.785 + 0.0119*optimal_RCA + 0.762*Asphalt - 0.649*TR + 19.046*WC
    optimal_EU = 6975 + 0.884*optimal_RCA + 62.58*Asphalt + 9.917*Additive - 55.74*TR + 0.021*HD + 1635*WC
    optimal_CA = 92.78 + 0.024*optimal_RCA + 1.368*Asphalt - 0.7312*TR + 0.00049*HD + 21.610*WC - 0.00025*TR*optimal_RCA
    optimal_NCA = 651.155 + 0.178*optimal_RCA + 11.157*Asphalt - 5.206*TR + 152.707*WC
    optimal_RE = 6168.445 + 1.65*optimal_RCA + 53.907*Asphalt - 49.683*TR + 1464.002*WC - 0.299*optimal_RCA*WC
    optimal_EC = 19640 + 4.093*optimal_RCA + 279*Asphalt + 16.43*Additive - 150*TR + 0.151*HD + 4716*WC - 3.221*TR*WC
    optimal_FFD = 24060 + 4.975*optimal_RCA + 284.2*Asphalt - 193.7*TR + 5683*WC
    
    output_optimal_OD = str(int(optimal_OD))
    output_optimal_GW = str(int(optimal_GW))
    output_optimal_SM = str(int(optimal_SM))
    output_optimal_AC = str(int(optimal_AC))
    output_optimal_EU = str(int(optimal_EU))
    output_optimal_CA = str(int(optimal_CA))
    output_optimal_NCA = str(int(optimal_NCA))
    output_optimal_RE = str(int(optimal_RE))
    output_optimal_EC = str(int(optimal_EC))
    output_optimal_FFD = str(int(optimal_FFD))
    
    print_optimal_RCA.set(optimal_RCA)
    print_optimal_OD.set(output_optimal_OD)
    print_optimal_GW.set(output_optimal_GW)
    print_optimal_SM.set(output_optimal_SM)
    print_optimal_AC.set(output_optimal_AC)
    print_optimal_EU.set(output_optimal_EU)
    print_optimal_CA.set(output_optimal_CA)
    print_optimal_NCA.set(output_optimal_NCA)
    print_optimal_RE.set(output_optimal_RE)
    print_optimal_EC.set(output_optimal_EC)
    print_optimal_FFD.set(output_optimal_FFD)
        
    return optimal_RCA

botoncalculate = Button(root, text="Calculate", command=develop_calculations, fg="black", bg="ivory", relief="groove", font=("Times New Roman",16), cursor="hand1")
botoncalculate.pack()

root.mainloop()