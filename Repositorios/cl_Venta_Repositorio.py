import pyodbc;
from Utilidades.cl_Database import cl_Database; 
from Nucleo.cl_Venta import cl_Venta;


class cl_Venta_Repositorio:
    
    def Listar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            
            if(not id):
                consulta: str = f"CALL SP_Ventas_Listar(NULL, @p_resultado);";
            else: 
                consulta: str = f"CALL SP_Ventas_Listar({id}, @p_resultado);";
            
            cursor = conexion.cursor();
            cursor.execute(consulta);

            respuesta: dict = { };
            contador = 0;
            for elemento in cursor:
                #LLENAR LISTA DE CLIENTES
                venta: cl_Venta = cl_Venta();
                venta.SetVentaID(elemento[0]);
                venta.SetClienteID(elemento[0]);
                venta.SetFecha(elemento[1]);
                venta.SetTotal(elemento[2]);
                respuesta[str(contador)] = venta.__dict__;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;