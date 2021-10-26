#!/usr/bin/python3.5
# -*-coding:utf_8 -*

from matplotlib import pyplot
import numpy as np
import statistics



import csv
file = open("../data.csv");
csvreader = csv.reader(file);
header = next(csvreader);
rows = [];
for row in csvreader:
    rows.append(row);
file.close();

# ------------------------------------------------------------------------ #
# Read datas
i=0; zone_1=[]; zone_2=[]; zone_3=[]; zone_4=[]; age=[];
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Experiment n°1"):
            i+=2;
            while( i<len(rows) ):
                if (rows[i][0]=='') : i = len(rows);
                else :
                    zone_1.append(float(rows[i][4]));
                    zone_2.append(float(rows[i][5]));
                    zone_3.append(float(rows[i][6]));
                    zone_4.append(float(rows[i][7]));
                    age.append(float(rows[i][1]));
                    i+=1;
        i+=1;

# Average and standard deviation
std_zone_1 = statistics.stdev(zone_1); std_zone_2 = statistics.stdev(zone_2); std_zone_3 = statistics.stdev(zone_3); std_zone_4 = statistics.stdev(zone_4);
mean_zone_1 = np.mean(zone_1); mean_zone_2 = np.mean(zone_2); mean_zone_3 = np.mean(zone_3); mean_zone_4 = np.mean(zone_4);

print("\x1B[1;36m------------------------------------------------------------------------");
print("\x1B[1;37;44mExperimentation no.1\x1B[0m");
print("");
print("\x1B[1;36mAnswers\x1B[0;36m");
i=0;
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Experiment n°1"):
            print( rows[i+1][0],"\t|",rows[i+1][1],"\t|",rows[i+1][2],"\t|",rows[i+1][3],"\t|",rows[i+1][4],"\t|",rows[i+1][5],"\t|",rows[i+1][6],"\t|",rows[i+1][7],"\t|");
            i+=2;
            while( i<len(rows) ):
                if (rows[i][0]=='') : i = len(rows);
                else : print( "\t", rows[i][0],"\t|",rows[i][1],"\t|",rows[i][2],"\t|",rows[i][3],"\t\t|",rows[i][4],"\t|",rows[i][5],"\t|",rows[i][6],"\t|",rows[i][7],"\t|"); i+=1;
        i+=1;
print("");
print("\x1B[1;36mPersonal ranking\x1B[0;36m");
i=0;
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Ranking"):
            print( rows[i+1][0],"\t|",rows[i+1][1],"\t|",rows[i+1][2],"\t|",rows[i+1][3],"\t|",rows[i+1][4],"\t|");
            i+=2;
            while( i<len(rows) ):
                if (rows[i][0]=='') : i = len(rows);
                else : print( "\t", rows[i][0],"\t|",rows[i][1],"\t|",rows[i][2],"\t|",rows[i][3],"\t|",rows[i][4],"\t|"); i+=1;
        i+=1;
print("");
print("\x1B[1;36mAverage and standard deviation\x1B[0;36m");
print("          \t| Average \t| Standard deviation ","\t|");
print("Age       \t|", np.around(np.mean(age),2), "\t\t|", np.around(statistics.stdev(age),2),"\t\t|");
print("Zone no.1 \t|", np.around(mean_zone_1,2), "\t\t|", np.around(std_zone_1,2),"\t\t\t|");
print("Zone no.2 \t|", np.around(mean_zone_2,2), "\t\t|", np.around(std_zone_2,2),"\t\t\t|");
print("Zone no.3 \t|", np.around(mean_zone_3,2), "\t\t|", np.around(std_zone_3,2),"\t\t\t|");


# Save histogram
values = [mean_zone_1, mean_zone_2, mean_zone_3, mean_zone_4];
errorValues = [std_zone_1, std_zone_2, std_zone_3, std_zone_4];
pyplot.bar(range(len(values)), values, color = 'skyblue');
pyplot.errorbar(range(len(values)), values, yerr = errorValues,
    fmt = 'none', capsize = 10, ecolor = 'red', elinewidth = 1, capthick = 1);
pyplot.savefig('histo_v1.png', transparent = True); pyplot.close();
pyplot.close();



