from odoo.osv import expression

domain = []

# domain = [[('phone', '=','123456789')],[('email','=','auto@email.com')]]
domain.append([('phone', '=','123456789')])
domain.append([('email','=','auto@email.com')])

domain = expression.OR(domain) if len(domain)>0 else False

print(domain)
