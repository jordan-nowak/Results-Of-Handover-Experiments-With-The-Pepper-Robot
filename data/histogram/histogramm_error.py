#!/usr/bin/python3.5
# -*-coding:utf_8 -*

from matplotlib import pyplot
import numpy as np
import statistics



import csv
file = open("../data.csv");
csvreader = csv.reader(file);
header = next(csvreader);
print(header);
rows = [];
for row in csvreader:
    rows.append(row);
file.close();

# ------------------------------------------------------------------------ #
# Read datas
i=0; zone_1=[]; zone_2=[]; zone_3=[]; zone_4=[];
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Experiment n°1"):
            i+=2;
            while( rows[i] ):
                zone_1.append(float(rows[i][4]));
                zone_2.append(float(rows[i][5]));
                zone_3.append(float(rows[i][6]));
                zone_4.append(float(rows[i][7]));
                i+=1;
        i+=1;

# Average and standard deviation
std_zone_1 = statistics.stdev(zone_1); std_zone_2 = statistics.stdev(zone_2); std_zone_3 = statistics.stdev(zone_3); std_zone_4 = statistics.stdev(zone_4);
mean_zone_1 = np.mean(zone_1); mean_zone_2 = np.mean(zone_2); mean_zone_3 = np.mean(zone_3); mean_zone_4 = np.mean(zone_4);
print("\nData:\nZone no.1:", np.around(zone_1,2), "\nZone no.2:", np.around(zone_2,2), "\nZone no.3:", np.around(zone_3,2), "\nZone no.4:", np.around(zone_4,2));
print("\nAverage:\nZone no.1:", np.around(mean_zone_1,2), "\nZone no.2:", np.around(mean_zone_2,2), "\nZone no.3:", np.around(mean_zone_3,2), "\nZone no.4:", np.around(mean_zone_4,2));
print("\nStandard deviation:\nZone no.1:", np.around(std_zone_1,2), "\nZone no.2:", np.around(std_zone_2,2), "\nZone no.3:", np.around(std_zone_3,2), "\nZone no.4:", np.around(std_zone_4,2));

# Save histogram
values = [mean_zone_1, mean_zone_2, mean_zone_3, mean_zone_4];
errorValues = [std_zone_1, std_zone_2, std_zone_3, std_zone_4];
pyplot.bar(range(len(values)), values, color = 'skyblue');
pyplot.errorbar(range(len(values)), values, yerr = errorValues,
    fmt = 'none', capsize = 10, ecolor = 'red', elinewidth = 1, capthick = 1);
pyplot.savefig('histogram_v1.png', transparent = True); pyplot.close();
pyplot.close();


# ------------------------------------------------------------------------ #
# Read datas
i=0; zone_1=[]; zone_2=[]; zone_3=[];
while(i<len(rows)):
    if not(rows[i]):
        i+=1;
    else:
        if (rows[i][0]=="Experiment n°2"):
            i+=2;
            while( i<len(rows) ):
                zone_1.append(float(rows[i][1+3])); zone_1.append(float(rows[i][5+3])); zone_1.append(float(rows[i][8+3])); zone_1.append(float(rows[i][12+3]));
                zone_3.append(float(rows[i][4+3])); zone_3.append(float(rows[i][7+3])); zone_3.append(float(rows[i][9+3])); zone_3.append(float(rows[i][10+3]));
                zone_2.append(float(rows[i][2+3])); zone_2.append(float(rows[i][3+3])); zone_2.append(float(rows[i][6+3])); zone_2.append(float(rows[i][11+3]));
                i+=1;
        i+=1;


# Average and standard deviation
std_zone_1 = statistics.stdev(zone_1); std_zone_2 = statistics.stdev(zone_2); std_zone_3 = statistics.stdev(zone_3);
mean_zone_1 = np.mean(zone_1); mean_zone_2 = np.mean(zone_2); mean_zone_3 = np.mean(zone_3);
print("\nData:\nZone no.1:", np.around(zone_1,2), "\nZone no.2:", np.around(zone_2,2), "\nZone no.3:", np.around(zone_3,2));
print("\nAverage:\nZone no.1:", np.around(mean_zone_1,2), "\nZone no.2:", np.around(mean_zone_2,2), "\nZone no.3:", np.around(mean_zone_3,2));
print("\nStandard deviation:\nZone no.1:", np.around(std_zone_1,2), "\nZone no.2:", np.around(std_zone_2,2), "\nZone no.3:", np.around(std_zone_3,2));

# Save histogram
values = [mean_zone_1, mean_zone_2, mean_zone_3];
errorValues = [std_zone_1, std_zone_2, std_zone_3];
pyplot.bar(range(len(values)), values, color = 'skyblue');
pyplot.errorbar(range(len(values)), values, yerr = errorValues,
    fmt = 'none', capsize = 10, ecolor = 'red', elinewidth = 1, capthick = 1);
pyplot.savefig('histogram_v2.png', transparent = True); pyplot.close();
pyplot.close();
