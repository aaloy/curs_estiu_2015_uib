Centralita es un proyecto pensado para introducir a los alumnos
del "I Campus d'Estiu d'Innovació Tecnològica" en la programaición
Python y Django.

No es un compendio de mejores prácticas, sirve para lo que sirve.

La aplicación sigue una estructura pensada para poder ser distribuida
e instalada por sistemas de despliegue automatizados. En lugar
de que el proyecto y la apliación principal tengan el mismo nombre
se ha optado por llamar `main` a la aplicación que contienen los 
settings.

Esto implica que se han modificado las urls, wsgi, y demás módulos
que dependen de dicho nombre. A lo largo del tiempo hemos visto
que esta estructura presenta muchos menos problemas, ya que
ayuda a identificar dónde se encuentran las configuraciones, incluso
para el neófito, permite la automatización más eficiente y
evita errores de importación relativos a la confusión del nombre del
módulo con el nombre del proyecto.

A los efectos de enseñar la aplicación se ha optado por hacer commit 
también de base de datos, facilitando así la labor de instalación y
puesta en marcha (se recomienda seguir el tutorial de Django) por
parte de los alumnos del curso.
