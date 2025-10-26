module.exports = (err, req, res, next) => {
  if (err?.name === 'CastError' && err?.kind === 'ObjectId') {
    return res.status(400).json({ message: 'Invalid id format.' });
  }

  if (err?.name === 'ValidationError') {
    const errors = Object.values(err.errors || {}).map(e => e.message);
    return res.status(400).json({ message: 'Validation failed', errors });
  }

  if (err?.code === 11000) {
    return res.status(409).json({ message: 'Duplicate key error', keyValue: err.keyValue });
  }

  console.error(err.stack || err);
  res.status(500).json({ message: 'Internal Server Error' });
};