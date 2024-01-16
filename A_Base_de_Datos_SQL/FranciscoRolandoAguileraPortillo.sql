-- PRUEBA A - BASE DE DATOS SQL
-- Francisco Rolando Aguilera Portillo

-- Seleccionamos la base de datos dwPYtest
USE dwPYtest;

-- Seleccionamos los registros de facturación de la tabla TypeII_factura_H para la fecha 01-05-2023, utilizando la función STR_TO_DATE
SELECT *
FROM TypeII_factura_H
WHERE STR_TO_DATE(fecha_factura, '%d-%m-%Y') = '2023-05-01';

-- Utilizamos una consulta anidada para filtrar los registros con clientes activos (credit_status = 'O')
SELECT *
FROM TypeII_factura_H
WHERE STR_TO_DATE(fecha_factura, '%d-%m-%Y') = '2023-05-01'
AND id_cliente IN (SELECT id_cliente FROM cliente WHERE credit_status = 'O');

-- Obtenemos el mismo resultado aplicando INNER JOIN, pero en esta ocasión traemos el credit_status por igual
SELECT h.*, c.credit_status
FROM TypeII_factura_H h
INNER JOIN cliente c ON h.id_cliente = c.id_cliente
WHERE STR_TO_DATE(h.fecha_factura, '%d-%m-%Y') = '2023-05-01'
AND c.credit_status = 'O';