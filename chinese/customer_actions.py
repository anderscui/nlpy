import jieba
import csv

notes = []
source_file = 'actions.csv'
#source_file = 'customer_actions.csv'
with open(source_file, 'rb') as csvfile:
    actions = csv.reader(csvfile, delimiter=',')
    for row in actions:

        # print row
        try:
            cid = int(row[0])
            status = row[1]
            task_type = row[2]
            school = row[-1]
            note = ",".join(row[3:-1])

            print '%d; %s; %s; %s -> %s' % (cid, status, task_type, school, note)
            notes.append([cid, note])
        except ValueError as e:
            print(row[0])
            print(row)

total_count = len(notes)
empty_count = 0
has_written = 0
with open('result.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    for note in notes:
        note[1] = note[1].strip()
        if note[1]:
            csvwriter.writerow(list(note))
        else:
            empty_count += 1

        has_written += 1
        if has_written % 1000 == 0:
            print has_written

print '%d of %d' % (empty_count, total_count)