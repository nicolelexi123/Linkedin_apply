import db from '../db.js';

export const AuctionResult = async (req, res) => {
  const query = `SELECT i.itemID,
    i.name AS item_name, CASE
    WHEN ci.itemID IS NOT NULL THEN NULL WHEN mb.amount = i.get_it_now THEN mb.amount WHEN mb.amount >= i.min_sale THEN mb.amount ELSE NULL
    END AS sale_price, CASE
    WHEN ci.itemID IS NOT NULL THEN 'CANCELED' WHEN mb.amount = i.get_it_now THEN mb.username WHEN mb.amount >= i.min_sale THEN mb.username ELSE NULL
    END AS winner, CASE
    WHEN ci.itemID IS NOT NULL THEN ci.datetime
    WHEN mb.amount = i.get_it_now THEN mb.datetime
    ELSE i.start_datetime + INTERVAL '1 DAY' * i.auction_length
    END AS auction_end_time FROM Item i
    LEFT JOIN
    (
    SELECT itemID,
    amount, username,
    datetime,
    RANK() OVER(PARTITION BY itemID ORDER BY amount DESC) as rank FROM Bid
    ) mb ON i.itemID = mb.itemID AND mb.rank = 1 LEFT JOIN CancelItem ci ON i.itemID = ci.itemID WHERE (
    ci.itemID IS NOT NULL OR
    mb.amount = i.get_it_now OR (CURRENT_TIMESTAMP>i.start_datetime + INTERVAL '1 DAY' *
    i.auction_length)
    )
    ORDER BY auction_end_time DESC`;

  try {
    const { rows } = await db.query(query);
    res.json(rows);
  } catch (error) {
    console.error('Error querying auction results:', error);
    res.status(500).json({ message: 'Internal server error.' });
  }
};

export const getWinner = async (req, res) => {
  const itemId = req.params.itemID;

  const query = `
    SELECT i.itemID,
      i.name AS item_name,
      CASE
        WHEN ci.itemID IS NOT NULL THEN NULL
        WHEN mb.amount = i.get_it_now THEN mb.amount
        WHEN mb.amount >= i.min_sale THEN mb.amount
        ELSE NULL
      END AS sale_price,
      CASE
        WHEN ci.itemID IS NOT NULL THEN 'CANCELED'
        WHEN mb.amount = i.get_it_now THEN mb.username
        WHEN mb.amount >= i.min_sale THEN mb.username
        ELSE NULL
      END AS winner,
      CASE
        WHEN ci.itemID IS NOT NULL THEN ci.datetime
        WHEN mb.amount = i.get_it_now THEN mb.datetime
        ELSE i.start_datetime + INTERVAL '1 DAY' * i.auction_length
      END AS auction_end_time
    FROM Item i
    LEFT JOIN (
      SELECT itemID, amount, username, datetime,
        RANK() OVER (PARTITION BY itemID ORDER BY amount DESC) as rank
      FROM Bid
    ) mb ON i.itemID = mb.itemID AND mb.rank = 1
    LEFT JOIN CancelItem ci ON i.itemID = ci.itemID
    WHERE (
      ci.itemID IS NOT NULL OR
      mb.amount = i.get_it_now OR
      (CURRENT_TIMESTAMP > i.start_datetime + INTERVAL '1 DAY' * i.auction_length)
    )
    AND i.itemID = $1
    ORDER BY auction_end_time DESC`;

  try {
    const { rows } = await db.query(query, [itemId]);
    res.json(rows);
  } catch (error) {
    console.error('Error querying auction results:', error);
    res.status(500).json({ message: 'Internal server error.' });
  }
};
