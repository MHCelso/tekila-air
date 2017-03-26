# Tekila Aires

## Configuraciones:
1. En MySQL crea una base de datos "DB_NAME".

	1.1. Crea un entorno virtual y al activarle hazle `git clone` con la url de mi proyecto.
	
	1.2. Instala los requeriemientos con pip install -r requiriments.txt

		* Coloca en settings.py de la carpeta airestekuila lo siguiente:
	  	la ubicacion de mi archivo 'my.cnf' es: '/etc/mysql/my.cnf' ya que utilizo una distribucion de linux.

			DATABASES = {
    			'default': {
        			'ENGINE': 'django.db.backends.mysql',
        			'OPTIONS': {
            			'read_default_file': '/etc/mysql/my.cnf',
            			'charset': 'utf8mb4'
        			},
    			}
			}
	

2. Ve al archivo de configuración my.cnf de MySQL.
	* La ubicacion de mi archivo 'my.cnf' es: '/etc/mysql/my.cnf' ya que utilizo una distribucion de linux.

	* Coloca en el apartado [client] lo siguiente:
		# ejemplo:

			[client]
			database = DB_NAME
			host = localhost
			user = DB_USER
			password = DB_PASSWORD
			default-character-set = utf8

3. ¡Activar Proyecto!.
	
	3.1. Activa tu entorno virtual y colocate dentro de la carpeta airestekuila
		 ahí se encuentra un archivo manage.py

	3.2. Teclea: python manage.py makemigrations.

	3.3. Teclea: python manage.py migrate.

	3.4. Teclea: python manage.py createsuperuser.

		3.4.1. Teclea los datos que te pide sin olvidarlos 
		con ellos tendras acceso al administrador de Django
		y a la aplicacion web. 

	3.5. Si has llegado sin ningun problema hasta aqui teclea:
	`python manage.py runserver`

	3.6. Si no tuviste problemas abre tu navegador y ve a la direccion:
		 `localhost:8000` ya que es donde corre nuestro proyecto.

4. Logueate con tu superusuario		 
5. 1.- Crea tu primer Cliente.
6. 2.- Crea tu primer Vuelo.
7. Despues de todo podrás darle el password a tus clientes y ellos podran agendar sus vuelos y cancelarlos,
	mietras tanto con tu super usuario podras tener de esos provilegios y de tambien borrar a los clientes que desees.