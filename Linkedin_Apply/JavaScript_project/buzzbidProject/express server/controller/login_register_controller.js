import db from '../db.js';

const loginUser = async (req, res) => {
  const { username, password } = req.body;

  try {
    const query = 'SELECT * FROM alluser WHERE username = $1 AND password = $2';
    const result = await db.query(query, [username, password]);

    if (result.rows.length > 0) {
      res
        .status(200)
        .json({ message: 'Login successful', user: result.rows[0] });
    } else {
      res.status(401).json({ message: 'Invalid username or password' });
    }
  } catch (error) {
    console.error('Error executing query:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
};

const RegisterUser = async (req, res) => {
  const { username, firstName, lastName, password } = req.body;

  try {
    const query =
      'INSERT INTO alluser (username, first_name, last_name, password) VALUES ($1, $2, $3, $4)';
    const result = await db.query(query, [
      username,
      firstName,
      lastName,
      password,
    ]);
    console.log('Received Register request:', {
      username,
      firstName,
      lastName,
      password,
    });

    res.status(200).json({ message: 'User registered successfully' });
  } catch (error) {
    console.error('Error executing query:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
};

const getPostionByUserName = async (req, res) => {
  const { username } = req.params; // Accessing the username from the URL parameter
  const query = 'SELECT position FROM AdminUser WHERE username=$1;';

  try {
    const result = await db.query(query, [username]);

    if (result.rows.length > 0) {
      // If the user is found, send back the position
      res.json({ success: true, position: result.rows[0].position });
    } else {
      // If no user is found, send a 404 response
      res
        .status(404)
        .json({ success: false, message: 'User not found or not an admin' });
    }
  } catch (error) {
    console.error('Error querying database:', error);
    res.status(500).json({ success: false, message: 'Internal server error' });
  }
};
const getUserByItemID = async (req, res) => {
  try {
    const { itemID } = req.params;
    console.log(req.params, 'itemID');

    const queryText = 'SELECT username FROM item WHERE item.itemID = $1';

    const { rows } = await db.query(queryText, [itemID]);

    if (rows.length > 0) {
      res.status(200).json({ username: rows[0].username });
    } else {
      res
        .status(404)
        .json({ message: 'User not found for the given item ID.' });
    }
  } catch (error) {
    console.error('Error occurred while fetching user by item ID:', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
};

export { loginUser, RegisterUser, getPostionByUserName, getUserByItemID };
