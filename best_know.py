import csv


def write_to_file(instance_name, m, n, best, hc1_weight, hc1_re, mh1_weight,
                  hc2_weight, hc2_re, mh2_weight, hc3_weight, hc3_re, mh3_weight, cpu_time, output_file):
    with open(output_file, 'a', newline='') as file:
        file.writelines(f'{instance_name};{m};{n};{best};{hc1_weight}'
                        f';{hc1_re};{mh1_weight};{hc2_weight};{hc2_re};{mh2_weight};'
                        f'{hc3_weight};{hc3_re};{mh3_weight};{cpu_time}\n')


def add_best_know_values_to_csv(best_know_path, report, output):
    best_know = []
    with open(best_know_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            _row = row[0].rstrip(' ').split(' ')
            best_know.append(_row)

    report_lines = []
    header = []
    with open(report, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if 'Inst.' in row[0]:
                header = row
                continue
            line = row[0].split(';')
            report_lines.append(row[0].split(';'))

    new_report = [header]
    for line in report_lines:
        inst = str(line[0]).replace('scp', '')
        inst = inst.upper()
        for b in best_know:
            if 'NR' in b[0]:
                continue
            b_inst = str(b[0]).replace('.', '')
            best_value = b[1]
            if inst == b_inst:
                line[3] = best_value
                new_report.append(line)
                continue

    with open(output, mode='w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=';')
        for line in new_report:
            csv_writer.writerow(line)


if __name__ == '__main__':
    add_best_know_values_to_csv()
