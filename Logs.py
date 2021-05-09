import csv

def load_best():
    best_chrom = []
    best_dist = 0
    try:
        with open('best.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for i, val in enumerate(reader):
                if i == 0:
                    best_dist = float(val[0])
                else:
                    best_chrom.append(int(val[0]))
    except:
        print('Could not find best.csv')
        print('Init new best logs')
        best_chrom = []
        best_dist = 1000000

    print('best distance : ', best_dist)
    return best_dist, best_chrom

def save_best(best_dist, best_chrom):
    with open('best.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([float(best_dist)])
        for val in best_chrom:
            writer.writerow([int(val)])
    print('saved best distance')