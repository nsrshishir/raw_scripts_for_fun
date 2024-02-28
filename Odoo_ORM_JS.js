// CREATE METHOD JS
await this.rpc({
  model: 'product.template',
  method: 'create',
  args: [{
    'name': 'Classic Chair',
    'is_published': true,
    'attribute_line_ids': [[0, 0, {
      'attribute_id': attributeId,
      'value_ids': [
        [0, 0, { 'name': 'green', 'attribute_id': attributeId, 'sequence': 3 }],
        [0, 0, { 'name': 'yellow', 'attribute_id': attributeId, 'sequence': 4 }],
      ],
    }]],
    'alternative_product_ids': [[6, 0, [productId]]],
  }],
});

// UPDATE/WRITE METHOD JS

await this.rpc({
  model: 'pos.order',
  method: 'write',
  args: [[orderId], { partner_id: newClient.id }],
  kwargs: { context: this.env.session.user_context },
});

// CALL A SPECIFIC FUNCTION JS

await this.rpc(
  {
    model: 'pos.order',
    method: 'action_pos_order_invoice',
    args: [orderId],
    kwargs: { context: this.env.session.user_context },
  },
  {
    timeout: 30000,
    shadow: true,
});


// SEARCH READ METHOD JS


await this.rpc({
  model: 'pos.order',
  method: 'search_read',
  domain: [['id', 'in', order_server_ids]],
  fields: ['name'],
  context: session.user_context,
});


// DELETE RECORD JS


await this._rpc({
  model: 'payment.token',
  method: 'unlink',
  args: [pm_id],
})

// FOR EACH LOOP FOR SEARCH READ

Object.forEach((record) => {
    console.log("DO YOUR THING WITH EACH record",record);
});