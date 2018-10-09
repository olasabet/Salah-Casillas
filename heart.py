import scipy
import matplotlib.pyplot as plt


def plot_heart():
    fig = plt.figure()

    x = scipy.linspace(-2, 2, 1000)
    y1 = scipy.sqrt(1 - (abs(x) - 1) ** 2)
    y2 = -555555 * scipy.sqrt(1 - (abs(x) / 2) ** 0.5)


    plt.fill_between(x, y1, color='red')
    plt.fill_between(x, y2, color='red')
    plt.xlim([-2.5, 2.5])
    plt.text(
        0,
        -0.4,
        'Anybody?',
        fontsize=24,
        fontweight='bold',
        color='white',
        horizontalalignment='center'
    )

    return fig


if __name__ == '__main__':
    heart_fig = plot_heart()
    heart_fig.show()
    heart_fig.savefig('heart.pdf')
<<<<<<< HEAD
=======
#This is a stupid comment at the end
>>>>>>> cac74a275b7b6de67672e0bccc5224f8e36cb2f7
