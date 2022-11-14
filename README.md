# Proyecto backend test bsale

Para la generación de los endpoint se utilizo el lenguaje [Python](https://www.python.org/) y en especifico el framework [Django](https://www.djangoproject.com/), junto el paquete django-cors-header para el manejo de las peticiones hacia los endpoint.

El objetivo de proyecto es presentar una API que pueda ser consumida por un frontend independiente del desarrollo backend, por lo cual se hizo deploy de la aplicación por separado del frontend.

Las tecnologías usadas para el desarrollo son las siguiente:
- [Django](ttps://www.djangoproject.com/)
- [Django-cors-header](https://github.com/adamchainz/django-cors-headers)

El deploy de la aplicación se realizo en la plataforma de Heroku en el sigueinte enlace [Backend](https://test-backend-bsale.herokuapp.com/).

**Para el consumo de la aplicación se tienen los siguiente endpoints:**

## **GET Lista de categorías**

**GET** ```api/v0/categories/``` *retorna todas las categorías de la base de datos*

- Respuesta

```json
{
  "message": "success",
  "categories": [
    {
      "id": 1,
      "name": "bebida energetica"
    },
    {
      "id": 2,
      "name": "pisco"
    },
    {
      "id": 3,
      "name": "ron"
    }
  ]
}
```
## **GET Lista de productos por categoria**

**GET** ```api/v0/categories/[id]``` *Retorna todos los productos relacionados con la categoría*

- Parametros
  - ***id*** Identificador de la categoria de la cual se obtendran los productos.

- Ejemplos
  - ```GET api/v0/categories/1```
  - ```GET api/v0/categories/3```

- Respuesta

```json
{
  "message": "success",
  "products": [
    {
      "id": 5,
      "name": "ENERGETICA MR BIG",
      "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/misterbig3308256.jpg",
      "price": 1490,
      "discount": 20,
      "category_id": 1
    },
    {
      "id": 6,
      "name": "ENERGETICA RED BULL",
      "url_image": "https://dojiw2m9tvv09.cloudfront.net/11132/product/redbull8381.jpg",
      "price": 1490,
      "discount": 0,
      "category_id": 1
    }
  ]
}
```