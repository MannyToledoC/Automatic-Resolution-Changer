import PySimpleGUI as sg
import random
import SortAlgos as sa

BAR_SPACE = 11
BAR_WIDTH = 10
BAR_OFFSET = 3

DATA_SIZE = GRAPH_SIZE = (700, 500) # (Width, Height)


def draw_data(graph, values):
    for i, value in enumerate(values):
        graph.draw_rectangle(top_left=(i * BAR_SPACE + BAR_OFFSET, value), # (x, y)
                             bottom_right=(i * BAR_SPACE + BAR_OFFSET + BAR_WIDTH, 0), fill_color='#FF0000')


def draw_process(graph, window, chosen_algorithm):
    timeout = 10

    for partially_sorted_list in chosen_algorithm:
        event, values = window.read(timeout=timeout)
        if event is None:
            break
        graph.Erase()
        draw_data(graph, partially_sorted_list)
        timeout = int(values['-SPEED-'])

    return True
    # window.close()


def assemble():
    sg.change_look_and_feel('Black')
    num_bars = DATA_SIZE[0] // (BAR_WIDTH + 1)

    # 500 // 10 * (1->2->3->n) determines height of each new rectangle via the max height
    lis = [DATA_SIZE[1] // num_bars * i for i in range(1, num_bars)]
    random.shuffle(lis)

    graph = sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE) # (Canvas size, Bottom left point, Top right point)

    layout = [[sg.Button('Bubble', key="_BUBBLE_"), sg.Button('Insertion', key="_INSERTION_"),
               sg.Button('Scramble', key='_SCRAMBLE_')],
              [graph],
              [sg.T('Fast'), sg.Slider((0, 20), orientation='h', default_value=10, key='-SPEED-'),
               sg.T('Slow')]]

    window = sg.Window('Sorting Visualizer', layout, finalize=True)

    draw_data(graph, lis)

    while True:
        event, values = window.read()
        ran = False
        running = False
        print(event)
        if event is None:
            break
        if event == '_BUBBLE_':
            if ran is True:
                random.shuffle(lis)
                graph.Erase()
                draw_data(graph, lis)

            chosen_algorithm = sa.bubble_sort(lis)
            print('hello')
            draw_process(graph, window, chosen_algorithm)
        if event == '_INSERTION_':
            if ran is True:
                random.shuffle(lis)
                graph.Erase()
                draw_data(graph, lis)

            chosen_algorithm = sa.insertion_sort(lis)
            draw_process(graph, window, chosen_algorithm)
        if event == '_SCRAMBLE_':
            if ran is True:
                random.shuffle(lis)
                graph.Erase()
                draw_data(graph, lis)


assemble()

# todo make button unclickable while the method is running, by adding a bool to the method
# todo consider using threads https://realpython.com/intro-to-python-threading/
