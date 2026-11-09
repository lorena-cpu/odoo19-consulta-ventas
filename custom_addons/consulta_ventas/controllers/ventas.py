
from odoo import http
from odoo.http import request
from datetime import datetime
import calendar


class ConsultaVentasController(http.Controller):

    @http.route(
        '/api/consulta-ventas',
        type='http',
        auth='user',
        methods=['GET'],
        csrf=False
    )
    def consultar_ventas(self, cliente_id=None, anio=None, mes=None, **kwargs):
        if not request.env.user.has_group(
            'sales_team.group_sale_salesman'
        ):
            return request.make_json_response({
                'error': 'No tiene permisos para consultar ventas'
            }, status=403)

        try:
            if not cliente_id or not anio or not mes:
                return request.make_json_response({
                    'error': 'Debe indicar cliente_id, anio y mes'
                }, status=400)

            cliente_id = int(cliente_id)
            anio = int(anio)
            mes = int(mes)

            if cliente_id <= 0 or not (1 <= mes <= 12):
                raise ValueError()

            ultimo_dia = calendar.monthrange(anio, mes)[1]

            fecha_inicio = datetime(anio, mes, 1)
            fecha_fin = datetime(anio, mes, ultimo_dia, 23, 59, 59)

            cliente = request.env['res.partner'].search([
                ('id', '=', cliente_id)
            ], limit=1)

            if not cliente:
                return request.make_json_response({
                    'error': 'Cliente no encontrado'
                }, status=404)

            ventas = request.env['sale.order'].search([
                ('partner_id', '=', cliente.id),
                ('state', '=', 'sale'),
                ('date_order', '>=', fecha_inicio),
                ('date_order', '<=', fecha_fin)
            ])

            total = sum(ventas.mapped('amount_total'))

            return request.make_json_response({
                'cliente': cliente.name,
                'anio': anio,
                'mes': mes,
                'cantidad_ventas': len(ventas),
                'total_compras': total
            })

        except (ValueError, OverflowError):
            return request.make_json_response({
                'error': 'Parametros invalidos'
            }, status=400)
