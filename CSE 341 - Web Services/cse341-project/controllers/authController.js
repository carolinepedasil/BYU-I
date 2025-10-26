const { addUser } = require('../services/userService');

exports.register = async (req, res, next) => {
  try {
    const { username, password } = req.body;

    await addUser(username, password);
    res.status(201).json({ message: 'User registered' });
  } catch (err) {
    if (err.message.includes('exists')) {
      return res.status(409).json({ message: 'User already exists' });
    }
    next(err);
  }
};

exports.loginSuccess = (req, res) => {
  res.status(200).json({ message: 'Login successful', user: req.user });
};

exports.loginFail = (req, res) => {
  res.status(401).json({ message: 'Invalid username or password' });
};

exports.logout = (req, res) => {
  req.logout(() => {
    res.status(200).json({ message: 'Logged out' });
  });
};

exports.protectedRoute = (req, res) => {
  res.status(200).json({ message: 'You are authenticated', user: req.user });
};
