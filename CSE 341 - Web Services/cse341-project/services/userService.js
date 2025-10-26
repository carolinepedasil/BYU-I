const bcrypt = require('bcrypt');
const User = require('../models/userModel');

const findUser = async (username) => {
  return await User.findOne({ username });
};

const addUser = async (username, password) => {
  const existingUser = await User.findOne({ username });
  if (existingUser) throw new Error('User already exists');

  const hashedPassword = await bcrypt.hash(password, 10);
  const newUser = new User({ username, password: hashedPassword });
  await newUser.save();
  return newUser;
};

module.exports = { findUser, addUser };
