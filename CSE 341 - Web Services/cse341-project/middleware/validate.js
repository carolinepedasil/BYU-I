function validateProduct(req, res, next) {
  const body = req.body || {};
  const errors = [];

  if (!body.name || typeof body.name !== 'string') errors.push('name (string) is required');
  if (body.description && typeof body.description !== 'string') errors.push('description must be a string');
  if (body.price === undefined || typeof body.price !== 'number' || body.price < 0) errors.push('price (number >= 0) is required');
  if (body.category && typeof body.category !== 'string') errors.push('category must be a string');
  if (body.stock === undefined || typeof body.stock !== 'number' || body.stock < 0) errors.push('stock (number >= 0) is required');
  if (body.imageUrl && typeof body.imageUrl !== 'string') errors.push('imageUrl must be a string');
  if (!body.sku || typeof body.sku !== 'string') errors.push('sku (string) is required');

  if (errors.length) return res.status(400).json({ message: 'Validation failed', errors });
  next();
}

function validateCategory(req, res, next) {
  const body = req.body || {};
  const errors = [];
  if (!body.name || typeof body.name !== 'string') errors.push('name (string) is required');
  if (body.description && typeof body.description !== 'string') errors.push('description must be a string');
  if (errors.length) return res.status(400).json({ message: 'Validation failed', errors });
  next();
}

function validateObjectId(req, res, next) {
  const id = req.params.id;
  if (!/^[0-9a-fA-F]{24}$/.test(id)) {
    return res.status(400).json({ message: 'Invalid id format. Must be a 24-char hex string.' });
  }
  next();
}

module.exports = { validateProduct, validateCategory, validateObjectId };
