# /*
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
#  */

texto = "Lorem ipsum dolor sit amet consectetur adipiscing elit Duis hendrerit ex ac scelerisque mollis Mauris eu vestibulum ante Pellentesque egestas eros in dui aliquet a imperdiet velit viverra Curabitur nisi diam bibendum vitae felis vitae ullamcorper sagittis metus Integer eu rutrum lorem Vivamus aliquet sem vitae convallis tristique risus purus elementum nibh ac tempor lorem lorem sed massa Vestibulum nisl risus efficitur nec blandit in sodales et sapien Nam ut sodales erat Integer nec lorem consectetur odio fringilla luctus eu a massa Sed nunc enim euismod et commodo eget rhoncus ac tellus Integer pretium elit sed convallis gravida purus est auctor velit vel posuere ligula nibh a ante Donec pretium rutrum turpis at dapibus ligula eleifend a Duis tincidunt ac lorem sit amet convallis Interdum et malesuada fames ac ante ipsum primis in faucibus Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aliquam egestas tellus sit amet metus pulvinar sit amet lobortis dui tempor Vestibulum eu orci rutrum hendrerit metus a pellentesque neque Ut suscipit fringilla egestas Vivamus velit urna blandit at finibus id luctus vitae nisi Curabitur rhoncus arcu purus in commodo lectus rhoncus in Mauris egestas bibendum purus mattis congue metus tempus dapibus Maecenas felis nulla sodales cursus massa vel varius dictum lorem Integer non nisi sit amet odio maximus congue Integer at sodales risus non rhoncus ipsum Ut neque enim tristique ac orci id aliquam luctus felis Proin risus sem tristique vel odio non dictum faucibus nulla Nunc at porta velit Vestibulum maximus luctus magna in sollicitudin tortor blandit vitae Etiam eu placerat dui sit amet imperdiet tortor Donec sagittis est eget vestibulum tempus metus metus porttitor lectus id rhoncus libero magna eget mi Curabitur posuere risus sit amet nibh rhoncus id gravida sem feugiat Sed gravida leo semper dapibus congue Sed porta tortor non purus dictum sed accumsan ligula tempor Nulla ac justo id nisi aliquam molestie Etiam et sapien neque Aliquam erat volutpat Nam tristique varius turpis et tempus quam condimentum a Etiam ac arcu at velit interdum eleifend Cras ut sem arcu Ut hendrerit mollis augue ut dapibus Duis pretium ultricies nunc ut fermentum Phasellus et purus at massa auctor vehicula Mauris tristique leo id euismod eleifend Cras vel ante sem Donec fringilla nibh quis hendrerit imperdiet purus massa ullamcorper nunc mollis ullamcorper lectus nunc ac tellus Etiam ullamcorper risus vel varius feugiat Nam porta eros nibh et imperdiet ex feugiat at Phasellus venenatis diam et lorem convallis finibus placerat massa condimentum Curabitur mi sem congue non finibus vel vestibulum ut mi Suspendisse consectetur a nisl ac ultrices In ut lorem nibh Curabitur vehicula laoreet augue ac ultricies mauris tempor nec Donec varius urna eu mauris imperdiet in ornare leo venenatis Pellentesque placerat diam eget commodo auctor tortor turpis venenatis nisl ut accumsan enim nulla et dolor Aenean ut facilisis enim Fusce sagittis accumsan dui quis elementum urna tempor sed Quisque pharetra mi dapibus malesuada tincidunt Nunc vehicula sed est sed dictum Morbi libero mi vehicula ac pellentesque sodales"


lista = texto.split()
conjunto = list(set(lista))
for palabra in conjunto:
    contador = 0
    for word in lista:
        if palabra == word:
            contador += 1
    print('la palabra ' + palabra + ' aparece ' + str(contador) + ' veces')