# ------------------------------------------------------------------------ #
print("\x1B[1;36m------------------------------------------------------------------------");
# Read datas
i=0; zone_1=[]; zone_2=[]; zone_3=[]; age=[];
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Experiment n°2"):
            i+=2;
            while( i<len(rows) ):
                if (rows[i][0]=='8') : i = len(rows);
                else :
                    zone_1.append(float(rows[i][1+3])); zone_1.append(float(rows[i][5+3])); zone_1.append(float(rows[i][8+3])); zone_1.append(float(rows[i][12+3]));
                    zone_3.append(float(rows[i][4+3])); zone_3.append(float(rows[i][7+3])); zone_3.append(float(rows[i][9+3])); zone_3.append(float(rows[i][10+3]));
                    zone_2.append(float(rows[i][2+3])); zone_2.append(float(rows[i][3+3])); zone_2.append(float(rows[i][6+3])); zone_2.append(float(rows[i][11+3]));
                    age.append(float(rows[i][1]));
                    i+=1;
        i+=1;

# Average and standard deviation
std_zone_1 = statistics.stdev(zone_1); std_zone_2 = statistics.stdev(zone_2); std_zone_3 = statistics.stdev(zone_3);
mean_zone_1 = np.mean(zone_1); mean_zone_2 = np.mean(zone_2); mean_zone_3 = np.mean(zone_3);

print("\x1B[1;37;44mExperimentation no.2: 7 residents\x1B[0m");
print("");
print("\x1B[1;36mAnswers\x1B[0;36m");
i=0; nb_people=0;
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Experiment n°2"):
            print(  rows[i+1][0],"\t|",rows[i+1][1],"\t|",rows[i+1][2],"\t|",rows[i+1][3],"\t|",
                    rows[i+1][4],"\t|",rows[i+1][5],"\t|",rows[i+1][6],"\t|",rows[i+1][7],"\t|",
                    rows[i+1][8],"\t|",rows[i+1][9],"\t|",rows[i+1][10],"\t|",rows[i+1][11],"\t|",
                    rows[i+1][12],"\t|",rows[i+1][13],"\t|",rows[i+1][14],"\t|",rows[i+1][15],"\t|");
            i+=2;
            while( i<len(rows) ):
                if (rows[i][0]=='8') : i = len(rows);
                else : print("\t",  rows[i][0],"\t|",rows[i][1],"\t|",rows[i][2],"\t|",rows[i][3],"\t\t|",
                                    rows[i][4],"\t|",rows[i][5],"\t|",rows[i][6],"\t|",rows[i][7],"\t|",
                                    rows[i][8],"\t|",rows[i][9],"\t|",rows[i][10],"\t|",rows[i][11],"\t|",
                                    rows[i][12],"\t|",rows[i][13],"\t|",rows[i][14],"\t|",rows[i][15],"\t|"); i+=1; nb_people+=1;
        i+=1;
print("");
print("\x1B[1;36mAverage and standard deviation\x1B[0;36m");
i=0;
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Experiment n°2"):
            i+=2;
            nb_people_str = "Personne no. \t| "; ligne1 = "Zone no.1 \t| "; ligne2 = "Zone no.2 \t| "; ligne3 = "Zone no.3 \t| "; j=1;
            while( j<=nb_people ) : nb_people_str += str(j) + "\t\t| "; j+=1;
            print(nb_people_str);
            while( i<len(rows) ):
                if (rows[i][0]=='8') : i = len(rows);
                else :
                    z1_mean_str = np.around(np.mean( [float(rows[i][1+3]),float(rows[i][5+3]),float(rows[i][8+3]),float(rows[i][12+3])]),2);
                    z1_std_str = np.around(statistics.stdev([float(rows[i][1+3]),float(rows[i][5+3]),float(rows[i][8+3]),float(rows[i][12+3])]),2);
                    z2_mean_str = np.around(np.mean([float(rows[i][4+3]),float(rows[i][7+3]),float(rows[i][9+3]),float(rows[i][10+3])]),2);
                    z2_std_str = np.around(statistics.stdev([float(rows[i][4+3]),float(rows[i][7+3]),float(rows[i][9+3]),float(rows[i][10+3])]),2);
                    z3_mean_str = np.around(np.mean([float(rows[i][2+3]),float(rows[i][3+3]),float(rows[i][6+3]),float(rows[i][11+3])]),2);
                    z3_std_str = np.around(statistics.stdev([float(rows[i][2+3]),float(rows[i][3+3]),float(rows[i][6+3]),float(rows[i][11+3])]),2);
                    ligne1 += str(z1_mean_str) + "±" + str(z1_std_str) + "\t| ";
                    ligne2 += str(z2_mean_str) + "±" + str(z2_std_str) + "\t| ";
                    ligne3 += str(z3_mean_str) + "±" + str(z3_std_str) + "\t| ";
                    i+=1;
        i+=1;
