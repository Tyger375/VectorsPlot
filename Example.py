from VectorsPlot import Vector2D, Grafico


def graficovettori():
    vettore = Vector2D(15, 15)

    print(vettore + Vector2D(2, 3), vettore - Vector2D(2, 3))
    test = Grafico()
    test.set_size((Vector2D(0, 0), vettore))
    test.set_x_interval(1)
    test.set_y_interval(1)
    test.set_title("sos")
    primovettore = Vector2D(2, 4)
    secondovettore = Vector2D(3, 1)
    #test.add_arrow(secondovettore)
    #test.punta_coda([primovettore, secondovettore])
    test.parallelogramma([primovettore, secondovettore, Vector2D(2, 3)])
    print(primovettore + secondovettore + Vector2D(2, 3))
    #test.add_arrow(primovettore)
    #test.add_arrow(vectorfrom=primovettore, vectorto=secondovettore)
    #test.add_arrow(primovettore + secondovettore)
    #test.add_arrow(Vector2D(2, 3))
    test.set_grid(True)
    test.save("test.png")


def grafico():
    #Forza-allungamento
    grafico = Grafico()
    grafico.set_size((Vector2D(0, 0), Vector2D(2, 20)))
    grafico.set_x_interval(0.25)
    grafico.set_y_interval(1)
    grafico.plot([2, 1], [2, 1], "points")
    grafico.save()


grafico()
#ax.arrow(2.0, 4.0, 6.0, test = Grafico()4#.0,.save() head_width=0.5, head_length=0.7, fc='lightblue', ec='black')

#plt.grid()

#plt.xlim(0,10#)
#plt.ylim(0#,10)

#plt.title#('How to plot a #vector in matplotlib ?',fontsize=10)

#plt.savefig('how_to_plot_#a_vector_in_matplotlib_fig1.png', bbox_inches='tight')
#plt.show()
#plt.close()
