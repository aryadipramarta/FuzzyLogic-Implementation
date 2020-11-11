import matplotlib.pyplot as plt
from numpy.lib.function_base import append
import pandas as pd
import csv
from operator import attrgetter

#membacaFile
dfile = pd.read_excel("Mahasiswa.xls");
class Mahasiswa:
    def __init__(self,id,penghasilan,pengeluaran,score):
        self.id = id
        self.penghasilan = penghasilan
        self.pengeluaran = pengeluaran
        self.score = score
    
    def __repr__(self):
        return repr((self.id,self.penghasilan,self.pengeluaran,self.score))

#Design Membership Function
def calc_high(value,x,y):
    high = round(((value - x)/(y - x)),2);
    return high

def calc_low(value,x,y):
    low = round(((y - value)/(y - x)),2);
    return low

def calc_med_one(value,x,y):
    med_one = round(((value - x)/(y - x)),2);
    return med_one

def calc_med_two(value,x,y):
    med_two = round(((y-value)/(y-x)),2);
    return med_two

#Membership Function for Penghasilan 
lim_inc = [5,7,11,15,18]
#Membership Function for Penghasilan(Upper)
def Penghasilanfunc_Up(value):
    if (value<=lim_inc[2]):
        return 0;
    elif(value>lim_inc[4]):
        return 1;
    elif(value > lim_inc[2] and value <= lim_inc[4]):
        return calc_high(value,lim_inc[2],lim_inc[4]); 

#Membership Function for Penghasilan(Bottom)
def Penghasilanfunc_Bot(value):
    if(value <= lim_inc[0]):
        return 1;
    elif(value > lim_inc[1]):
        return 0;
    elif(value <= lim_inc[1] and value > lim_inc[0]):
        return calc_low(value,lim_inc[0],lim_inc[1]);

#Membership Function for Penghasilan(Medium)
def Penghasilanfunc_Med(value):
    if(value <= lim_inc[1] or value > lim_inc[4]):
        return 0;
    elif(value > lim_inc[1] and value <= lim_inc[2]):
        return calc_med_one(value,lim_inc[1],lim_inc[2]);
    elif(value >lim_inc[2] and value <= lim_inc[3]):
        return 1;
    elif(value > lim_inc[3] and value <= lim_inc[4]):
        return calc_med_two(value,lim_inc[3],lim_inc[4]);

#Membership Function for Pengeluaran
lim_out = [3,4,7,9,11]
#Membership Function for Pengeluaran(High)
def Pengeluaranfunc_High(value):
    if (value<=lim_out[2]):
        return 0;
    elif(value>lim_out[4]):
        return 1;
    elif(value > lim_out[2] and value <= lim_out[4]):
        return calc_high(value,lim_out[2],lim_out[4]); 

#Membership Function for Pengeluarn(Low)
def Pengeluaranfunc_Low(value):
    if(value <= lim_out[0]):
        return 1;
    elif(value > lim_out[1]):
        return 0;
    elif(value <= lim_out[1] and value > lim_out[0]):
        return calc_low(value,lim_out[0],lim_out[1]);

#Membership Function for Pengeluaran(Average)
def Pengeluaranfunc_Avg(value):
    if(value <= lim_out[1] or value > lim_out[4]):
        return 0;
    elif(value > lim_out[1] and value <= lim_out[2]):
        return calc_med_one(value,lim_out[1],lim_out[2]);
    elif(value >lim_out[2] and value <= lim_out[3]):
        return 1;
    elif(value > lim_out[3] and value <= lim_out[4]):
        return calc_med_two(value,lim_out[3],lim_out[4]);

#PlotForMembershipFunctionForPenghasilan
x1_inc = [0,11,15,18];
y1_inc = [0,0,1,1];

x2_inc = [0,5,7,18];
y2_inc = [1,1,0,0];

x3_inc = [0,5,7,11,15,18];
y3_inc = [0,0,1,1,0,0];

fig, axs = plt.subplots(1,2,figsize=(9,3),sharey=True)
fig.suptitle('Membership Function for Penghasilan and Pengeluaran')
axs[0].plot(x1_inc,y1_inc,label='Penghasilan Tinggi');
axs[0].plot(x2_inc,y2_inc,label='Penghasilan Rendah');
axs[0].plot(x3_inc,y3_inc,label='Penghasilan Sedang');
axs[0].legend()
#PlotForMembershipFunctionForPengeluaran
x1_out = [0,7,9,11];
y1_out = [0,0,1,1];

x2_out = [0,3,4,11];
y2_out = [1,1,0,0];

x3_out = [0,3,4,7,9,11];
y3_out = [0,0,1,1,0,0];