print(ligne1);
print(ligne2);
print(ligne3);
print("");
print("          \t| Average \t| Standard deviation \t|");
print("Age       \t|", np.around(np.mean(age),2), "\t|", np.around(statistics.stdev(age),2), "\t\t\t|");
print("Zone no.1 \t|", np.around(mean_zone_1,2), "\t\t|", np.around(std_zone_1,2), "\t\t\t|");
print("Zone no.2 \t|", np.around(mean_zone_2,2), "\t\t|", np.around(std_zone_2,2), "\t\t\t|");
print("Zone no.3 \t|", np.around(mean_zone_3,2), "\t\t|", np.around(std_zone_3,2), "\t\t\t|");

# Save histogram
values = [mean_zone_1, mean_zone_2, mean_zone_3];
errorValues = [std_zone_1, std_zone_2, std_zone_3];
pyplot.bar(range(len(values)), values, color = 'skyblue');
pyplot.errorbar(range(len(values)), values, yerr = errorValues,
    fmt = 'none', capsize = 10, ecolor = 'red', elinewidth = 1, capthick = 1);
pyplot.savefig('histo_v2_7.png', transparent = True); pyplot.close();




# ------------------------------------------------------------------------ #
print("\x1B[1;36m------------------------------------------------------------------------");
# Read datas
i=0; zone_1=[]; zone_2=[]; zone_3=[]; age=[];
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Experiment n°2"):
            i+=2;
            while( i<len(rows) ):
                if (rows[i][0]=='') : i = len(rows);
                else :
                    zone_1.append(float(rows[i][1+3])); zone_1.append(float(rows[i][5+3])); zone_1.append(float(rows[i][8+3])); zone_1.append(float(rows[i][12+3]));
                    zone_3.append(float(rows[i][4+3])); zone_3.append(float(rows[i][7+3])); zone_3.append(float(rows[i][9+3])); zone_3.append(float(rows[i][10+3]));
                    zone_2.append(float(rows[i][2+3])); zone_2.append(float(rows[i][3+3])); zone_2.append(float(rows[i][6+3])); zone_2.append(float(rows[i][11+3]));
                    age.append(float(rows[i][1]));
                    i+=1;
        i+=1;

# Average and standard deviation
std_zone_1 = statistics.stdev(zone_1); std_zone_2 = statistics.stdev(zone_2); std_zone_3 = statistics.stdev(zone_3);
mean_zone_1 = np.mean(zone_1); mean_zone_2 = np.mean(zone_2); mean_zone_3 = np.mean(zone_3);

print("\x1B[1;37;44mExperimentation no.2: all volunteers\x1B[0m");
print("");
print("\x1B[1;36mAnswers\x1B[0;36m");
i=0; nb_people=0;
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Experiment n°2"):
            print(  rows[i+1][0],"\t|",rows[i+1][1],"\t|",rows[i+1][2],"\t|",rows[i+1][3],"\t|",
                    rows[i+1][4],"\t|",rows[i+1][5],"\t|",rows[i+1][6],"\t|",rows[i+1][7],"\t|",
                    rows[i+1][8],"\t|",rows[i+1][9],"\t|",rows[i+1][10],"\t|",rows[i+1][11],"\t|",
                    rows[i+1][12],"\t|",rows[i+1][13],"\t|",rows[i+1][14],"\t|",rows[i+1][15],"\t|");
            i+=2;
            while( i<len(rows) ):
                if (rows[i][0]=='') : i = len(rows);
                else : print("\t",  rows[i][0],"\t|",rows[i][1],"\t|",rows[i][2],"\t|",rows[i][3],"\t\t|",
                                    rows[i][4],"\t|",rows[i][5],"\t|",rows[i][6],"\t|",rows[i][7],"\t|",
                                    rows[i][8],"\t|",rows[i][9],"\t|",rows[i][10],"\t|",rows[i][11],"\t|",
                                    rows[i][12],"\t|",rows[i][13],"\t|",rows[i][14],"\t|",rows[i][15],"\t|"); i+=1; nb_people+=1;
        i+=1;
