# Spaceship Titanic
Repositorio para el equipo 5 de la concentración de IA del reto de kaggle.

## Correcciones
- La principal corrección del modelo fue que estabamos tratando los valores nulos de forma general, pero después separamos aquellos que estaban en cryo-sleep y aquellos que no para realizar la imputación de datos por separado bajo la premisa de que "una persona en cryo-sleep no puede gastar lo mismo que una persona que no está en animación suspendida".
- La segunda corrección más importante fue que separamos la columna "cabin" para crear las columnas "deck" y "side" que nos pueden proporcionar más información sobre dónde se encuentra el pasajero.
- La tercera corrección fue que separamos la columna "passenger_id" utilizando los últimos dos digitos de esta columna para crear la columna "passenger_group".
Con estas correcciones alcanzamos un score en Kaggle de 0.80757.

## Correcciones adicionales post-entrega
Una vez que realizamos la presentación, se nos comentó que para la creación de la columna "passenger_group" no se debían de utilizar los últimos dos dígitos de la columna "passenger_id", sino que más bien los primeros 4 dígitos antes del guión bajo, son los que representan el grupo de forma que gggg_pp gggg representando el grupo y pp el id de la persona en el grupo. Este cambio subió nuestro score en Kaggle hasta 0.80780.