axs[1].plot(x1_out,y1_out,label='Pengeluaran Tinggi');
axs[1].plot(x2_out,y2_out,label='Pengeluaran Rendah');
axs[1].plot(x3_out,y3_out,label='Pengeluaran Rata-Rata');
axs[1].legend()

#INFERENCE

#FuzzyRules For Determine Mahasiswa Accepted , Rejected or Considered based on input Penghasilan and Pengeluaran
def Fuzzy_Rules(cond_pengeluaran,cond_penghasilan,val_inc,val_out):
    acc,cons,rej = [], [], [];
    if(cond_penghasilan[i][0] == 'Diatas' and cond_pengeluaran[i][0] == 'Tinggi'):
        value = min(val_inc[i][0],val_out[i][0]);
        rej.append(['Reject',value]);
    if(cond_penghasilan[i][0] == 'Diatas' and cond_pengeluaran[i][1] == 'Rata-Rata'):
        value = min(val_inc[i][0],val_out[i][1]);
        rej.append(['Reject',value]);
    if(cond_penghasilan[i][0] == 'Diatas' and cond_pengeluaran[i][2] == 'Rendah'):
        value = min(val_inc[i][0],val_out[i][2]);
        rej.append(['Reject',value]);
    if(cond_penghasilan[i][1] == 'Tengah' and cond_pengeluaran[i][0] == 'Tinggi'):
        value = min(val_inc[i][1],val_out[i][0]);
        rej.append(['Reject',value]);
    if(cond_penghasilan[i][1] == 'Tengah' and cond_pengeluaran[i][1] == 'Rata-Rata'):
        value = min(val_inc[i][1],val_out[i][1]);
        cons.append(['Considered',value]);
    if(cond_penghasilan[i][1] == 'Tengah' and cond_pengeluaran[i][2] == 'Rendah'):
        value = min(val_inc[i][1],val_out[i][2]);
        cons.append(['Considered',value]);
    if(cond_penghasilan[i][2] == 'Bawah' and cond_pengeluaran[i][0] == 'Tinggi'):
        value = min(val_inc[i][2],val_out[i][0]);
        acc.append(['Accept',value]);
    if(cond_penghasilan[i][2] == 'Bawah' and cond_pengeluaran[i][1] == 'Rata-Rata'):
        value = min(val_inc[i][2],val_out[i][1]);
        acc.append(['Accept',value]);
    if(cond_penghasilan[i][2] == 'Bawah' and cond_pengeluaran[i][2] == 'Rendah'):
        value = min(val_inc[i][2],val_out[i][2]);
        acc.append(['Accept',value]);
    
    return acc,cons,rej

#Disjunction rule to get the maximum value for each fuzzy output
def Disjunction_Rule(Score):
    value = []
    value.append(max(Score[0]));
    value.append(max(Score[1]));
    value.append(max(Score[2]));
    return value

#Defuzzification - Sugeno Style 
def defuzzification(Value):
    batas = [50,75,100]
    hasila = Value[0][1]*batas[2]
    hasilb = Value[1][1]*batas[1]
    hasilc = Value[2][1]*batas[0]
    pembagi = Value[0][1]+Value[1][1]+Value[2][1]
    hasil = ((hasila+hasilb+hasilc)/pembagi)
    return hasil 

#mainprogram
mhs = []
income = [];
out = []
con_pengeluaran = []
con_penghasilan = []
hasil = []
for i in range(len(dfile)):
    mhs.append(Mahasiswa(dfile["Id"][i],dfile["Penghasilan"][i],dfile["Pengeluaran"][i],""));
    con_pengeluaran.append(['Tinggi','Rata-Rata','Rendah'])
    con_penghasilan.append(['Diatas','Tengah','Bawah'])
    income.append([Penghasilanfunc_Up(mhs[i].penghasilan),Penghasilanfunc_Med(mhs[i].penghasilan),Penghasilanfunc_Bot(mhs[i].penghasilan)]);
    out.append([Pengeluaranfunc_High(mhs[i].pengeluaran),Pengeluaranfunc_Avg(mhs[i].pengeluaran),Pengeluaranfunc_Low(mhs[i].pengeluaran)]);
    Score = Fuzzy_Rules(con_pengeluaran,con_penghasilan,income,out)
    Disj = Disjunction_Rule(Score);
    hasil = round(defuzzification(Disj),2);
    mhs[i].score = hasil
    #print(mhs[i].id,mhs[i].penghasilan,mhs[i].pengeluaran,mhs[i].score);
  
sorted_mhs = sorted(mhs,key=attrgetter('score'),reverse=True)
penerima = []
for i in range(20):
    penerima.append([sorted_mhs[i].id,sorted_mhs[i].score])
print("Penerima Bantuan Mahasiswa dengan ID : ")
for i in range(len(penerima)):
    print(penerima[i])
