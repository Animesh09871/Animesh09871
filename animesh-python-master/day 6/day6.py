import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress



with open('Joining_Status.csv','r')as file_to_read:
    data=csv.reader(file_to_read)
    for i in data:
        print(i)

        with open('HR_Hiring_details_transaction.csv', 'r') as file_to_read:
            data = csv.reader(file_to_read)
            for i in data:
                print(i)

    with open('LOB_Master.csv', 'r') as file_to_read:
                    data = csv.reader(file_to_read)
                    for i in data:
                        print(i)



fields = ['LOB_Id', 'LOB', 'Description']

data = [
    [1, 'ERS', 'ERS typically stands for "Enterprise Resource Services"'],
    [2, 'INFRA', 'INFRA often represents "Infrastructure'],
    [3, 'Healthcare', 'The Healthcare LOB likely relates to services and operations '],
    [4, 'BFSI', ' BFSI stands for "Banking, Financial Services, and Insurance.'],
    [5, 'CSMP', 'The meaning of CSMP is not widely recognized'],
    [6, 'ETS', 'ETS could refer to "Enterprise Technology Services'],
    [7, 'AXON', 'The term AXON is not specific enough to provide a detailed description'],
    [8, 'EAS', 'EAS may stand for "Enterprise Application Services'],
    [9, 'MMS', 'MMS could represent "Managed Mobility Services']
]
with open('LOB_Master.csv', 'w') as file_to_write:
 exec = csv.writer(file_to_write)
 exec.writerow(fields)
 exec.writerows(data)

with open('LOB_Master.csv', 'r') as file_to_read:
        data = csv.reader(file_to_read)
        for i in data:
         print(i)

percent_hikes = []
with open('HR_Hiring_details_transaction.csv', 'r') as file_to_read:
    data = csv.DictReader(file_to_read)
    for row in data:
        percent_hike = float(row['Percent_hike_offered_in_CTC'])
        percent_hikes.append(percent_hike)
        max_percent_hike = np.max(percent_hikes)
        print("Maximum Percent Hike:", max_percent_hike)


Lob=pd.read_csv('LOB_Master.csv')
print(Lob)
Joining=pd.read_csv('Joining_Status.csv')
print(Joining)
Hr=pd.read_csv('HR_Hiring_details_transaction.csv')
print(Hr)

concate_date = pd.concat([Lob,Joining])
concate_date.head()
concate_date1 = pd.merge(Hr, Joining, on='Candidate_Ref', how='inner')
concate_date.head()
concate_date2 = pd.merge(Lob, concate_date1, on='LOB_Id', how='inner')
concate_date2.head()

#

fh = pd.read_csv('Joining_Status.csv')
print(fh.head(6000))


joined = fh[fh['Status'] == 'Joined']
not_joined = fh[fh['Status'] == 'Not joined']

joined_count = len(joined)
not_joined_count = len(not_joined )


labels = ['Joined', 'Not joined']
counts = [joined_count, not_joined_count]

plt.bar(labels, counts, color='red')
plt.xlabel('Status')
plt.ylabel('Number of Candidates')
plt.title('Joined vs. Not joined')
plt.show()

Min_expected_hike= Hr['Percent_hike_expected_in_CTC'].min()
Min_offered_hike= Hr['Percent_hike_offered_in_CTC'].min()
Diff_in_CTC= Hr['Percent_difference_CTC'].min()
print('Minimum expected hike in percentage: ', Min_expected_hike)
print('Minimum expected hike in percentage: ', Min_offered_hike)
print('Differce in CTC: ', Diff_in_CTC)





