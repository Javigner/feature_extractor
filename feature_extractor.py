import sys

def dispersion(data, days):
    result = 0
    tmp = 0
    if len(data) < days:
        print('List length must be at least equal to days')
        return
    for i in range(len(data)):
        if (i > len(data) - days):
            break 
        for j in range(days - 1):
            tmp += abs(data[i + 1 + j] - data[i + j])
        if tmp > result:
            result = tmp
        tmp = 0
    print("Highest dispersion for {} days: {}".format(days, result))

def compare_peak(peak, peak_tmp):
    if len(peak) > len(peak_tmp):
        return(peak)
    else:
        return(peak_tmp)

def longest_peak(data, valley):
    peak = []
    peak_tmp = []
    rise = 1
    for i in range(len(data)):
        if i == 0:
            peak.append(data[0])
            continue
        if (data[i] >= data[i - 1] and valley == 0) or (data[i] < data[i - 1] and valley == 1):
            if rise == 0:
                peak_tmp = compare_peak(peak, peak_tmp)
                peak = []
                peak.append(data[i - 1])
                rise = 1
            peak.append(data[i])
        elif (data[i] <= data[i - 1] and valley == 0) or (data[i] >= data[i - 1] and valley == 1):
            if rise == 1:
                rise = 0
            peak.append(data[i])
        else:
            peak_tmp = compare_peak(peak, peak_tmp)
            peak = []
    peak_tmp = compare_peak(peak, peak_tmp)
    if (valley == 1):
        if peak_tmp[len(peak_tmp) - 1] == min(peak_tmp) or peak_tmp[0] == min(peak_tmp):
            print("The list does not contain gaps")
            return
    if (valley == 0):
        if peak_tmp[len(peak_tmp) - 1] == max(peak_tmp) or peak_tmp[0] == max(peak_tmp):
            print("The list does not contain peak")
            return
        print("Longest valley: {}, duration: {}, amplitude: {}".format(peak_tmp, len(peak_tmp), max(peak_tmp) - min(peak_tmp)))  
    else:
        print("Longest peak: {}, duration: {}, amplitude: {}".format(peak_tmp, len(peak_tmp), max(peak_tmp) - min(peak_tmp)))           
            
def feature_extractor(data):
    if isinstance(data, list) == False:
        sys.exit('data must be a list of integer')
    for number in data:
        if isinstance(number, int) == False:
            sys.exit('Your list must contain only integer')
    longest_peak(data, 0)
    longest_peak(data, 1)
    dispersion(data, 3)
    dispersion(data, 5)
    dispersion(data, 11)
