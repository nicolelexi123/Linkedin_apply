import db from '../db.js';

const bidOnItem = async (req, res) => {
  // Extracting `id` from URL parameters and `username` & `amount` from request body
  const { itemID } = req.params;
  const { username, amount } = req.body;

  try {
    const query =
      'INSERT INTO Bid (username, itemID, amount, datetime) VALUES ($1, $2, $3, CURRENT_TIMESTAMP)';

    const result = await db.query(query, [username, itemID, amount]);
    console.log('req.body', req.body);
    res.status(200).json({ message: 'Bid placed successfully.' });
  } catch (error) {
    console.error('Error occurred while placing bid:', error);

    res.status(500).json({ message: 'Internal Server Error' });
  }
};

export default bidOnItem;