print("");
print("\x1B[1;36mAverage and standard deviation\x1B[0;36m");
i=0;
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Experiment n°2"):
            i+=2;
            nb_people_str = "Personne no. \t| "; ligne1 = "Zone no.1 \t| "; ligne2 = "Zone no.2 \t| "; ligne3 = "Zone no.3 \t| "; j=1;
            while( j<=nb_people ) : nb_people_str += str(j) + "\t\t| "; j+=1;
            print(nb_people_str);
            while( i<len(rows) ):
                if (rows[i][0]=='') : i = len(rows);
                else :
                    z1_mean_str = np.around(np.mean( [float(rows[i][1+3]),float(rows[i][5+3]),float(rows[i][8+3]),float(rows[i][12+3])]),2);
                    z1_std_str = np.around(statistics.stdev([float(rows[i][1+3]),float(rows[i][5+3]),float(rows[i][8+3]),float(rows[i][12+3])]),2);
                    z2_mean_str = np.around(np.mean([float(rows[i][4+3]),float(rows[i][7+3]),float(rows[i][9+3]),float(rows[i][10+3])]),2);
                    z2_std_str = np.around(statistics.stdev([float(rows[i][4+3]),float(rows[i][7+3]),float(rows[i][9+3]),float(rows[i][10+3])]),2);
                    z3_mean_str = np.around(np.mean([float(rows[i][2+3]),float(rows[i][3+3]),float(rows[i][6+3]),float(rows[i][11+3])]),2);
                    z3_std_str = np.around(statistics.stdev([float(rows[i][2+3]),float(rows[i][3+3]),float(rows[i][6+3]),float(rows[i][11+3])]),2);
                    ligne1 += str(z1_mean_str) + "±" + str(z1_std_str) + "\t| ";
                    ligne2 += str(z2_mean_str) + "±" + str(z2_std_str) + "\t| ";
                    ligne3 += str(z3_mean_str) + "±" + str(z3_std_str) + "\t| ";
                    i+=1;
        i+=1;
print(ligne1);
print(ligne2);
print(ligne3);
print("");
print("          \t| Average \t| Standard deviation \t|");
print("Age       \t|", np.around(np.mean(age),2), "\t|", np.around(statistics.stdev(age),2), "\t\t|");
print("Zone no.1 \t|", np.around(mean_zone_1,2), "\t\t|", np.around(std_zone_1,2), "\t\t\t|");
print("Zone no.2 \t|", np.around(mean_zone_2,2), "\t\t|", np.around(std_zone_2,2), "\t\t\t|");
print("Zone no.3 \t|", np.around(mean_zone_3,2), "\t\t|", np.around(std_zone_3,2), "\t\t\t|");

# Save histogram
values = [mean_zone_1, mean_zone_2, mean_zone_3];
errorValues = [std_zone_1, std_zone_2, std_zone_3];
pyplot.bar(range(len(values)), values, color = 'skyblue');
pyplot.errorbar(range(len(values)), values, yerr = errorValues,
    fmt = 'none', capsize = 10, ecolor = 'red', elinewidth = 1, capthick = 1);
pyplot.savefig('histo_v2_12.png', transparent = True); pyplot.close();




#   void ERROR( std::string msg ) { std::cout << "\x1B[1;37;41m" << msg << "\x1B[0m" << std::endl; exit(0); }
#   void error( std::string msg ) { std::cout << "\x1B[1;31m" << msg << "\x1B[0m" << std::endl; }
#   void warning( std::string msg ) { std::cout << "\x1B[1;33m" << msg << "\x1B[0m" << std::endl; }
#   void debug( std::string msg ) { std::cout << "\x1B[1;45;37m" << msg << "\x1B[0m" << std::endl; }
#   void subdebug( std::string msg ) { std::cout << "\x1B[1;35m" << msg << "\x1B[0m" << std::endl; }
#   void subsubdebug( std::string msg ) { std::cout << "\x1B[0;35m" << msg << "\x1B[0m" << std::endl; }
#   void info( std::string msg ) { std::cout << "\x1B[1;36m" << msg << "\x1B[0m" << std::endl; }
#   void subinfo( std::string msg ) { std::cout << "\x1B[0;36m" << msg << "\x1B[0m" << std::endl; }
#   void subsubinfo( std::string msg ) { std::cout << "\x1B[1;34m" << msg << "\x1B[0m" << std::endl; }
