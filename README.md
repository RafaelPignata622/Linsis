# Linsis
Se propone crear un paquete de análisis de espectroscopia de ranura larga e IFU en las bandas del visible y del infrarrojo cercano. El mismo tendrá como imput uno o más espectros con sus correspondientes “headers”.El paquete tendrá tres salidas a elección del usuario:

   1) Ajuste del continuo espectral + identificación y ajuste automático de todas las líneas de emisión y absorción presentes en el espectro dentro de un límite de S/N establecido por el usuario. Esta salida estará dada principalmente aplicando el paquete specutils (o similar) ya existente.

   2) Ajuste de continuo espectral + identificación automática de lineas + ajuste manual de lineas elegidas por el usuario. El ajuste manual puede tener múltiples componentes, la cantidad de componentes y sus parámetros serán determinados interactivamente por el usuario.

   3) Tomando como input la salida de la opción 2, es decir la cantidad de componentes ajustados a una determinada línea y sus parámetros, se ajustan automáticamente otras líneas presentes en el espectro, elegidas por el usuario, que teóricamente deben tener la misma cantidad de componentes y separación entre componentes que la línea que se utiliza para el imput. Esto es de gran utilidad al realizar ajustes multicomponentes en líneas de baja S/N.


En cualquiera de las tres opciones, el paquete producirá una tabla con todas las líneas identificadas y sus mediciones (centro, flujo, ancho equivalente, fwhm, etc) y un plot mostrando el espectro rectificado, además se podrán obtener los plots de las líneas ajustadas manualmente. Por otro lado, utilizando paquetes (e.g. PyNeb), se podrían realizar algunos diagnósticos que se pueden realizar rápidamente para cada tipo de objeto astronómico, como por ejemplo: diagramas de cocientes de líneas, curvas de velocidad radial, extinción interestelar, temperatura electrónica, densidad electrónica, etc.
