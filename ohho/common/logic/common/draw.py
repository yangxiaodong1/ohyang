# try:
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt


class Draw(object):
    @staticmethod
    def draw_line(x_list, y_list, label_list, x_label, y_label, title, name):
        xy = zip(x_list, y_list, label_list)
        for x, y, label in xy:
            plt.plot(x, y, label=label)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.legend()
        path = 'static/draw/'
        path_name = path + name
        plt.savefig(path_name)


if __name__ == "__main__":
    print("start")
    x_list = [[1, 2, 3], [1, 2, 3]]
    y_list = [[5, 7, 4], [10, 14, 12]]
    label_list = ['First Line', 'Second Line']
    x_label = 'x'
    y_label = 'y'
    title = 'test'
    name = 'test007.png'
    Draw.draw_line(x_list, y_list, label_list, x_label, y_label, title, name)
    print("end")
# except Exception as ex:
#     print(ex)
