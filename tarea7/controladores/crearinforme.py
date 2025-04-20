import os
import pyreportjasper

def compiling(): # Si no se utiliza JasperSoft Studio
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/informes/Agrupamiento.jrxml'
    print(input_file)
    #jasper = pyjasper.JasperPy()
    jasper = pyreportjasper.PyReportJasper()
    jasper.config(input_file)
    jasper.compile()



def processing():
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/informes/Agrupamiento.jrxml'
    output = os.path.dirname(os.path.abspath(__file__)) + '/informes/pdf'
   
    #jasper = pyjasper.JasperPy()
    jasper = pyreportjasper.PyReportJasper()
    jasper.process(
        input_file, output_file=output, format_list=["pdf", "rtf"])

def listing_parameters(): #listar parámetros
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/informes/Listado_clientes_param_filtrado.jrxml'
    jasper = pyreportjasper.PyReportJasper()
    jasper.config(input_file=input_file)
    output = jasper.list_report_params()
    print(output)



def xml_to_pdf(): #Convertir XML en PDF
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/CancelAck.jrxml'

    output = os.path.dirname(os.path.abspath(__file__)) + '/output/_CancelAck'

    data_file = os.path.dirname(os.path.abspath(__file__)) + \
        '/examples/CancelAck.xml'

    jasper = pyreportjasper.PyReportJasper()

    jasper.process(
        input_file,
        output=output,
        format_list=["pdf"],
        parameters={},
        db_connection={
            'data_file': data_file,
            'driver': 'xml',
            'xml_xpath': '/CancelResponse/CancelResult/ID',
        },
        locale='pt_BR'  # LOCALE Ex.:(en_US, de_GE)
    )

    print('Result is the file below.')
    print(output + '.pdf')

def json_to_pdf(): # Informe en JSON
    input_file = os.path.dirname(os.path.abspath(__file__)) + \
                 '/examples/json.jrxml'

    output = os.path.dirname(os.path.abspath(__file__)) + '/output/_Contacts'
    json_query = 'contacts.person'

    data_file = os.path.dirname(os.path.abspath(__file__)) + \
        '/examples/contacts.json'

    jasper = pyreportjasper.PyReportJasper()
    jasper.process(
        input_file,
        output=output,
        format_list=["pdf"],
        parameters={},
        db_connection={
            'data_file': data_file,
            'driver': 'json',
            'json_query': json_query,
        },
        locale='pt_BR'  # LOCALE Ex.:(en_US, de_GE)
    )

    print('Result is the file below.')
    print(output + '.pdf')


def advanced_example_using_database(ficheroEntrada, ficheroSalida,parametros):
    
    input_file = ficheroEntrada
    output_file = ficheroSalida 
    """
    #conexión para postgreSQL
    con = {
        'driver': 'postgres',
        'username': 'DB_USERNAME',
        'password': 'DB_PASSWORD',
        'host': 'DB_HOST',
        'database': 'DB_DATABASE',
        'schema': 'DB_SCHEMA',
        'port': '5432'
    }"""
    
    """
    #conexión para mysql
    con = {
    'driver': 'mysql',
     'username': 'luis',
     'password': 'Brianda20',
     'host': 'localhost',
     'database': 'fabrica',
     'schema': 'DB_SCHEMA',
     'port': '3306',
     'jdbc_driver': 'com.mysql.cj.jdbc.Driver',
     'jdbc_dir': 'libs/jdbc/mysql-connector-java-8.0.30.jar'
    }"""
    

    """
    Conexión para SQLIte. A diferencia de postgreSQL y MySQL, pyreportjasper no viene preparado para
    SQLite, por lo que es necesario modificar el código para que pueda utilizar también SQLite.
    Para ello basta con añadir en el kugar adecuado de db.py el siguiente código:
        elif dbtype == "sqlite":
            driver = config.dbDriver
            #port = config.dbPort or 5434
            dbname = config.dataFile
            connect_string = "jdbc:sqlite:{}".format(dbname)

    Por otra parte, en referencia a los propios reportes .jrxml, recordar que algunas funciones SQL 
    utilizadas en MySQL no funcionan en SQLite, como     las relacionadas con fechas.
    También tener en cuenta que SQLite es menos permisivo con los tipos de los datos en los Dataset
    de los reportes .jrxml: es necesario indicar claramente el tipo (string, integer, float...)

    """
    con = {
    'driver': 'sqlite',
    'jdbc_driver': 'org.sqlite.JDBC',
    'jdbc_dir': 'libs/jdbc/sqlite-jdbc-3.7.2.jar',
    'data_file': '/home/luis/Dropbox/Instituto/VirtualShared/DI/EjemploTema7/modelos/fabrica.db',
    
    }
    #libs/jdbc/sqlite-jdbc-3.7.2.jar
    
    jasper = pyreportjasper.PyReportJasper()
   
    jasper.process(
        input_file,
        output_file,
       
        #format_list=["pdf", "rtf", "xml"],
        format_list=["pdf"],
        parameters=parametros,
        db_connection=con,
        locale='es_ES'  # LOCALE Ex.:(en_US, de_GE)
    )
   # print(jasper.list_report_params)

if __name__ == "__main__":

    #compiling()
    #processing()
    advanced_example_using_database()
    #listing_parameters()

"""comboPDF.setModel(new DefaultComboBoxModel(new String[] {"Agrupamiento.jrxml", 
"AgrupamientoComplejo.jrxml", "Graficos.jrxml", "Listado_clientes.jrxml", 
"Listado_clientes_parametros.jrxml", "Listado_clientes_param_filtrado.jrxml", 
"Listado_clientes_param_ordenar.jrxml", "Pedidos_clientes.jrxml", 
"Pedidos_clientes_enca_pie.jrxml", "Subinformes.jrxml", "SubinformesSecundario.jasper", 
"SubinformesSecundario.jrxml", "SubinformesSecundariotfno.jasper", 
"SubinformesSecundariotfno.jrxml", "Subtotal.jrxml"}));"""

"""txtdirinformes = new JTextField();
		txtdirinformes.setText("C:\\Users\\dptoinformatica\\Downloads\\di");
	"""	
