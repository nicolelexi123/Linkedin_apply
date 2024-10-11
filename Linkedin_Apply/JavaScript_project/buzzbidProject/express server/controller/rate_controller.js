import db from '../db.js';
import Joi from 'joi';

const ratingSchema = Joi.object({
  itemID: Joi.number().integer().required(),
  rated_by: Joi.string().required(),
  comment: Joi.string().max(300).allow('', null),
  rating: Joi.number().min(0).max(5).required(),
});
export const rateAdd = async (req, res) => {
  const { itemID, rated_by, comment, rating } = req.body;

  const { error } = ratingSchema.validate({
    itemID,
    rated_by,
    comment,
    rating,
  });
  if (error) {
    return res
      .status(400)
      .json({ message: 'Validation error', details: error.details });
  }

  const queryText =
    'INSERT INTO Rating (itemID, rated_by, comment, rating, rate_datetime) VALUES ($1, $2, $3, $4, CURRENT_TIMESTAMP)';
  const queryValues = [itemID, rated_by, comment, rating];

  try {
    const result = await db.query(queryText, queryValues);
    res.json({ message: 'Rating added successfully' });
  } catch (error) {
    console.error('Error adding rating:', error);
    res.status(500).json({ message: 'Internal server error.' });
  }
};
export const rateDel = async (req, res) => {
  const itemID = req.body.itemID;

  const rated_by = req.body.rated_by;

  const verifyQuery = `
      SELECT * FROM Rating
      WHERE itemID = $1 AND rated_by = $2
  `;

  try {
    const verifyResult = await db.query(verifyQuery, [itemID, rated_by]);
    if (verifyResult.rows.length === 0) {
      return res
        .status(404)
        .json({
          message:
            'Rating not found or you do not have permission to delete this rating.',
        });
    }

    const deleteQuery = `
          DELETE FROM Rating
          WHERE itemID = $1 AND rated_by = $2
      `;
    await db.query(deleteQuery, [itemID, rated_by]);

    res.json({ message: 'Rating deleted successfully.' });
  } catch (error) {
    console.error('Error deleting rating:', error);
    res.status(500).json({ message: 'Internal server error.' });
  }
};

export const getRatingsByNameForItemId = async (req, res) => {
  const { id } = req.params;
  try {
    const itemNameQuery = 'SELECT name FROM Item WHERE itemID = $1';
    const itemNameResult = await db.query(itemNameQuery, [id]);

    if (itemNameResult.rows.length === 0) {
      return res.status(404).json({ message: 'Item not found.' });
    }

    const itemName = itemNameResult.rows[0].name;
    console.log(itemName);

    const ratingsQuery = `
      SELECT
        i.name,
        r.itemid,
        r.rated_By,
        r.rate_datetime,
        r.rating,
        r.comment,
        AVG(r.rating) OVER(PARTITION BY i.name) AS average_rating
      FROM
        Item i
      LEFT JOIN rating r ON i.itemID = r.itemID
      WHERE i.name = $1
      ORDER BY rate_datetime DESC`;

    const result = await db.query(ratingsQuery, [itemName]);
    console.log(result.rows[0]);

    res.json({
      firstResult: result.rows[0],
      allResult: result.rows,
    });
  } catch (error) {
    console.error(error);
    res
      .status(500)
      .json({ message: 'An error occurred while fetching the ratings.' });
  }
};

export const getRateByItemidanduser = async (req, res) => {
  // Extract itemid and rated_by from request parameters or body
  const { itemid, rated_by } = req.params; // or req.body, depending on how you're sending data

  const query = `SELECT * FROM rating WHERE itemid = $1 AND rated_by = $2`;

  try {
    const result = await db.query(query, [itemid, rated_by]);

    if (result.rows.length > 0) {
      res.json(result.rows[0]);
    } else {
      res
        .status(404)
        .json({ message: 'No rating found for the provided itemid and user.' });
    }
  } catch (error) {
    console.error('Error querying rating:', error);
    res.status(500).json({ message: 'Internal server error.' });
  }
};
