import sys

#def dispersion(data, days):
    

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
        print("Longest valley:", peak_tmp, "Duration:", len(peak_tmp), "Amplitude:", max(peak_tmp) - min(peak_tmp))   
    else:
        print("Longest Peak:", peak_tmp, "Duration:", len(peak_tmp), "Amplitude:", max(peak_tmp) - min(peak_tmp))           
            
def main():
    test = [62, 65, 63, 72, 71, 60, 61, 65, 70, 73, 68, 70, 73, 71, 67, 66, 65]
    test2 = [65, 62, 62, 61]
    test3 = [65, 64, 64, 64, 69]
    test4 = [63, 62, 68]
    longest_peak(test, 0)
    longest_peak(test, 1)

if __name__ == "__main__":
    main();