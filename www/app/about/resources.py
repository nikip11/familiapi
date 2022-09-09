import json
from flask import request, jsonify
from flask_restful import Resource
from flask_cors import cross_origin


class SkillsResource(Resource):
  @cross_origin()
  def get(self):
    skills =  [
        {
        "id": "lenguajes",
        "name": "Lenguajes",
        "items": [
            {
            "name": "PHP",
            "icon": "php-plain",
            },
            {
            "name": "Symfony",
            "icon": "symfony-plain",
            },
            {
            "name": "Laravel",
            "icon": "laravel-plain",
            },
            {
            "name": "Python",
            "icon": "python-plain",
            },
            {
            "name": "Django",
            "icon": "django-plain",
            },
            {
            "name": "Javascript",
            "icon": "javascript-plain",
            },
            {
            "name": "NodeJS",
            "icon": "nodejs-plain",
            },
            {
            "name": "VUEjs",
            "icon": "vuejs-plain",
            },
            {
            "name": "Angular",
            "icon": "angularjs-plain",
            },
            {
            "name": "Typescript",
            "icon": "typescript-plain",
            },
            {
            "name": "jQuery",
            "icon": "jquery-plain",
            },
        ],
        },
        {
        "id": "database",
        "name": "Database",
        "items": [
            {
            "name": "MySQL",
            "icon": "mysql-plain",
            },
            {
            "name": "SQLServer",
            "icon": "sqlserver-plain",
            },
            {
            "name": "MongoDB",
            "icon": "mongodb-plain",
            },
            {
            "name": "Redis",
            "icon": "redis-plain",
            },
        ],
        },
        {
        "id": "cms",
        "name": "CMS",
        "items": [
            {
            "name": "Wordpress",
            "icon": "wordpress-plain",
            },
            {
            "name": "Drupal",
            "icon": "drupal-plain",
            },
            {
            "name": "Prestashop",
            "icon": "prestashop-plain",
            },
        ],
        },
        {
        "id": "Maquetación",
        "name": "Maquetación",
        "items": [
            {
            "name": "HTML5",
            "icon": "html5-plain",
            },
            {
            "name": "CSS3",
            "icon": "css3-plain",
            },
            {
            "name": "Bootstrap",
            "icon": "bootstrap-plain",
            },
            {
            "name": "Sass",
            "icon": "sass-plain",
            },
        ],
        },
        {
        "id": "Varios",
        "name": "Varios",
        "items": [
            {
            "name": "Git",
            "icon": "git-plain",
            },
            {
            "name": "Trello",
            "icon": "trello-plain",
            },
            {
            "name": "SourceTree",
            "icon": "sourcetree-plain",
            },
            {
            "name": "Doctrine",
            "icon": "doctrine-plain",
            },
            {
            "name": "Composer",
            "icon": "composer-plain",
            },
            {
            "name": "Bower",
            "icon": "bower-plain",
            },
        ],
        },
        {
        "id": "so",
        "name": "SO",
        "items": [
            {
            "name": "Mac OS",
            "icon": "apple-plain",
            },
            {
            "name": "Windows",
            "icon": "windows8-plain",
            },
            {
            "name": "Ubuntu",
            "icon": "ubuntu-plain",
            },
            {
            "name": "Debian",
            "icon": "debian-plain",
            },
            {
            "name": "Android",
            "icon": "android-plain",
            },
            {
            "name": "Docker",
            "icon": "docker-plain",
            },
        ],
        },
    ]
    return jsonify(skills)

class WorksResource(Resource):
  @cross_origin()
  def get(self):
      data = [
      {
          "company": "Dentix",
          "date": "abril 2019 \n actualmente",
          "fdate": "01/05/2019",
          "position": "FullStack developer",
          "description": "Digitalización total de la compañía, con una estructura de colas de trabajo y microservicios",
          "resume": "Microservicios",
          "skills": ["Python", "vue.js", "SQL Server", "gitlab", "Mongo", "flask", "django", "docker"]
      },
      {
          "company": "ThinkSmart",
          "date": "mayo 2018 \n abril 2019",
          "fdate": "01/05/2018",
          "position": "FullStack developer",
          "description": "Creación y mantenimiento de programa de incentivos creados según especificaciones de cada cliente, usando un framework propio",
          "resume": "Webapp",
          "skills": ["PHP", "Javascript", "SQL Server", "GIT"]
      },
      {
          "company": "Everyone Plus",
          "date": "abril 2014 \n mayo 2018",
          "fdate": "01/05/2014",
          "position": "FullStack developer en el equipo Multimedia",
          "description": "Creación de los proyectos desde la toma de contacto con el cliente, pasando por la fase de diseño, maquetación y desarrollo, hasta la entrega del proyecto terminado.",
          "resume": "Web, webapp, api, promopages",
          "skills": ["PHP", "Javascript", "Angular", "HTML5", "CSS3", "SASS", "Bootstrap", "Symfony", "jQuery", "MariaDB",  "MySQL", "Wordpress", "Prestashop", "Drupal", "entre otros"]
      },
      {
          "company": "Penkus Alchemy",
          "date": "junio 2013 \n enero 2014",
          "fdate": "01/06/2013",
          "position": "Programador web",
          "description": "Creación de los proyectos desde la fase de diseño, maquetación y desarrollo, hasta la entrega del proyecto terminado.",
          "resume": "Web",
          "skills": ["PHP", "Javascript", "Wordpress", "HTML5", "CSS3",  "MySQL", "Prestashop", "Drupal", "Magento", "Joomla"]
      },
      {
          "company": "GrupoClick",
          "date": "enero 2010 \n noviembre 2013",
          "fdate": "01/01/2010",
          "position": "Programador web",
          "description": "Creación y mantenimiento de páginas web desde la fase de diseño, maquetación y desarrollo, hasta la entrega del proyecto terminado.",
          "resume": "Web",
          "skills": ["PHP", "Javascript", "HTML5", "CSS3", "Wordpress", "Joolma", "Prestashop"]
      },
      {
          "company": "Spain Phone Card",
          "date": "noviembre 2008 \n julio 2012",
          "fdate": "01/11/2008",
          "position": "Técnico informático, Dependiente",
          "description": "",
          "resume": "",
          "skills": ["PHP", "Javascript"]
      }
      ]
      return jsonify(data)

class CoursesResource(Resource):
  @cross_origin()
  def get(self):
      data =  [
      {
          "title": "Técnico Superior Informática",
          "center": "Colegio Universitario de los Teques Cecilio Acosta",
          "date": "2002 - 2006"
      },
      {
          "title": "Bachiller en ciencias y tecnologí­a",
          "center": "Unidad Educativa Manuel Marí­a Villalobos",
          "date": "1995 - 2000"
      }
      ]
      return jsonify(data)
