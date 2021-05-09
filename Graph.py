import matplotlib.pyplot as plt
import matplotlib.colors as colors
'''
한 fig에 최대 12가지 선 그래프
x_list :    한 그래프에 대한 x축 값들을 가지고 있는 2차원 리스트
            x_list[i] : i번째 그래프
            x_list[0][i] : 0번째 그래프의 i번째 x값
y_list :    한 그래프에 대한 y축 값들을 가지고 있는 2차원 리스트
            y_list[i] : i번째 그래프
            y_list[0][i] : 0번째 그래프의 i번째 y값
legends :   각 그래프가 어떤 그래프인지 명시하는 String 리스트
            ex) ['graphA', 'graphB']
'''
def draw_graph(x_list, y_list, xlabel, ylabel, legends=[]):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'darkgoldenrod', 'olive', 'steelblue', 'maroon', 'purple']
    for i in range(len(x_list)):
        print('i : ', i)
        plt.plot(x_list[i], y_list[i], colors[i])
    '''
    try:
        for i in range(len(x_list)):
            plt.plot(x_list[i], y_list[i], colors[i])
    except:
        if (len(x_list) > 7):
            print('Error : 한 figure에 7개 이상의 그래프를 그릴 수 없습니다!')
        else:
            print('그래프 그리기 오류!')
        print('그래프 그리기를 건너뜁니다...')
        plt.close()
        return
    '''

    x_min = 10000000
    x_max = 0
    y_min = 10000000
    y_max = 0
    for cur_list in x_list:
        cur_Xmin = min(cur_list)
        cur_Xmax = max(cur_list)
        if x_min > cur_Xmin:
            x_min = cur_Xmin
        if x_max < cur_Xmax:
            x_max = cur_Xmax
    for cur_list in y_list:
        cur_Ymin = min(cur_list)
        cur_Ymax = max(cur_list)
        if y_min > cur_Ymin:
            y_min = cur_Ymin
        if y_max < cur_Ymax:
            y_max = cur_Ymax
    x_max += x_max/10
    y_max += y_max/10
            
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(legends)
    plt.axis([x_min, x_max, y_min, y_max])
    plt.show()
    